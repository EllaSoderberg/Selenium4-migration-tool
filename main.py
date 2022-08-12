import os
import glob

PATH_TO_FOLDER = "Add the path to the folder containing python files"


def get_files(folder):
    """
    Gets the name of all files in a directory.
    :param folder: The path to the folder
    :return: A list with the full paths to the files
    """
    files = []
    for file in glob.glob(folder + "\\*.py"):
        files.append(file)
    subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]
    if len(subfolders) != 0:
        subfiles = []
        for folder in subfolders:
            subfiles += get_files(folder)
        files += subfiles
    return files


def migrate_file(file):
    """
    Reads a file and substitutes the "find_element_by" with the "find_element(By" syntax of selenium 4.
    Immediately overwrites the file.
    :param file: the path to the file to be read
    """
    with open(file, "r") as codefile:
        lines = codefile.readlines()
        lines.insert(0, "from selenium.webdriver.common.by import By\n")
        i = 0

        for line in lines:
            try:
                if "find_element_by" in line:
                    after_find = line.split("find_element_by")[-1]
                    by_type = after_find.split("(")[0][1:].upper()
                    #print(after_find)
                    argument = after_find.split('"')[1]
                    lines[i] = line.replace(f'_by{after_find.split(")")[0]}', f'(By.{by_type}, "{argument}"')
                elif "find_elements_by" in line:
                    after_find = line.split("find_elements_by")[-1]
                    by_type = after_find.split("(")[0][1:].upper()
                    argument = after_find.split('"')[1]
                    lines[i] = line.replace(f'_by{after_find.split(")")[0]}', f'(By.{by_type}, "{argument}"')
            except Exception:
                print("Skipped", file, line)
            i += 1
        with open(file, "w") as writefile:
            if lines:
                writefile.writelines(lines)


if __name__ == '__main__':
    for path in get_files(PATH_TO_FOLDER):
        migrate_file(path)

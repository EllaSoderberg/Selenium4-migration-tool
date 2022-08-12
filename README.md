This is a tool to help in the migration from Selenium 3 to Selenium 4.

In Selenium 3 the syntax to find elements is for example: 

`find_element_by_xpath("xpath string")`

This script will convert the syntax to:

`find_element(By.XPATH, "xpath string")`

It will also import `By` from Selenium
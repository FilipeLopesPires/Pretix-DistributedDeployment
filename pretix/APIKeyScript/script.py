'''

Title: Pretix API Key Generator

Description: Python script that uses Selenium to create an organization inside Pretix, generates a secret API key for sending REST requests and stores it in a plaintext file.
Note: The script assumes that you have already deployed Pretix (using docker-compose).

Authors: Filipe Pires (85122) and João Alegria (85048)

'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Change these variables if you wish to personalize the script results
organization_name = "default"

# Open Firefox, navigate to Pretix and enter into the login page
browser = webdriver.Firefox()
browser.get("http://localhost:8888/")
head_over_here = browser.find_element(s)_by_link_text("head over here")
head_over_here.click()
wait = WebDriverWait( browser, 2 )
assert browser.find_element_by_id("id_email")

# Login as an administrator
email = browser.find_element_by_id("id_email")
password = browser.find_element_by_id("id_password")
submit = browser.find_element_by_xpath("//button[contains(text(),'Log in')]")
username.send_keys("admin@localhost")
password.send_keys("admin")
submit.click()
wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Dashboard pretix.de"

# Create Organization
admin = browser.find_element_by_id("button-sudo")
admin.click()
wait = WebDriverWait( browser, 2 )

organizers = browser.find_element(s)_by_link_text("Organizers")
organizers.click()
wait = WebDriverWait( browser, 2 )

create_organizer = browser.find_element(s)_by_link_text("Create a new organizer")
create_organizer.click()
wait = WebDriverWait( browser, 2 )

organizer_name = browser.find_element_by_id("id_name")
organizer_name.send_keys(organization_name)
organizer_short = browser.find_element_by_id("id_slug")
organizer_short.send_keys(organization_name)
save = browser.find_element_by_xpath("//button[contains(text(),'Log in')]")
save.click()
wait = WebDriverWait( browser, 5 )
assert browser.find_elements_by_class_name("alert alert-success")

# Create API Token
teams = browser.find_element(s)_by_link_text("Teams")
teams.click()
wait = WebDriverWait( browser, 2 )
# ...

# https://www.selenium.dev/documentation/en/webdriver/driver_requirements/





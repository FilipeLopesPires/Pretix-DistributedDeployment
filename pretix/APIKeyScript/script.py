'''

Title: Pretix API Key Generator

Description: Python script that uses Selenium to create an organization inside Pretix, generates a secret API key for sending REST requests and stores it in a plaintext file. The script also creates a default event.
Note: The script assumes that you have already deployed Pretix (using docker-compose).

Authors: Filipe Pires (85122) and João Alegria (85048)

'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Change these variables if you wish to personalize the script results
admin_email = "admin@localhost"
admin_pwd = "admin"
host_address = "http://localhost:80"
organizer_name = "ws"


# Open Firefox, navigate to Pretix and enter into the login page
browser = webdriver.Firefox()
browser.get(host_address)
head_over_here = browser.find_element_by_link_text("head over here")
head_over_here.click()
wait = WebDriverWait( browser, 2 )
assert browser.find_element_by_id("id_email")

# Login as an administrator
email = browser.find_element_by_id("id_email")
password = browser.find_element_by_id("id_password")
submit = browser.find_element_by_xpath("//button[contains(text(),'Log in')]")
email.send_keys(admin_email)
password.send_keys(admin_pwd)
submit.click()
wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Dashboard pretix.de"

# Create Organizer
admin = browser.find_element_by_id("button-sudo")
admin.click()
wait = WebDriverWait( browser, 2 )

organizers = browser.find_element_by_link_text("Organizers")
organizers.click()
wait = WebDriverWait( browser, 2 )

create_organizer = browser.find_element_by_link_text("Create a new organizer")
create_organizer.click()
wait = WebDriverWait( browser, 2 )

organizer_name = browser.find_element_by_id("id_name")
organizer_name.send_keys(organizer_name)
organizer_short = browser.find_element_by_id("id_slug")
organizer_short.send_keys(organizer_name)
save = browser.find_element_by_xpath("//button[contains(text(),'Log in')]")
save.click()
wait = WebDriverWait( browser, 5 )
assert browser.find_elements_by_class_name("alert alert-success")

# Create API Token
teams = browser.find_element_by_link_text("Teams")
teams.click()
wait = WebDriverWait( browser, 2 )
# ...

# https://www.selenium.dev/documentation/en/webdriver/driver_requirements/


'''
Steps to prepare pretix for testing

1. Create organizer
- enter as admin (admin@localhost admin)
- activate admin mode
- go to organizers
- create a new organizer
- fill form and create organizer

2. Create event
- create a new event
- select english and continue
- fill form (event name, short form, start and end times) and continue
- remove maximum ticket capacity (to make it infinite) and save
- go to settings > plugins > payment providers
- enable manual payment
- go to settings > payment
- go to manual payment settings
- enable payment method, fill form and save
- go to dashboard > "in private test mode"
- disable test mode and go live

3. Create question
- go to products > quesstions
- create a new question
- set question "1", type "Number", regular ticket and save

'''



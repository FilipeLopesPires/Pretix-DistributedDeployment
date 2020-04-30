'''

Title: Pretix Quickstart (w/ API Key Generation)

Description: 
Python script that uses Selenium to create an organization inside Pretix, generates a secret API key for sending REST requests and stores it in a plaintext file. 
The script also creates a default event and prepares it for load testing with Locust.

Note: The script assumes that you have already deployed Pretix (using docker-compose).

Authors: Filipe Pires (85122) and João Alegria (85048)

'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# Change these variables if you wish to personalize the script
admin_email = "admin@localhost"
admin_pwd = "admin"
host_address = "http://10.2.0.1:7200"
shortWaitTime = 5
longWaitTime = 10
organizer_name = "ws"
token_name = "t1"
event_name = "ws2020"
start_date = "2020-04-23"
end_date = "2020-07-31"
max_capacity = "" # if empty => infinite
manual_payment = "mp"
question = "1"
question_type = "Number"

# Open Firefox, navigate to Pretix and enter into the login page
browser = webdriver.Firefox()
browser.get(host_address)
head_over_here = browser.find_element_by_link_text("head over here")
head_over_here.click()
wait = WebDriverWait( browser, shortWaitTime )
assert browser.find_element_by_id("id_email")

# Login as an administrator
email = browser.find_element_by_id("id_email")
password = browser.find_element_by_id("id_password")
submit = browser.find_element_by_xpath("//button[contains(text(),'Log in')]")
email.send_keys(admin_email)
password.send_keys(admin_pwd)
submit.click()
wait = WebDriverWait( browser, longWaitTime )
page_title = browser.title
assert page_title == "Dashboard pretix.de"

# Create Organizer
admin = browser.find_element_by_id("button-sudo")
admin.click()
wait = WebDriverWait( browser, shortWaitTime )

organizers = browser.find_element_by_link_text("Organizers")
organizers.click()
wait = WebDriverWait( browser, shortWaitTime )

create_organizer = browser.find_element_by_link_text("Create a new organizer")
create_organizer.click()
wait = WebDriverWait( browser, shortWaitTime )

org_name = browser.find_element_by_id("id_name")
org_name.send_keys(organizer_name)
org_short = browser.find_element_by_id("id_slug")
org_short.send_keys(organizer_name)
save = browser.find_element_by_xpath("//button[contains(text(),'Save')]")
save.click()
wait = WebDriverWait( browser, longWaitTime )
assert browser.find_element_by_xpath("//div[contains(text(),'The new organizer has been created.')]")

# Create API Token
teams = browser.find_element_by_link_text("Teams")
teams.click()
wait = WebDriverWait( browser, shortWaitTime )
administrators = browser.find_element_by_link_text("Administrators")
administrators.click()
wait = WebDriverWait( browser, shortWaitTime )

tok_name = browser.find_element_by_id("id_name")
tok_name.send_keys(token_name)
add = browser.find_elements_by_xpath("//button[@class='btn btn-primary btn-sm btn-block']")
add[1].click()
wait = WebDriverWait( browser, shortWaitTime )

success_msg = browser.find_element_by_xpath("//div[@class='alert alert-success']").text
success_words = success_msg.split(" ")
token = ""
for i in range(0,len(success_words)):
    if len(success_words[i])>10:
        token = success_words[i].split("\n")[0]
        print(token)
assert len(token) > 0

# Write API Token to .txt File
file = open("token.txt","w")
file.write(token)
file.close()

# Create Event
events = browser.find_element_by_link_text("Events")
events.click()
wait = WebDriverWait( browser, shortWaitTime )
create = browser.find_element_by_link_text("Create a new event")
create.click()
wait = WebDriverWait( browser, shortWaitTime )

language = browser.find_element_by_id("id_foundation-locales_0") 
language.click()
cont = browser.find_element_by_xpath("//button[contains(text(),'Continue')]")
cont.click()
wait = WebDriverWait( browser, longWaitTime )
assert browser.find_element_by_xpath("//small[contains(text(),'Step 2')]") 

evt_name = browser.find_element_by_id("id_basics-name_0")
evt_name.send_keys(event_name)
short_name = browser.find_element_by_id("id_basics-slug")
short_name.send_keys(event_name)
strt_date = browser.find_element_by_id("id_basics-date_from_0")
strt_date.send_keys(start_date)
nd_date = browser.find_element_by_id("id_basics-date_to_0")
nd_date.send_keys(end_date)
cont = browser.find_element_by_xpath("//button[contains(text(),'Continue')]")
cont.click()
wait = WebDriverWait( browser, longWaitTime )
#browser.find_element_by_xpath("//small[contains(text(),'Step 3')]")
#cont = browser.find_element_by_xpath("//button[contains(text(),'Continue')]")
#cont.click()
#wait = WebDriverWait( browser, longWaitTime )
assert browser.find_element_by_xpath("//h2[contains(text(),'Congratulations!')]") 

trash = browser.find_elements_by_xpath("//button[@class='btn btn-danger']")
trash[1].click()
wait = WebDriverWait( browser, shortWaitTime )
capacity = browser.find_element_by_id("id_form-0-quota")
capacity.clear()
if max_capacity != "":
    capacity.send_keys(max_capacity)
save = browser.find_element_by_xpath("//button[contains(text(),'Save')]")
save.click()
wait = WebDriverWait( browser, longWaitTime )
#assert browser.find_element_by_xpath("//div[contains(text(),'Your changes have been saved.')]")

# Activate manual payment
settings = browser.find_element_by_link_text("Settings")
settings.click()
wait = WebDriverWait( browser, shortWaitTime )
plugins = browser.find_element_by_link_text("Plugins")
plugins.click()
wait = WebDriverWait( browser, shortWaitTime )
payment_providers = browser.find_element_by_link_text("Payment providers")
payment_providers.click()
wait = WebDriverWait( browser, shortWaitTime )
man_payment = browser.find_element_by_name("plugin:pretix.plugins.manualpayment")
man_payment.click()
wait = WebDriverWait( browser, longWaitTime )
#assert browser.find_element_by_xpath("//div[contains(text(),'Your changes have been saved.')]")

settings = browser.find_element_by_link_text("Settings")
settings.click()
wait = WebDriverWait( browser, shortWaitTime )
payment = browser.find_element_by_link_text("Payment")
payment.click()
wait = WebDriverWait( browser, shortWaitTime )
settings = browser.find_elements_by_xpath("//a[@class='btn btn-default']")
settings[1].click()
wait = WebDriverWait( browser, shortWaitTime )

enable = browser.find_element_by_id("id_payment_manual__enabled") 
enable.click()
payment_method_name = browser.find_element_by_id("id_payment_manual_public_name_0")
payment_method_description = browser.find_element_by_id("id_payment_manual_checkout_description_0")
payment_method_instructions = browser.find_element_by_id("id_payment_manual_email_instructions_0")
payment_method_pending = browser.find_element_by_id("id_payment_manual_pending_description_0")
payment_method_name.send_keys(manual_payment)
payment_method_description.send_keys(manual_payment)
payment_method_instructions.send_keys(manual_payment)
payment_method_pending.send_keys(manual_payment)
save = browser.find_element_by_xpath("//button[contains(text(),'Save')]")
save.click()
wait = WebDriverWait( browser, longWaitTime )
#assert browser.find_element_by_xpath("//div[contains(text(),'Your changes have been saved.')]")

# Go live with event
dashboard = browser.find_element_by_link_text("Dashboard")
dashboard.click()
wait = WebDriverWait( browser, shortWaitTime )
in_private_test_mode = browser.find_element_by_xpath("//div[@class='shopstate']")   
in_private_test_mode.click()
disable_test_mode = browser.find_element_by_xpath("//button[contains(text(),'Disable test mode')]")
disable_test_mode.click()
wait = WebDriverWait( browser, shortWaitTime )
#assert browser.find_element_by_xpath("//div[contains(text(),'disabled test mode for you.')]")
go_live = browser.find_element_by_xpath("//button[contains(text(),'Go live')]") 
go_live.click()
wait = WebDriverWait( browser, longWaitTime )
#assert browser.find_element_by_xpath("//div[contains(text(),'Your shop is live now!')]")  

# Create question (for locust load testing)
products = browser.find_element_by_link_text("Products")
products.click()
wait = WebDriverWait( browser, shortWaitTime )
questions = browser.find_element_by_link_text("Questions")
questions.click()
wait = WebDriverWait( browser, shortWaitTime )
create_question = browser.find_element_by_xpath("//a[@class='btn btn-primary btn-lg']")
create_question.click()
wait = WebDriverWait( browser, shortWaitTime )

question_name = browser.find_element_by_id("id_question_0")
question_name.send_keys(question)
q_type = browser.find_element_by_xpath("//select[@name='type']/option[text()='" + question_type + "']")
q_type.click()
regular_ticket = browser.find_element_by_id("id_items_0") 
regular_ticket.click()
save = browser.find_element_by_xpath("//button[contains(text(),'Save')]")
save.click()
wait = WebDriverWait( browser, longWaitTime )
#assert browser.find_element_by_xpath("//div[contains(text(),'The new question has been created.')]")  

browser.quit()

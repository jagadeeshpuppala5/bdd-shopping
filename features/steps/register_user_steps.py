from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from features.pages.homepage import HomePage

# Step to launch the browser
@given('I launch the browser')
def launch_browser(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()

# Step to navigate to the URL
@given('I navigate to the URL "{url}"')
def navigate_to_url(context, url):
    context.driver.get(url)

# Step to verify the home page title
@then('the home page should be visible successfully')
def verify_homepage(context):
    assert "Automation Exercise" in context.driver.title

@when('I click on the "Signup / Login" button')
def click_signup_button(context):
    signup_button = context.driver.find_element(By.LINK_TEXT, "Signup / Login")
    signup_button.click()


@then('\"New User Signup!\" should be visible')
def verify_new_user_signup_visible(context):
    new_user_signup_text = context.driver.find_element(By.XPATH,'//h2[text()="New User Signup!"]')
    assert new_user_signup_text.is_displayed()
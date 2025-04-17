from behave import given, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from features.pages.homepage import HomePage

@given('I launch the browser and open the website')
def step_open_homepage(context):
    service = Service(ChromeDriverManager().install())  # 🔧 Correct way to pass driver path
    context.driver = webdriver.Chrome(service=service)  # ✅ Proper usage with Service object
    context.driver.maximize_window()
    context.driver.get('https://www.automationexercise.com/')
    context.homepage = HomePage(context.driver)

@then('the title should be "Automation Exercise"')
def step_verify_title(context):
    title = context.homepage.get_title()
    assert "Automation Exercise" in title
    context.driver.quit()

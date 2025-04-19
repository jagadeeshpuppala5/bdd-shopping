Feature: User Registration

  Scenario: Register a new user on the website
    Given I launch the browser
    And I navigate to the URL "http://automationexercise.com"
    Then the home page should be visible successfully
    When I click on the "Signup / Login" button
    Then "New User Signup!" should be visible
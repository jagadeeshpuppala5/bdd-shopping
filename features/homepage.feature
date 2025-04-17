Feature: Homepage

  Scenario: Verify the homepage title
    Given I launch the browser and open the website
    Then the title should be "Automation Exercise"

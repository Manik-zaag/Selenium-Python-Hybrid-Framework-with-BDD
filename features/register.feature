Feature: Register Account functionality

  Background:
    Given I got navigated to Home page
    And I navigate to Register page

  @fullscreenshot
  Scenario: Register with mandatory fields
    When I enter below details into mandatory fields
      |first_name |last_name |telephone |password |
      |Manik      |Hossain   |12345678  |123456   |
    And I select Privacy Policy option
    And I click on continue button
    Then Account should get created

  Scenario: Register with all fields
    When I enter below details into all fields
      |first_name |last_name |telephone |password |
      |Manik      |Hossain   |12345678  |123456   |
    And I select Privacy Policy option
    And I click on continue button
    Then Account should get created

  Scenario: Register with duplicate email address
    When I enter details into all fields except email field
      |first_name |last_name |telephone |password |
      |Manik      |Hossain   |12345678  |123456   |
    And I enter existing accounts email say "kinam@gmail.com" into email field
    And I select Privacy Policy option
    And I click on continue button
    Then Proper warning message information about duplicate account should be displayed

  Scenario: Register without providing any details
    When I don't enter anything into the fields
    And I click on continue button
    Then Proper warning message for every mandatory fields should be displayed


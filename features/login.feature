Feature: Login Functionality

  Background:
    Given I navigated to Login page

  Scenario Outline: Login with valid credentials
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      | email                         | password    |
      | amotoorisampleone@gmail.com   | secondone   |
      | amotoorisampletwo@gmail.com   | secondtwo   |
      | amotoorisamplethree@gmail.com | secondthree |
      | kinam@gmail.com               | 123456      |

  Scenario Outline: : Login with invalid email and valid password
    When I enter invalid email address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message
    Examples:
      | email          |password  |
      | @gmail.com     |123456    |
      | x@gmail.com    |123456    |
      | kinam@gm.com   |123456    |


  Scenario Outline: Login with valid email and invalid password
    When I enter valid email address as "<email>" and invalid password as "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message
    Examples:
      | email                         | password |
      | amotoorisampleone@gmail.com   | 12345678 |
      | amotoorisampletwo@gmail.com   | 12345678 |
      | amotoorisamplethree@gmail.com | 12345678 |
      | kinam@gmail.com               | 12345678 |

  Scenario Outline: Login with invalid credentials
    When I enter invalid email address as "<email>" and invalid password as "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message
    Examples:
      | email                       | password |
      | amotsampleone@gmail.com     | 12345678 |
      | amotoorisamo@gmail.com      | 12345678 |
      | amotoorisamplethree@gil.com | 12345678 |
      | kinamgmail.com              | 12345678 |

  Scenario: Login without entering any credentials
    When I do not enter anything into email address and password fields
    And I click on Login button
    Then I should get a proper warning message
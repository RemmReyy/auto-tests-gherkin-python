Feature: To do list functionality
  As a user
  I want to manage my tasks in a to-do list
  So that I can organize my work effectively

  Scenario: Successful task creation and adding it to the list
    Given I want to create a task with the following details:
      | title         | description                       | deadline    | priority |
      | Make homework | You need make your python homework| 20.02.2025  | Medium   |
    When I add the task "Make homework" to the list
    Then the task should be successfully created
    And the task should appear in my to-do list
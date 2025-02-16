Feature: To do list functionality
  As a user
  I want to manage my tasks in a to-do list
  So that I can organize my work effectively

  Scenario: Successful task creation and adding it to the list
    Given I want to create a tasks with the following details:
      | title             | description                       | deadline    | priority |
      | Make homework     | You need make your python homework| 20.02.2025  | Medium   |
      | Buy some products | Buy milk, cheese and beef         | 17.02.2025  | Low      |
      | Call mom          | Call mom and wish happy birthday  | 18.02.2025  | High     |

    When I add the tasks "Make homework", "Buy some products" and "Call mom" to the list
    Then the tasks should be successfully created
    And the tasks should appear in my to-do list

  Scenario: Preventing duplicate task creation
    Given I have a task "Make homework" in my list
    When I try to add another task with title "Make homework"
    Then I should see an error about duplicate task

  Scenario: Marking task as completed
    Given I have a task "Call mom" in my list
    When I change task Call mom status to completed
    Then the task Call mom should be marked as completed

  Scenario: Showing completed tasks
    Given I have my list with some completed tasks
    When I call function show completed tasks
    Then the completed tasks should include tasks with status complete
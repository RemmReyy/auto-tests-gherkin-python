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

  Scenario: Showing active tasks
    Given I have my list with completed and active tasks
    When I call function show active tasks
    Then the active tasks list should include tasks with status active

  Scenario: Deleting a task from the list
    Given I have the following tasks in my list:
      | title             | description                       | deadline    | priority |
      | Make homework     | You need make your python homework| 20.02.2025  | Medium   |
      | Buy some products | Buy milk, cheese and beef         | 17.02.2025  | Low      |
    When I delete the task "Make homework"
    Then the task should be removed from the list

  Scenario: Sorting tasks by priority
    Given I have the following tasks already in my list:
      | title           | description          | deadline    | priority |
      | Make homework   | Python homework      | 20.02.2025  | Medium   |
      | Buy groceries   | Milk, eggs, bread    | 17.02.2025  | High     |
      | Clean room      | Vacuum and dusting   | 18.02.2025  | Low      |
    When I sort tasks by priority
    Then tasks should be ordered with highest priority first
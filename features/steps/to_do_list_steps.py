from behave import given, when, then
from to_do_list import Task, ToDoList


@given('I want to create a tasks with the following details')
def prepare_tasks_data(context):
    context.task_data = {}
    for row in context.table:
        context.task_data[row['title']] = {
            'description': row['description'],
            'deadline': row['deadline'],
            'priority': row['priority']
        }

    context.todo_list = ToDoList()

@when('I add the tasks "{task1}", "{task2}" and "{task3}" to the list')
def add_multiple_tasks(context, task1, task2, task3):
    try:
        for task_title in [task1, task2, task3]:
            task_info = context.task_data[task_title]
            context.todo_list.add_task(
                task_title=task_title,
                task_text=task_info['description'],
                deadline=task_info['deadline'],
                priority=task_info['priority']
            )
        context.tasks_added = True
    except Exception as e:
        context.tasks_added = False
        context.error = str(e)

@then('the tasks should be successfully created')
def verify_tasks_creation(context):
    assert context.tasks_added, "Tasks were not created successfully"
    assert len(context.todo_list.task_list) == 3, "Not all tasks were added"

@then('the tasks should appear in my to-do list')
def verify_tasks_in_list(context):
    expected_tasks = {
        "Make homework": {
            "description": "You need make your python homework",
            "deadline": "20.02.2025",
            "priority": "Medium"
        },
        "Buy some products": {
            "description": "Buy milk, cheese and beef",
            "deadline": "17.02.2025",
            "priority": "Low"
        },
        "Call mom": {
            "description": "Call mom and wish happy birthday",
            "deadline": "18.02.2025",
            "priority": "High"
        }
    }

    found_tasks = {task: False for task in expected_tasks}

    for task in context.todo_list.task_list:
        if task.task_title in expected_tasks:
            found_tasks[task.task_title] = True
            expected = expected_tasks[task.task_title]
            assert task.task_text == expected["description"], f"Wrong description for {task.task_title}"
            assert task.deadline == expected["deadline"], f"Wrong deadline for {task.task_title}"
            assert task.priority == expected["priority"], f"Wrong priority for {task.task_title}"

    for task_title, found in found_tasks.items():
        assert found, f"Task '{task_title}' was not found in the list"


@given('I have a task "{task_title}" in my list')
def create_single_task(context, task_title):
    context.todo_list = ToDoList()
    context.todo_list.add_task(task_title, "Test description", "20.02.2025", "Medium")

@when('I try to add another task with title "{task_title}"')
def try_add_duplicate(context,task_title):
    try:
        context.todo_list.add_task(task_title,"Test description", "20.02.2025", "Medium")
        context.duplicate_added = True
    except ValueError as e:
        context.error_message = str(e)
        context.duplicate_added = False

    @then('I should see an error about duplicate task')
    def verify_duplicate_error(context):
        assert context.error_message == f"The task '{task_title}' already exist!", "Duplicate task error message incorrect"



@when('I change task {task_title} status to completed')
def change_task_status(context,task_title):
    context.todo_list.change_status(task_title,True)

@then('the task {task_title} should be marked as completed')
def verify_task_status(context, task_title):
    for task in context.todo_list.task_list:
        if task.task_title == task_title:
            assert task.status == True, "Task status was not changed to completed"


@given('I have my list with some completed tasks')
def initialize_completed_tasks(context):
    context.todo_list = ToDoList()
    context.todo_list.add_task("Make homework", "You need to do your python homework", "20.02.2025", "Medium")
    context.todo_list.add_task("Call mom", "Call mom and wish happy birthday", "18.02.2025", "High")
    context.todo_list.change_status("Make homework", True)
    context.todo_list.change_status("Call mom", True)

@when('I call function show completed tasks')
def retrieve_completed_tasks(context):
    context.completed_tasks = context.todo_list.show_completed_tasks()

@then('the completed tasks should include tasks with status complete')
def verify_completed_tasks(context):
    assert all(task.status for task in context.completed_tasks), "Not all tasks are marked as completed"

@given('I have my list with completed and active tasks')
def add_active_task(context):
    context.todo_list = ToDoList()
    context.todo_list.add_task("Buy some products", "Buy milk, cheese and beef", "17.02.2025", "Low")
    context.todo_list.add_task("Make homework", "You need to do your python homework", "20.02.2025", "Medium")
    context.todo_list.add_task("Call mom", "Call mom and wish happy birthday", "18.02.2025", "High")
    context.todo_list.add_task("Write tests", "Write tests for main functions of your project", "25.02.2025", "High")
    context.todo_list.change_status("Make homework", True)
    context.todo_list.change_status("Call mom", True)


@when('I call function show active tasks')
def retrieve_active_tasks(context):
    context.active_tasks = context.todo_list.show_active_tasks()

@then('the active tasks list should include tasks with status active')
def verify_active_tasks(context):
    assert all(not task.status for task in context.active_tasks), "Not all tasks are marked as active"


@given('I have the following tasks in my list')
def setup_tasks_in_list(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(
            task_title=row['title'],
            task_text=row['description'],
            deadline=row['deadline'],
            priority=row['priority']
        )

@when('I delete the task "{task_title}"')
def delete_task(context, task_title):
    context.todo_list.delete_task(task_title)

@then('the {task_title} should be removed from the list')
def verify_task_deleted(context, task_title):
    for task in context.todo_list.task_list:
        assert all(task.task_title != task_title for task in context.todo_list.task_list), f"Task '{task_title}' was not deleted"


@given('I have the following tasks already in my list')
def setup_tasks_in_unsorted_list(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(
            task_title=row['title'],
            task_text=row['description'],
            deadline=row['deadline'],
            priority=row['priority']
        )

@when('I sort tasks by priority')
def step_sort_by_priority(context):
    context.todo_list.task_list = context.todo_list.sort_by_priority()

@then('tasks should be ordered with highest priority first')
def check_sorted_list_by_priority(context):
       for task in context.todo_list.task_list:
           assert context.todo_list.task_list[0].priority == "High" and context.todo_list.task_list[1].priority == "Medium", "Tasks are not sorted correctly"


@given('I have a tasks  in my list')
def setup_tasks_in_new_list(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(
            task_title=row['title'],
            task_text=row['description'],
            deadline=row['deadline'],
            priority=row['priority']
        )

@when('I edit the task "{task_title}" changing description to "{new_description}"')
def step_edit_task(context, task_title, new_description):
    context.todo_list.edit_the_task(task_title,new_description)

@then('the task "{task_title}" should have the updated description "{new_description}"')
def check_new_description(context, task_title, new_description):
    for task in context.todo_list.task_list:
        if task.task_title == task_title:
            assert task.task_text == new_description, "Failed to edit task description"


@given("I create the following tasks in my list")
def create_tasks_in_new_list(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(
            task_title=row['title'],
            task_text=row['description'],
            deadline=row['deadline'],
            priority=row['priority']
        )

@when("I whant to clear my to-do list")
def clear_to_do_list(context):
    context.todo_list.delete_all_tasks()

@then("my to-do list should be empty")
def check_list_after_clearing(context):
    assert len(context.todo_list.task_list) == 0, "The list did not delete all tasks"


@given('I create a task with title "{title}", description "{description}", deadline "{deadline}", priority "{priority}"')
def add_invalid_priority_task(context, title, description, deadline, priority):
    context.todo_list = ToDoList()
    try:
        context.todo_list.add_task(title, description, deadline, priority)
        context.error_message = None
    except ValueError as e:
        context.error_message = str(e)

@then('I should see an error message')
def step_error(context):
    assert context.error_message is not None, "Expected an error message, but none was raised."



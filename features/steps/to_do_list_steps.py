from behave import given, when, then
from to_do_list import Task, ToDoList

@given('I want to create a task with the following details')
def get_data(context):
    context.task_data = {}
    for row in context.table:
        context.task_data[row['title']] = {
            'description': row['description'],
            'deadline': row['deadline'],
            'priority': row['priority']
        }

    context.todo_list = ToDoList()

@when('I add the task "{task_title}" to the list')
def add_task_to_the_list(context, task_title):
    try:
        task_info = context.task_data[task_title]
        context.todo_list.add_task(
            task_title=task_title,
            task_text=task_info['description'],
            deadline=task_info['deadline'],
            priority=task_info['priority']
        )
        context.task_added = True
    except Exception as e:
        context.task_added = False
        context.error = str(e)

@then('the task should be successfully created')
def step_impl(context):
    assert context.task_added, "Task was not created successfully"

@then('the task should appear in my to-do list')
def availability_check(context):
    found = False
    for task in context.todo_list.task_list:
        if task.task_title == "Make homework":
            found = True
            assert task.task_text == "You need make your python homework"
            assert task.deadline == "20.02.2025"
            assert task.priority == "Medium"
            break
    assert found, "Task was not found in the list"
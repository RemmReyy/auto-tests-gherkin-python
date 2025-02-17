from datetime import datetime, date


class Task:
    def __init__(self, task_title, task_text = "", deadline ="", priority = "", status = False):
        self.task_title = task_title
        self.task_text = task_text
        self.deadline = deadline
        self.priority = priority
        self.status = status

        valid_priorities = {"High", "Medium", "Low"}
        if priority not in valid_priorities:
            raise ValueError(f"Invalid priority! Choose from {valid_priorities}.")
        self.priority = priority

class ToDoList:
    def __init__(self):
        self.task_list = []

    def task_exists(self, task_title):
        return any(task.task_title == task_title for task in self.task_list)

    def add_task(self, task_title, task_text="", deadline="", priority=""):
        if self.task_exists(task_title):
            raise ValueError(f"The task '{task_title}' already exist!")

        new_task = Task(task_title, task_text, deadline, priority)
        self.task_list.append(new_task)

    def delete_task(self, task_title):
        for task in self.task_list:
            if task.task_title == task_title:
                self.task_list.remove(task)
                return
        raise NameError("We don't have this task")

    def change_status(self, task_title, status):
        for task in self.task_list:
            if task.task_title == task_title:
                task.status = status
                return

        raise NameError("We don't have this task")

    def show_completed_tasks(self):
        completed_tasks = [task for task in self.task_list if task.status]
        if completed_tasks:
            return completed_tasks
        else:
            raise ValueError("You don't have completed tasks")


    def show_active_tasks(self):
        active_tasks = [task for task in self.task_list if not task.status]
        if active_tasks:
            return active_tasks
        else: print("Congratulations, you have completed all your tasks!")


    def sort_by_priority(self):
        high_priority = []
        medium_priority = []
        low_priority = []
        for task in self.task_list:
            if task.priority == "High":
                high_priority.append(task)
            elif task.priority == "Medium":
                medium_priority.append(task)
            else: low_priority.append(task)
        return high_priority + medium_priority + low_priority


    def edit_the_task(self,task_title,new_text):
        for task in self.task_list:
            if task.task_title == task_title:
                task.task_text = new_text
                return True
        return False


    def delete_all_tasks(self):
        self.task_list.clear()

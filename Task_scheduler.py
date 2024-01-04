import sys, os
import win32com.client
from datetime import datetime, timedelta

class Task:
    def __init__(self, task_name, executable_path):
        self.task_name = task_name
        self.executable_path = executable_path
        self.triggers = []  # List to store triggers

    def Add_trigger(self, start_hour, start_minute):
        trigger = {
            "type": 2,  # 2 means daily trigger
            "start_boundary": self._calculate_start_boundary(start_hour, start_minute)
        }
        self.triggers.append(trigger)

    def _calculate_start_boundary(self, start_hour, start_minute):
        now = datetime.now()
        start_time = datetime(now.year, now.month, now.day, start_hour, start_minute)
        if start_time < now:
            start_time += timedelta(days=1)  # If the calculated start time is in the past, move to the next day
        return start_time.isoformat()

    def Create_task(self):
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()

        root_folder = scheduler.GetFolder('\\')

        task_def = scheduler.NewTask(0)
        task_def.RegistrationInfo.Description = self.task_name

        # Define the action
        exec_action = task_def.Actions.Create(0)
        exec_action.Path = sys.executable
        exec_action.Arguments = os.path.dirname(__file__) +"\\"+self.executable_path

        # Define the triggers
        for trigger_info in self.triggers:
            trigger = task_def.Triggers.Create(trigger_info["type"])
            trigger.StartBoundary = trigger_info["start_boundary"]

        # Register the task
        root_folder.RegisterTaskDefinition(
            self.task_name,
            task_def,
            6,  # Logon trigger type
            None,  # User and password are None since we set it in task_def
            None,
            3  # Logon type
        )


def Task_exists(task_name):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    task_collection = root_folder.GetTasks(0)

    for task in task_collection:
        if task.Name == task_name:
            return True
    return False



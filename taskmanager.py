import pandas as pd
import datetime

class TaskManager:


    # Example task list:
    # [[taskName, completed=True/False], [taskname2, False]]

    task_list = []
    completed_tasks = []

    def __init__(self):
        self.fd = open("tasks.txt", "a+")
        date_nl = datetime.datetime.now().strftime("%m/%d/%Y, %I:%M") + '\n'
        self.fd.write(date_nl)

    def makeTaskList(self):
        self.task_list = []
        doneTasks = False
        while (doneTasks == False):
            task = input()
            if (task == "Done" or task == "done") and len(self.task_list) == 0:
                print("Please enter at least one task.")
            elif task == "Done" or task == "done":
                doneTasks = True
            elif task == " " or task == "":
                pass
            else:
                self.task_list.append([task, 'incomplete'])

        # Once complete, write the tasks to the output file.
        taskString = "tasks: "
        for x in self.task_list[:-1]:
            taskString += x[0] + ", "
        taskString += self.task_list[-1][0] + '\n'
        self.fd.write(taskString)
        self.fd.close()

    def displayTasks(self):
        if len(self.task_list) > 0:
            print()
            df = pd.DataFrame(self.task_list, columns=["task", "completed"])
            print(df)

    def displayCompletedTasks(self):
        if len(self.completed_tasks) > 0:
            print()
            df = pd.DataFrame(self.completed_tasks, columns=["task", "completed", "time completed"])
            print(df)

    def hasTasks(self):
        return len(self.task_list) > 0

    def finishTask(self, taskName):
        try:
            self.task_list.remove([taskName, 'incomplete'])
            taskTime = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S")
            self.completed_tasks.append([taskName, 'complete', taskTime])
        except:
            print("That task name isn't on the list, try again.")

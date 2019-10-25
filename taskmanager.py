import pandas as pd
import datetime

class TaskManager:


    # Example task list:
    # [[taskName, completed=True/False], [taskname2, False]]

    task_list = []
    completed_tasks = []

    def __init__(self):
        # When task manager inits, open task file and read in tasks.
        # Tasks marked completed go to the completed list, and tasks
        # marked incomplete go to the active task list.
        self.fd = open("tasks.txt", "r+")

        # write date to file, beginning new entry
        self.fd.write("d_"+datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S")+'\n')

        for line in self.fd:
            line = line[:-1]
            words = line.split()
            if words[0][0:2] == "d_":
                pass
            elif words[1] == "completed":
                self.completed_tasks.append([words[0], words[1], words[2]])
            else:
                self.task_list.append([words[0], words[1]])
        self.fd.close()
        self.fd = open("tasks.txt", "w")
        self.fd.write("d_" + datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S") + '\n')



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

    def newTask(self, task):
        self.task_list.append([task, 'incomplete'])

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
            # Remove task from active task list.
            self.task_list.remove([taskName, 'incomplete'])
            taskTime = datetime.datetime.now().strftime("%m/%d/%Y_%I:%M:%S")
            # Add task with completion time to completed task list.
            self.completed_tasks.append([taskName, 'completed', taskTime])
            # Write completed task to file.
            taskString = taskName + " completed " + taskTime + '\n'
            self.fd.write(taskString)
        except:
            print("That task name isn't on the list, try again.")

    def closeFile(self):
        # If tasks were remaining at quit time, write them to the file as incomplete.
        if len(self.task_list) > 0:
            taskString = ""
            for entry in self.task_list:
                taskString = entry[0] + " " + entry[1] + '\n'
                self.fd.write(taskString)
        self.fd.close()
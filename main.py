from taskmanager import TaskManager


# To implement: avg productivity, avg interval time
# - remembering what interval time produced best productivity
# - what intervals produced better productivity, maybe with a dictionary


def main():
  # Creates taskmanager instance and opens file for output, writes date.
  tm = TaskManager()

  # Start program.
  print("Hi! I'm Herupa, your task helper.")
  print("Enter your list of tasks to begin.")
  print("Enter each task at a time. Type Done when you're finished.")
  tm.makeTaskList()
  tm.displayTasks()
  print()

  while(tm.hasTasks()):
      print()
      print("F [task] to finish a task.")
      print("L to see a list of completed tasks.")
      response = input()
      if response[0] == "F" or response[0] == "f":
        cur_task = response[2:]
        tm.finishTask(cur_task)
        print("You've earned 10XP!")
        tm.displayTasks()
      else:
        tm.displayCompletedTasks()

  print()
  print("You've finished every task and earned 50XP!")
  tm.displayCompletedTasks()



main()

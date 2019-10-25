from taskmanager import TaskManager


# To implement: avg productivity, avg interval time
# - remembering what interval time produced best productivity
# - what intervals produced better productivity, maybe with a dictionary


def main():
  # Creates taskmanager instance and opens file for output.
  tm = TaskManager()

  # Start program.
  # Imports task list from file & displays it.
  print("Hi! I'm Herupa, your task helper.")
  tm.displayTasks()
  print()

  # If we have no tasks, create a list.
  if not tm.hasTasks():
    tm.makeTaskList()
    tm.displayTasks()

  # While we have tasks, let the user enter a task, finish a task, or view completed tasks.
  while(tm.hasTasks()):
      print()
      print("E [task] to enter new task.")
      print("F [task] to finish a task.")
      print("L to see a list of completed tasks.")
      print("Q to quit.")
      response = input()
      if response[0] == "F" or response[0] == "f":
        cur_task = response[2:]
        tm.finishTask(cur_task)
        tm.displayTasks()
      elif response[0] == "e" or response[0] == "e":
        cur_task = response[2:]
        tm.newTask(cur_task)
        tm.displayTasks()
      elif response[0] == "q" or response[0] == "Q":
          break
      elif response[0] == 'l' or response[0] == "L":
        tm.displayCompletedTasks()
      else:
        print("Not a valid command.")

  print()
  tm.displayCompletedTasks()
  tm.closeFile()



main()

todo_list = []

class task():
 def __init__(self, content, due):
  self.content = content
  self.due = due

def add(content, due):
 t = task(content, due)
 todo_list.append(t)
 print("task added")

def delete(index):
 try:
  if int(index) <= len(todo_list):
   todo_list.remove(todo_list[int(index) -1])
   print("task deleted")
  else:
   print("delete failed!")
 except:
  print("invalid input")

def view_tasks():
 if todo_list == []:
  print("No tasks to be done")
 else:
  for i, task in enumerate(todo_list, 1):
   print(f"{i}. {task.content}, due at {task.due}")

while True:
 user_input = input("what action do you want to perform? (add,delete,view,quit)? ").lower()
 if user_input == "add":
  content = input("what do you want to add? ")
  due = input("when is the task due? ")
  add(content, due)
 elif user_input == "delete":
  to_delete = input("which task do you wish to delete? ")
  delete(to_delete)
 elif user_input == "view":
  view_tasks()
 elif user_input == "quit":
  break
 else:
  print("invalid action!! ")
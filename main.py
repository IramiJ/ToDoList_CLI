todo_list = []

def add(task):
 todo_list.append(task)
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
   print(f"{i}. {task}")

while True:
 user_input = input("what action do you want to perform? (add,delete,view,quit)? ").lower()
 if user_input == "add":
  to_push = input("what do you want to add? ")
  add(to_push)
 elif user_input == "delete":
  to_delete = input("which task do you wish to delete? ")
  delete(to_delete)
 elif user_input == "view":
  view_tasks()
 elif user_input == "quit":
  break
 else:
  print("invalid action!! ")
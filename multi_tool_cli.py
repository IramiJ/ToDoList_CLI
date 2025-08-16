from todo_list import run_todo
from calculator import run_calculator
from file_organizer import run_file_organizer

while True:
 print("\n=== Multi-Tool CLI ===")
 print("1. To-do List")
 print("2. File Organizer")
 print("3. Calculator")
 print("4. Quit")

 inp = input("choose an option: ")
 if inp == "1":
  run_todo()
 elif inp == "2":
  run_file_organizer()
 elif inp == "3":
  run_calculator()
 elif inp == "4":
  break
 else: 
  print("invalid option! please try again")
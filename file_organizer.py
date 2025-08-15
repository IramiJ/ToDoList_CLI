import os, shutil
while True: 
 dir = input("please enter your directory, so that i may be able to sort the files by type").strip()
 if os.path.exists(dir) == True:
  print(os.listdir(dir))
  question = input("should i sort the folder by file types? (y/n) ").lower().strip()
  if question == "y":
   os.makedirs(os.path.join(dir, "Texts"), exist_ok=True)
   os.makedirs(os.path.join(dir, "Images"), exist_ok=True)
   os.makedirs(os.path.join(dir, "PDFs"), exist_ok=True)
   os.makedirs(os.path.join(dir, "Others"), exist_ok=True)

   files = os.listdir(dir)

   for file in files:
    file_path = os.path.join(dir, file)
    if os.path.isfile(file_path):
     ext = file.split(".")[-1].lower()
     if ext == "txt":
      shutil.move(file_path, os.path.join(dir, "Texts"))
     elif ext in ["png","jpg","jpeg"]:
      shutil.move(file_path, os.path.join(dir, "Images"))
     elif ext == "pdf":
      shutil.move(file_path, os.path.join(dir, "PDFs"))
     else:
      shutil.move(file_path, os.path.join(dir, "Others"))
   break
 else:
  print("This directory does not exist. Please try again")
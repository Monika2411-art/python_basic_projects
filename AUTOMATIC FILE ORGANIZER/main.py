import os

#ASKING USER TO ENTER SOURCE FILE
source_file = input("Enter the path of source folder:   ").strip()
if not os.path.exists(source_file):

#PRINT THIS MESSAGE IF THE SOURCE FILE DOES NOT EXISTS AND CLOSE THE FILE
	print("Source folder does not exist")
	exit()
#IF SOURCE FILE EXISTS THEN 
print("Source folder found")

#PRINT FOLDER/FILES OF THE SOURCE PATH AND TREAT THEM AS SINGLE SEPARATE FILE
for items in os.listdir(source_file):
	file_path = os.path.join(source_file,items)
	

	#IF THE FILE IS READY WITH NAME PRINT THEM 
	#if os.path.isfile(file_path):
	#	print(items)

	
	#SEPARATE FILE NAMES AND EXTENSION
	if os.path.isfile(file_path):
		name,extension = os.path.splitext(items)
		print(f"File = {items},  extension:= {extension}")
		#print(f"File = {names},  extension:= {extension}")

		if extension == "":
			continue
		folder_name = (extension[1:].upper() +"_FILES ").strip()
		folder_path = os.path.join(source_file,folder_name)

		if not os.path.exists(folder_path):
			os.mkdir(folder_path)
			print(f"folder created = {folder_name}")

		#MOVE FILES
		import shutil
		destination_path = os.path.join(folder_path,items)
		shutil.move(file_path,destination_path)
		print(f"Moved: {items} -> (folder_name)")
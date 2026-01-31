#Problem Statement

#Create a Python program that:

#1️⃣ Asks the user to enter a folder path
#2️⃣ Scans that folder
#3️⃣ Counts how many files are there for each extension
#4️⃣ Prints the result in a clean way

import os

source_path = input("Enter folder path: ").strip()
if not os.path.exists(source_path):
	print("source path doesn't exists")
	exit()
print("Folder path found")

#TO SIMPLY PRINT FILES
#for filename in os.listdir(source_path):
#	print(filename)
	#if os.path.isfile(filename):
	#	name, extension = os.path.splittext(filename)
	#	print(f"Files = {names}, extension={extension}")



#PRINTS WHOLE PATH
for item in os.listdir(source_path):
	file_path = os.path.join(source_path,item)
	print(file_path)

	extension_counter={
		"txt" = input
	if os.path.isfile(file_path):
		
		name , extension = os.path.splitext(item)
		print(f"Files = {name}, extension = {extension}")
		if extension == "":
			continue
		if os.path.exists(extension):
			counter  +=  extension
		else:
			extension +=  extension
		print(f"{counter} of extension{name} ")
	
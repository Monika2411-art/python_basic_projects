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

extension_counter = {}
for item in os.listdir(source_path):
	file_path = os.path.join(source_path,item)

	if os.path.isfile(file_path):
		name , extension = os.path.splitext(item)
	#	print(f"Files = {name}, extension = {extension}")

		if extension == "":
			continue

		if extension in extension_counter:
			extension_counter[extension] += 1
		else:
			extension_counter[extension] = 1

for ext, count in extension_counter.items():
	print(f"{ext.upper()}  -- files :{count}")
	
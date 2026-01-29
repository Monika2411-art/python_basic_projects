import os
for folder,subFolder,filenames in os.walk("walk_test"):
	for filename in filenames:
		if filename.endswith(".txt"):
			file_path = os.path.join(folder,filename)
			print(file_path)
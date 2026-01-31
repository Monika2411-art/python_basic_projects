import os
source_file = input("Enter source file: ").strip()
if not os.path.exists(source_file):
	print("source file does not found")
	exit()
print("Source file founded")
total_size = 0
for files in os.listdir(source_file):
	file_path = os.path.join(source_file,files)
	print(f"{file_path}")
	
	if os.path.isfile(file_path):

		fileSize = os.path.getsize(file_path)	
		total_size += fileSize
		print(f"File: {files}  Size: {fileSize / 1024:.2f} KB")

print(f"\nTotal folder size: {total_size / 1024:.2f} KB")
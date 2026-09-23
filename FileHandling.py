# file=open("samplefile.txt","x")
# file=open("samplefile.txt","r+")
# open("samplefile.txt","w").write("Heyy Its a New File!")
# print(file.read())


# newfile=open("newfile.txt","x")
# with open("newfile","w"):
#  newfile.write("Yoooooooooooo!")

with open("newfile.txt") as f:
    print(f.read())
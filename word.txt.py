fp=open("word.txt","w")
if fp:
    print("Successfully opened")
    fp.write("i")
    fp.write("a")
    fp.write("")
    fp.close()
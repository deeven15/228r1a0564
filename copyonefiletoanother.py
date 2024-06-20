fp1=open("csa1.txt","r")
fp2=open("csea12.txt","w+")
if fp1:
    print("open successfully")
    for i in fp1:
        fp2.write(i)
        print("file is copied successfully")
        fp2.seek(0,0)
        content=fp2.read()
        print(content)
        for i in fp2:
            print(i)

    fp1.close()
    fp2.close()
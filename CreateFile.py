'''
open()
read()
readline()
writeline()
close()
fseek()
tell()
'''

fp=open("csa1.txt","w")
if fp:
    print("file is created successfully")
    fp.writelines("hi student welcome to cmr engineering college\n today smartinterviews class\n today python class is on files\n")

fp.close()
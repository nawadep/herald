try:
    f=open("123.txt","r")
    x=f. read()
    f.close()
except:
    print("Invalid filename")

def extract_temp(line):
    x=y.split()
    for i in x:
        if (i.isdigit()):
            print(i)
        else:
            pass

extract_temp(y)

try:
    f=open("123.txt","r")
    x=f. read()
    y=x.split("")
    print(y)
    list_1=[]
    for i in y:
        list_1.append(i)
    
    while("") in list_1:
        list_1.remove("")
    print(list_1)
    stri=""
    for j in list-1:
        stri=stri+j+""

    print(stri)    
except:
    print("Invalid name")

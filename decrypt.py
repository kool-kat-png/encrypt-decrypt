key={0:" ",1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
while True:    
    try:
        d=input("NUMBERs:").split(" ")
        x=0
        for i in d:
            d[x]=((float(d[x])*152)**(1/2))
            x+=1
        x=0
        eged=[]
        for i in range(0,len(d)):
            eged.append(key[d[x]])
            x+=1
        print(*eged)
    except Exception as e:
        print(e)

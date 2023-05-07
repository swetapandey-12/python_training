a =input()
b =input()
c =input()
if(a!="Monday" and a!="Thursday"):
    print("Invalid Day")
if(b!="CSE" and b!="ECE" and b!="MECH"):
    print("Invalid Dept")
if(c!="A" and c!="B"):
    print("Invalid Group")

if(b=="CSE"):
    if(a=="Monday"):
        if(c=="A"):
            print("Java")
        elif(c=="B"):
            print("C++")
    elif(a=="Thursday"):
        if(c=="A"):
            print("C++")
        elif(c=="B"):
            print("Java")

elif(b=="ECE"):
    if(a=="Monday"):
        if(c=="A"):
            print("C")
        elif(c=="B"):
            print("Python")
    elif(a=="Thursday"):
        if(c=="A"):
            print("Python")
        elif(c=="B"):
            print("C") 
            
elif(b=="MECH"):
    if(a=="Monday"):
        if(c=="A"):
            print("Central Workshop")
        elif(c=="B"):
            print("Machine Design")
    elif(a=="Thursday"):
        if(c=="A"):
            print("Machine Design")
        elif(c=="B"):
            print("Central Workshop")             
            

def upper1(x):
    s=""
    for i in x:
        if ord(i)>96 and ord(i)<123:
            s+=(chr(ord(i)-32))
        else: 
            s+=i
    return s

def lower1(x):
    s=""
    for i in x:
        if ord(i)>64 and ord(i)<91:
            s+=(chr(ord(i)+32))
        else:
            s+=i
    return s

def cap1(x):
    s=""
    if ord(x[0])>96 and ord(x[0])<123:
        s+=chr(ord(x[0])-32)
    else:
        pass
    for i in range(1,len(x)):
        if ord(x[i])>64 and ord(x[i])<91:
            s+=(chr(ord(x[i])+32))
        else:
            s+=x[i]   
    return s

def title1(x):
    a=0;b=0
    l1=[]
    l=x.split()
    print(l)
    for y in l:
        s=""
        for i in range(0,len(y)):
            if ord(y[i])>97 and ord(y[i])<123:
                print("Alphabet found at : ",i)
                a=i
                b=chr(ord(y[i])-32)
                break        
            else:
                 pass        
        
        for i in range(0,len(y)):
            if i==a:
                s+=b
            elif ord(y[i])>64 and ord(y[i])<91:
                s+=(chr(ord(y[i])+32))                 
            else:
                s+=y[i]
                
        l1.append(s)
        print(l1)            
            
    return (" ".join(l1))
    
def isalpha1(x):
    c=0
    for i in x: 
        if (ord(i)>64 and ord(i)<90) or (ord(i)>96 and ord(i)<123):
            c+=1
        else: 
            pass
        
    if c==len(x):           
        return True
    else:
        return False
                     
def isupper1(x):
    c=0
    for i in x: 
        if (ord(i)>64 and ord(i)<90):
            c+=1
        else: 
            pass
        
    if c==len(x):           
        return True
    else:
        return False
                     
def islower1(x):
    c=0
    for i in x: 
        if (ord(i)>96 and ord(i)<123):
            c+=1
        else: 
            pass
        
    if c==len(x):           
        return True
    else:
        return False
                     
def swapcase1(x):
    s=""
    for i in x: 
        if (ord(i)>96 and ord(i)<123):
            s+=chr(ord(i)-32)
        elif (ord(i)>64 and ord(i)<91): 
            s+=chr(ord(i)+32)
        else:
            s+=i
    return s                      
                      
def isdigit1(x):
    c=0
    for i in x: 
        if (ord(i)>47 and ord(i)<58):
            c+=1
        else:
            pass
    if c==len(x):
        return True
    else:
        return False
                      
def isalnum1(x):
    c=0
    for i in x: 
        if (ord(i)>47 and ord(i)<58) or (ord(i)>64 and ord(i)<90) or (ord(i)>96 and ord(i)<123):
            c+=1
        else:
            pass
    if c==len(x):
        return True
    else:
        return False
                      
         
        

def calculator():
    a=input("enter calculation")
    c=0
    m=0
    for i in a:
        if not i.isdigit():
            if i not in ("+","-",'*','/','(',')','.'):
                print ("invalid input")
                return
            else:
                c=1   
        else:
            c=1
    if a[-1] in "+-*/":
        print("invalid input, operant at end")
        return
    if a.count("(")!=a.count(")"):
        print("invalid input, parentheses don't match")
        return
    for i in a:
        if i=='(':
            m+=1
        elif i==')':
            m-=1
        if m<0:
            print("invalid input, parentheses position error")
            return
    
    operants=[]
    values=[]
    def solve():
        b=values.pop()
        a=values.pop()
        op=operants.pop()
        eq=a+op+b
        try:
            r=eval(eq)
        except ZeroDivisionError:
            print("error, division by zerou")
            return False
        values.append(str(r))
    precedence = {'+':1,'-':1,'*':2,'/':2 }
    if c==1:
        pos=0
        while len(a)>pos:
            stri=''
            if a[pos]=='-':
                if pos==0 or a[pos-1] in "+-*/(":
                    stri='-'
                    pos+=1
                else:
                    while operants and operants[-1]!='(' and precedence[operants[-1]]>=precedence[i] :
                        if solve()==False:
                            return
                    operants.append(a[pos])
                    pos+=1
            while pos<len(a) and (a[pos].isdigit() or a[pos]=='.'):
                i=a[pos]
                stri=stri+i
                pos+=1
            if pos<len(a):
                i=a[pos]
            if stri != '':
                if stri[0]=='.' or stri[-1]=='.' or stri.count('.')>1:
                    print("error, invalid number,decimal point error")
                    return
                elif stri=='-':
                    values.append('-1')
                else:
                    values.append(stri)
            if i=="(":
                operants.append(i)
                pos+=1
            elif i in '+*/':
                if pos==0: 
                    print("error, operant at start")
                    return
                elif a[pos-1] in "+-*/(":
                    print("error, two operants in a row")
                    return
                else:
                    while operants and operants[-1]!='(' and precedence[operants[-1]]>=precedence[i] :
                        if solve()==False:
                            return
                    operants.append(i)
                    pos+=1
            c=0
            if i==')':
                while operants and operants[-1]!='(':
                    if solve()==False:
                        return
                    c+=1
                operants.pop()
                if c==0 and operants and operants[-1]=='(':
                    print("error, parentheses position error")
                    return
                pos+=1
        if pos==len(a):
            while operants:
                if solve()==False:
                    return       
    if len(values)==1:
        print(values[0])
    elif len(values)>1:
        for i in range(len(values)-1):
            operants.append('*')
            if solve()==False:
                return
        print(values[0])
    else:
        print("error, invalid input")
        
while True:  
    calculator()


    
                        
    

def calculator():
    a=input("enter calculation")
    c=0
    for i in a:
        if not i.isdigit():
            if i not in ("+","-",'*','/','(',')') or a.count("(")!=a.count(")"):
                print ("invalid input")
                break    
            else:
                c=1
    operants=[]
    values=[]
    def solve():
        b=values.pop()
        a=values.pop()
        op=operants.pop()
        eq=a+op+b
        r=eval(eq)
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
            while pos<len(a) and a[pos].isdigit():
                i=a[pos]
                stri=stri+i
                pos+=1
            if pos<len(a):
                i=a[pos]
            if stri != '':
                values.append(stri)
            if i=="(":
                operants.append(i)
            elif i in '+-*/':
                while operants and operants[-1]!='(' and precedence[operants[-1]]>=precedence[i] :
                    solve()
                operants.append(i)
            elif i==')':
                while operants and operants[-1]!='(':
                    solve()
                operants.pop()
            pos+=1
        while operants:
            solve()

    print(values[0])
    
while True:  
    calculator()


    
                        
    

def code(x,y):
    dic1={'A':'1','B':"2",'C':'3','D':'4','E':'5','F':'6','G':'7','H':'8'}
    dic2={'1':'A','2':"B",'3':'C','4':'D','5':'E','6':'F','7':'G','8':'H'}
    z=''
    if y==1:
        for i in x:
           z+=dic1[i] 
    elif y==2:
        for j in x:
            z+=dic2[j]

    return z
x=input("enter your code/word")
y=int(input("if its a code type 2 if its a word press 1"))
z=code(x,y)
print(z)
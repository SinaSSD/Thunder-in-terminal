x= int(input("please enter the size of thunderbolt:"))
c= int(input("please enter the numbers of thunderbolt:"))

m=[[]]
l=[[],[]]
i= 0
j= 0
jj=0
while j!=x :
    i= 0
    while i!=x :
        m[j].append(' ')
        i+=1
        if i == (x-j) :
                m[j].append('/ /')
    j+=1
    m.append([])
    
while jj!=x :
    i= 0
    while i!=x :
        m[jj+x].append(' ')
        i+=1
        if i == (x-jj) :
                m[jj+x].append('/ /')
    jj+=1
    m.append([])
    
k =range(x)
l[0]= ['/ /']
if x == 1 :
    l[0]= ['/|']
l[1]=['|']
for h in k :
    l[0].append('_')
    l[1].append('_')
l[1].append(' ')
l[1].append('|')

m[0][x]=''
m[1][x-1]='/|'
m[2*x-1]=['  |/']

cn = range(c)
for ii in cn :
    d =range(2*x+1)
    for n in d  :
        k =range(2)
        print(''.join(m[n-1]))
        if n == x :
            for h in k :
                print("".join(l[h]))
    

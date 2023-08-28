
import random
#---------------------------------------------------------
''' Generate Dna_Sequence '''
def random_DNA_Sequence(size):
    letters = 'atgc'
    return ''.join(random.choice(letters) for i in range(size))

size=int(input("Enter number of DNA sequence : "))
query=random_DNA_Sequence(size)

with open("query.txt",'a') as af:
    af.write(query)
#---------------------------------------------------------
''' return charchter to use in following for loop'''
def getchar(i):
    with open("query.txt",'r') as rf:
        return rf.read()[i]
#---------------------------------------------------------
a,g,c,t=[],[],[],[]
for i in range(size):
    ch=getchar(i)
    if ch=='a':
        a.append(i)
    elif ch=='t':
        t.append(i)
    elif ch=='g':
        g.append(i)
    elif ch=='c':
        c.append(i)
print(' all sites of c =',c)
#---------------------------------------------------------
indexing_query={'a':a,'t':t,'g':g,'c':c}
'''print dectionary of bases'''
print(indexing_query)
#---------------------------------------------------------
''' Target pattern '''
finallylist=[]
diff_a,diff_t,diff_g,diff_c=[],[],[],[]
target=input(" Enter Target pat : ")
for i in range (len(target)):
    size_of_value_key=len(indexing_query[target[i]])
    for j in range(size_of_value_key):
        finallylist.append(indexing_query[target[i]][j]-i)
finallyset=set(finallylist)
f_number,f_count=0,0
for i in range(1):
    f_number=finallylist[0]
    f_count=finallylist.count(f_number)
c=iter(finallyset)
for i in range(len(finallyset)):
    current_number_set=next(c)
    test_count=finallylist.count(current_number_set)
    if f_count < test_count :
        f_count=test_count
        f_number=current_number_set
print(f' Number : {f_number}\n count : {f_count} \n Shift : {f_number}')
#---------------------------------------------------------------------
if f_number>=0:
    ps='_'*f_number
    j=0
    cnt=0
    for i in range(f_number,len(target)+f_number):
       if target[j]==getchar(i):
           cnt+=1
           ps+=target[j]
       else:
           ps+='_'
       j+=1
    percent=cnt/len(target)*100
    print(f' similatry string : {ps}\n similatry is : {percent}%')
else:
    ns=''
    j=abs(f_number)
    ns+='_'*j
    cnt=0
    for i in range(0,len(target)+f_number):
       if target[j]==getchar(i):
           cnt+=1
           ns+=target[j]
       j+=1
    percent=cnt/len(target)*100
    print(f' similatry string : {ns}\n similatry is : {percent}%')    
import os
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
''' size of file '''
def get_size_of_file(file):
    return os.stat(file).st_size

print('Size of File = ',get_size_of_file('query.txt'))
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
#---------------------------------------------------------    
''' print all array of bases'''
print(' all sites of a =',a)
print(' all sites of t =',t)
print(' all sites of g =',g)
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
        if target[i]=='a':
            diff_a.append(indexing_query[target[i]][j]-i)
        elif target[i]=='t':
            diff_t.append(indexing_query[target[i]][j]-i)
        elif target[i]=='g':
            diff_g.append(indexing_query[target[i]][j]-i)
        elif target[i]=='c':
            diff_c.append(indexing_query[target[i]][j]-i)
print(' difference a = ',diff_a)
print(' difference t = ',diff_t)
print(' difference g = ',diff_g)
print(' difference c = ',diff_c)
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
'''



print ("welcom")
x=input("enter your name  ")
print("welcom  " + x)
print("=========================")
print("enter numper from 65 to 121")

a=int(input("enter numper1  "))
b=int(input("enter numper2  "))
print("numper in askycood")
print(chr(a))
s=str(input("enter character  "))
print(ord(s))
print("==========================")
import random
print("بيطبع رقم عشوائي من 1 ل 1000")
print(random.randint(1,100))
print("===========================")
d="youssef"
d+=" "
d+="Ashraf"
print (d)
print("السمي")
print("=============================")
input("enter any key to exit")

p1={"name":"jo","age":10,"shcool":"alsadeya banen",
'p2':{"name":"ali","age":20,"shcool":"alzahraa"}}
p3={"name":"hos","age":30,"shcool":"sapteya"}
print(p1)
print("multey dectionary")
x=p3.copy()
print(x)
print("نسخة من dect 3")
x.clear()
print(x)
print("مسحنا النسخة")
#print(p1)
print('=========================================')
#p1.pop("name")
#p1['p2'].pop("name")
print(p1)
c=p1.popitem()
print(c)

print(p1)
print("i love back slash \\")
print("123456789101112\rABCDefg")
print("\x59\x6f\x75\x73\x73\x65\x66")
print(100*"#")
def sca (x):
    return x**2
print(sca(5))
let = "z"
let_two = "p"
c = let_two + let
m = c*5
print(m)
print(100*"#")
print(100*"#")
#sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last=sports[3:5]
print(last)
b = "My, what a lovely day"
x = b.split(',')
print(x)
print(type (x))
original_str = "The quick brown rhino jumped over the extremely lazy fox."
count=0
for i in original_str:
    count+=1
print("tha count of str::",count)
print(100*"#")
print(100*"#") 

import turtle

star = turtle.Turtle() 
  
for i in range(50): 
    star.forward(50) 
    star.right(144) 
      
turtle.done() 

print("#"*100)
print(100*"#")
'''
print("sting function")
a="           youssef          "
b="youssef love python and 2 other  languages"
print(len(a))
print(a.strip())
print(a.rstrip())
print(a.lstrip())
print(b.title())
print(b.capitalize())
x,y,z="1","2","3333" 
print(x,'\n',y,'\n',z)
print(x.zfill(4))
print(y.zfill(4))
print(z.zfill(4))
print(b.split())
print(b.split(" ",3))
print(b.rsplit(" ",3))
e="youssef"
print(e.center(17,"%"))
print(b.count("python",0,50))
t="ALI pIAy FOOtbal"
d="samy sleep Alot"
print(t.swapcase())
print(d.swapcase())
r="i love python"
print(r.startswith("i"))
print(r.endswith("y",0,9))

s="I\tLove\t python"
d="sddsd"
print(d.isalpha())

print(d.isidentifier())
g=" "
print(g.isspace())
print(s.istitle())
print(s.expandtabs(5))
print(s.splitlines())
print(s.rjust(50,"@"))
print('\n')
print(s.ljust(50,"@"))
print(s.find("L",0,10))
print(s.index("L",0,10))
print(s.find("h",0,10))
#print(s.index("h",0,10)) erorr h not fouund

x=["youssef", "Ashraf", "Ftahy"]
print("#".join(x))
print("#"*100)
print("#"*100)
print("sring format old and new")
name="youssef"
age=21
rank=10
print("My Name Is: %s my age is: %d And My Rank Is: %f"% (name,age,rank))
name="ali"
age=30
rank=20
print("My NAme Is: %s And My Age IS:%d And My Rank Is: %f " %(name,age,rank))
print("My NAme Is: %.2s And My Age IS:%d And My Rank Is: %.2f " %(name,age,rank))
print("MY Name Is:{:s} And MY Age Is:{:d} And MY Rank Is:{:f}".format(name, age,rank))
print("MY Name Is:{:.2s} And MY Age Is:{:d} And MY Rank Is:{:.2f}".format(name, age,rank))
x=132425435634
print("my Number:{:d}".format(x))
print("my Number:{:,d}".format(x))
print("my Number:{:_d}".format(x))
x,y,z=10,20,30
print("my items is:{:d},{:d},{:d}".format(x,y,z))
print("my items is:{0:d} {1:d} {2:d}".format(x,y,z))
print("my items is:{1:d} {2:d} {0:d}".format(x,y,z))
print("my items is:{:f},{:f},{:f}".format(x,y,z))
print("my items is:{0:.2f} {1:.2f} {2:.2f}".format(x,y,z))
print("my items is:{1:f} {2:f} {0:f}".format(x,y,z))
a="youssef"
age=10
print("my name {a} and my age{age}")
print(f"my name {a} and my age {age}")
























































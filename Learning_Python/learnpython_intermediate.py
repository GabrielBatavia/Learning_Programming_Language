def get_root(a,b,c):
  r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  r3 = (a + b + c)
  return r1,r2,23

result1, result2, result3 = get_root(a=1,c=-8,b=2)
print('Hasil akar-akarnya adalah', result1, 'atau', result2, 'dan pertambahan nya adalah', result3)

add = lambda x, y : x + y
print("total dari 100 dan 200 adalah:",add(100,200))

list_umur = [34,39,20,18,13,54]
print("Umur yang dewasa: ")
for a in filter(lambda x: x >= 19, list_umur): # filter umur menggunakan fungsi filter
    print(a,end = ' ')
    
print()

a = [1,2,3,4,5,6,7]

a_kuadrat = list(map(lambda x: x **2, a))
print(a_kuadrat)

from functools import reduce
# Returns the sum of two elements
def sumTwo(a,b):
    return a+b

result = reduce(sumTwo, [1, 2, 3, 4, 10, 12])
print(result)


a = [1,2,3,4]
n = reduce(lambda x,y : x + y, a)
print(n)


def decorate(style = 'italic'):
  def italic(s):
    return '<i>' + s + '<i>'
  def bold(s):
    return '<b>' + s + '<b>'
  if style == 'italic':
    return italic
  else:
    return bold
    
dec = decorate()
print(dec('hello'))
dec2 = decorate('bold')
print(dec2('hello'))

def another_func():
  print('hello')
  
def outer_func():
  return another_func()
  
outer_func()



def print_counter():
  global counter
  counter = 200
  print('counter didalam fungsi =',counter) # nilai counter didalam fungsi

counter = 100
print_counter()
counter = 150
print('counter diluar fungsi = ',counter) # nilai counter diluar fungsi


def closure_calc():
  a = 2
  def mult(x):
    return a * x
  return mult
  
c = closure_calc()
print(c(1),c(2),c(3))

def fungsi_luar(x):
    a = 10
    def addition(z):
        return a + z
    return addition(x)
  

#declare class
class Cat: # membuat class Cat
  pass # menggunakan pass statement 

nobi = Cat() # membuat sebuah instance dari Cat
print(nobi)



class Cat: # membuat class Cat
  def meow(self): # fungsi meow didalam class Cat
   print('meowwww') 

nobi = Cat() # membuat sebuah instance dari Cat
nobi.meow() # setelah membuat object dari Cat, kita bisa memanggil method meow 



#inisialisasi konstruktor

class Cat:
  def __init__(self,name,color): # menginisialisasi instance dengan constructor
    self.name = name
    self.color = color

nobi = Cat('nobi','black') # membuat instance dari kelas Cat dengan nama nabi dan warna hitam
nero = Cat('nero','white')

print(nobi.name)
print(nobi.color)
print(nero.name)
print(nero.color)






class Circle:
  def __init__(self,name,radius,PI):
    self.__name = name # instance variable
    self.__radius = radius # instance variable
    self.__PI = PI
  
  # menghitung area sebuah lingkaran dengan pi * r kuadrat
  def area(self):
    return self.__PI * self.__radius ** 2

c1 = Circle("C1",4,3.14)
print("Area dari c1:",c1.area())
c2 = Circle("C2",6,3.141)
print("Area dari c2:",c2.area())
c3 = Circle("C3",6,3.1415)
print("Area dari c3:",c3.area())






class Circle:
  PI = 3.1415
  def __init__(self,name,radius):
    self.__name = name # instance variable
    self.__radius = radius # instance variable
  
  # menghitung area sebuah lingkaran dengan pi * r kuadrat
  # method dari class Circle dan instance akan mengambil value PI dari class variable melalui Circle.PI
  def area(self):
    return Circle.PI * self.__radius ** 2

c1 = Circle("C1",4)
print("Area dari c1:",c1.area())
c2 = Circle("C2",6,)
print("Area dari c2:",c2.area())
c3 = Circle("C3",5)
print("Area dari c3:",c3.area())
# FUNDAMENTOS
# Crear clase
# class TheSimplestClass:
    # pass

# Crear objeto
# my_first_object = TheSimplestClass()


# PILAS
# Procedimental
# stack = []

# def push(val):
#     stack.append(val)

# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val

# push(3)
# push(2)
# push(1)
# print(pop()) # 1
# print(pop()) # 2
# print(pop()) # 3

# Orientado a objetos
# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#     def push(self, val):
#         self.__stack_list.append(val)
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#     def get_sum(self):
#         return self.__sum
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val

# stack_object = AddingStack()
# for i in range(5):
#     stack_object.push(i)
# print(stack_object.get_sum())
# for i in range(5):
#     print(stack_object.pop())



# PROPIEDADES
# Variables de instancia
# class ExampleClass:
#     def __init__(self, val = 1):
#         self.__first = val
#     def set_second(self, val = 2):
#         self.__second = val
        
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.__third = 5
# print(example_object_1.__dict__) # {'_ExampleClass__first': 1}
# print(example_object_2.__dict__) # {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
# print(example_object_3.__dict__) # {'_ExampleClass__first': 4, '__third': 5}

# Variables de clase
# class ExampleClass:
#     varia = 1
#     def __init__(self, val):
#         ExampleClass.varia = val

# print(ExampleClass.__dict__) # {'__module__': '__main__', 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x7f417c0764d0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
# example_object = ExampleClass(2)
# print(ExampleClass.__dict__) # {'__module__': '__main__', 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x7f417c0764d0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
# print(example_object.__dict__) # {}

# # Comprobanco existencia d eatributo
# class ExampleClass:
#     attr = 1

# print(hasattr(ExampleClass, 'attr')) # True
# print(hasattr(ExampleClass, 'prop')) # False


# METODOS
# Invocando un metodo
# Solo con self
# class Classy:
#     def method(self):
#         print("método")

# obj = Classy()
# obj.method() # método

# Con parametros
# class Classy:
#     def method(self, par):
#         print("método:", par)
 
# obj = Classy()
# obj.method(1) # método: 1
# obj.method(2) # método: 2
# obj.method(3) # método: 3


# Uso de self
# Uso 1
# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)
 
 
# obj = Classy()
# obj.var = 3
# obj.method() # 2 3

# uso 2
# class Classy:
#     def other(self):
#         print("otro")
 
#     def method(self):
#         print("método")
#         self.other()
 
 
# obj = Classy()
# obj.method()
# # Salida:
# # método
# # otro

# Constructor
# Simple
# class Classy:
#     def __init__(self, value):
#         self.var = value

# obj_1 = Classy("objeto")
# print(obj_1.var) # objeto

# Con argumentos
# class Classy:
#     def __init__(self, value = None):
#         self.var = value

# obj_1 = Classy("objeto")
# obj_2 = Classy()
# print(obj_1.var) # objeto
# print(obj_2.var) # None

# Oculto
# class Classy:
#     def visible(self):
#         print("visible")
 
#     def __hidden(self):
#         print("oculto")
 
 
# obj = Classy()
# obj.visible()
 
# try:
#     obj.__hidden()
# except:
#     print("fallido")
 
# obj._Classy__hidden()
# # Salida:
# # visible
# # fallido
# # oculto

# Vida interior de clases y objetos
# Dict
# class Classy:
#     varia = 1
#     def __init__(self):
#         self.var = 2
#     def method(self):
#         pass
#     def __hidden(self):
#         pass

# obj = Classy()
# print(obj.__dict__) # {'var': 2}
# print(Classy.__dict__) # {'__module__': '__main__', 'varia': 1, '__init__': <function Classy.__init__ at 0x7fd639df7320>, 'method': <function Classy.method at 0x7fd639df7ef0>, '_Classy__hidden': <function Classy.__hidden at 0x7fd639df7f80>, '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>, '__doc__': None}

# Name
# class Classy:
#     pass
# print(Classy.__name__) # Classy
# obj = Classy()
# print(type(obj).__name__) # Classy

# Type
# class Classy:
#     pass

# print(Classy.__name__) # Classy
# obj = Classy()
# print(type(obj).__name__) # Classy

# Module
# class Classy:
#     pass

# print(Classy.__module__) # __main__
# obj = Classy()
# print(obj.__module__) # __main__

# Bases
# class SuperOne:
#     pass

# class SuperTwo:
#     pass

# class Sub(SuperOne, SuperTwo):
#     pass

# def printBases(cls):
#     print('( ', end='')
#     for x in cls.__bases__:
#         print(x.__name__, end=' ')
#     print(')')

# printBases(SuperOne) # ( object )
# printBases(SuperTwo) # ( object )
# printBases(Sub) # ( SuperOne SuperTwo )


# HERENCIA
# Imprimiendo objetos
# El objeto
# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy


# sun = Star("Sol", "Vía Láctea")
# print(sun) # <__main__.Star object at 0x7f3d20065a10>

# Con str
# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

#     def __str__(self):
#         return self.name + ' en ' + self.galaxy


# sun = Star("Sol", "Vía Láctea")
# print(sun) # Sol en Vía Láctea

# Herencia
# Dos niveles
# class Vehicle:
#     pass
 
 
# class LandVehicle(Vehicle):
#     pass
 
 
# class TrackedVehicle(LandVehicle):
#     pass

# issubclass
# class Vehicle:
#     pass


# class LandVehicle(Vehicle):
#     pass


# class TrackedVehicle(LandVehicle):
#     pass


# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end="\t")
#     print()

# isinstance
# class Vehicle:
#     pass


# class LandVehicle(Vehicle):
#     pass


# class TrackedVehicle(LandVehicle):
#     pass


# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()

# for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
#     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(obj, cls), end="\t")
        
# # Salida:
# # True	False	False	
# # True	True	False	
# # True	True	True	

# is
# class SampleClass:
#     def __init__(self, val):
#         self.val = val


# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val += 1

# print(object_1 is object_2) # False
# print(object_2 is object_3) # False
# print(object_3 is object_1) # True
# print(object_1.val, object_2.val, object_3.val) # 1 2 1

# string_1 = "Mary tenía un "
# string_2 = "Mary tenía un corderito"
# string_1 += "corderito"

# print(string_1 == string_2, string_1 is string_2) # True False

# Encontrando metodos y propiedades
# Super
# class Super:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "Mi nombre es " + self.name + "."


# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)


# obj = Sub("Andy")

# print(obj) # Mi nombre es Andy.

# Super()
# class Super:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "Mi nombre es " + self.name + "."


# class Sub(Super):
#     def __init__(self, name):
#         super().__init__(name)


# obj = Sub("Andy")

# print(obj) # Mi nombre es Andy.

# Variables de clase
# # Probando propiedades: variables de clase.
# class Super:
#     supVar = 1


# class Sub(Super):
#     subVar = 2


# obj = Sub()

# print(obj.subVar) # 2
# print(obj.supVar) # 1

# Variables de instancia
# # Probando propiedades: variables de instancia.
# class Super:
#     def __init__(self):
#         self.supVar = 11


# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12


# obj = Sub()

# print(obj.subVar) # 12
# print(obj.supVar) # 11

# Herencia multiple
# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
 
 
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
 
 
# class Sub(SuperA, SuperB):
#     pass
 
# obj = Sub()
 
# print(obj.var_a, obj.fun_a()) # 10 11
# print(obj.var_b, obj.fun_b()) # 20 21

#Overrideng
# class Level1:
#     var = 100
#     def fun(self):
#         return 101

# class Level2(Level1):
#     var = 200
#     def fun(self):
#         return 201

# class Level3(Level2):
#     pass

# obj = Level3()
# print(obj.var, obj.fun()) # 200 201

# Overriding mas complejo
# class Left:
#     var = "L"
#     var_left = "LL"
#     def fun(self):
#         return "Left"

# class Right:
#     var = "R"
#     var_right = "RR"
#     def fun(self):
#         return "Right"

# class Sub(Left, Right):
#     pass

# obj = Sub()
# print(obj.var, obj.var_left, obj.var_right, obj.fun()) # L LL RR Left

#Como contruir una jerarquia de clases
# import time
# class Tracks:
#     def change_direction(self, left, on):
#         print("pistas: ", left, on)

# class Wheels:
#     def change_direction(self, left, on):
#         print("ruedas: ", left, on)

# class Vehicle:
#     def __init__(self, controller):
#         self.controller = controller
#     def turn(self, left):
#         self.controller.change_direction(left, True)
#         time.sleep(0.25)
#         self.controller.change_direction(left, False)

# wheeled = Vehicle(Wheels())
# tracked = Vehicle(Tracks())
# wheeled.turn(True)
# tracked.turn(False)
# # ruedas:  True True
# # ruedas:  True False
# # pistas:  False True
# # pistas:  False False


# El problema del Diamante
# class Top:
#     def m_top(self):
#         print("top")


# class Middle_Left(Top):
#     def m_middle(self):
#         print("middle_left")


# class Middle_Right(Top):
#     def m_middle(self):
#         print("middle_right")


# class Bottom(Middle_Left, Middle_Right):
# 	def m_bottom(self):
# 		print("bottom")


# object = Bottom()
# object.m_bottom()
# object.m_middle()
# object.m_top()

# # bottom
# # middle_left
# # top


# LABORATORIO 1
# class Stack:
#     def __init__(self):
#         self.__stk = []

#     def push(self, val):
#         self.__stk.append(val)

#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val


# class CountingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__counter = 0

#     def get_counter(self):
#         return self.__counter

#     def pop(self):
#         self.__counter += 1
#         return Stack.pop(self)


# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter()) # 100

# # LABORATORIO 2
# class QueueError(IndexError):
#     pass


# class Queue:
#     def __init__(self):
#         self.queue = []

#     def put(self, elem):
#         self.queue.insert(0, elem)

#     def get(self):
#         if len(self.queue) > 0:
#             elem = self.queue[-1]
#             del self.queue[-1]
#             return elem
#         else:
#             raise QueueError


# que = Queue()
# que.put(1)
# que.put("perro")
# que.put(False)
# try:
#     for i in range(4):
#         print(que.get())
# except:
#     print("Queue error")
    
# 100
# 1
# perro
# False
# Queue error
    
# LABORATORIO 3
# class QueueError(IndexError):
#     pass


# class Queue:
#     def __init__(self):
#         self.queue = []
#     def put(self,elem):
#         self.queue.insert(0,elem)
#     def get(self):
#         if len(self.queue) > 0:
#             elem = self.queue[-1]
#             del self.queue[-1]
#             return elem
#         else:
#             raise QueueError


# class SuperQueue(Queue):
#     def isempty(self):
#         return len(self.queue) == 0


# que = SuperQueue()
# que.put(1)
# que.put("perro")
# que.put(False)
# for i in range(4):
#     if not que.isempty():
#         print(que.get())
#     else:
#         print("Cola vacía")

# 1
# perro
# False
# Cola vacía

# LABORATORIO 4def two_digits(val):
# def two_digits(val):
#     s = str(val)
#     if len(s) == 1:
#         s = '0' + s
#     return s


# class Timer:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds

#     def __str__(self):
#         return two_digits(self.__hours) + ":" + \
#                two_digits(self.__minutes) + ":" + \
#                two_digits(self.__seconds)

#     def next_second(self):
#         self.__seconds += 1
#         if self.__seconds > 59:
#             self.__seconds = 0
#             self.__minutes += 1
#             if self.__minutes > 59:
#                 self.__minutes = 0
#                 self.__hours += 1
#                 if self.__hours > 23:
#                     self.__hours = 0

#     def prev_second(self):
#         self.__seconds -= 1
#         if self.__seconds < 0:
#             self.__seconds = 59
#             self.__minutes -= 1
#             if self.__minutes < 0:
#                 self.__minutes = 59
#                 self.__hours -= 1
#                 if self.__hours < 0:
#                     self.__hours = 23


# timer = Timer(23, 59, 59)
# print(timer) # 23:59:59
# timer.next_second()
# print(timer) # 00:00:00
# timer.prev_second()
# print(timer) # 23:59:59

# LABORATORIO 5
# class WeekDayError(Exception):
#     pass


# class Weeker:
#     __names = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

#     def __init__(self, day):
#         try:
#             self.__current = Weeker.__names.index(day)
#         except ValueError:
#             raise WeekDayError

#     def __str__(self):
#         return Weeker.__names[self.__current]

#     def add_days(self, n):
#         self.__current = (self.__current + n) % 7

#     def subtract_days(self, n):
#         self.__current = (self.__current - n) % 7


# try:
#     weekday = Weeker('Lun')
#     print(weekday) # Lun
#     weekday.add_days(15)
#     print(weekday) # Mar
#     weekday.subtract_days(23)
#     print(weekday) # Dom
#     weekday = Weeker('Lunes')
# except WeekDayError:
#     print("Lo siento, no puedo atender tu solicitud.") # Lo siento, no puedo atender tu solicitud.
    
# LABORATORIO 6
# import math


# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__y

#     def distance_from_xy(self, x, y):
#         return math.hypot(abs(self.__x - x), abs(self.__y - y))

#     def distance_from_point(self, point):
#         return self.distance_from_xy(point.getx(), point.gety())


# point1 = Point(0, 0)
# point2 = Point(1, 1)
# print(point1.distance_from_point(point2)) # 1.4142135623730951
# print(point2.distance_from_xy(2, 0)) # 1.4142135623730951
    
    
# LABORATORIO 7
# import math


# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__y

#     def distance_from_xy(self, x, y):
#         return math.hypot(abs(self.__x - x), abs(self.__y - y))

#     def distance_from_point(self, point):
#         return self.distance_from_xy(point.getx(), point.gety())


# class Triangle:
#     def __init__(self, vertice1, vertice2, vertice3):
#         self.__vertices = [vertice1, vertice2, vertice3]

#     def perimeter(self):
#         per = 0
#         for i in range(3):
#             per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
#         return per


# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(triangle.perimeter()) # 3.414213562373095
    



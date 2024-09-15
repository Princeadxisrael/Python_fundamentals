# x = "str" 
# print(type(x))

# y= 6
# z=float(y)
# v= str(y)

# print(type(y))
# print(type(z))
# print(type(v))

# class Myclass:
#     x=5
# num1=Myclass()
# print(num1.x)
# class Dog:
#     name= "caeser",
#     color="black"
#     breed="Dogo Argentino"

# Ceaser= Dog()
# Ceaser.name="Caeser"

# snoppy=Dog()
# snoppy.name="snoopy"
# snoppy.breed="german shepered"

# print(Dog)
# print(Ceaser)
# print(snoppy)
# print(Ceaser.name)
# print(snoppy.name)



# print(dennis)
# print(dennis.name)


# principles of OOP
# -Inheritance
# -Polymorphism
# -Encapsulation
# -Abstraction

# INHERITANCE
# Parent Class/ Base class - the class from which properties(attr and methods) are inherited
# Child Class- the class from which inherits properties(attr and methods)

# -Single Inheritance- get properties from a single parent class
# -MultiLevel Inheritance- get properties from a parent class and the parent class inherits from its parents
# -Hierarchical Inheritance- multiple child class to inherit from a parent class
# -Multiple Inheritance- a child class inheriting from multiple parent classes

# class Person:
 
#     def __init__(self, fname, lname):
#         self.fname=fname
#         self.lname=lname
    

#     def __str__(self):
#         return f"{self.fname}"
    
#     def printname(self):
#         print(self.fname, self.lname)
 
# elsie=Person("elsie", "wanjiha")
# kalvine=Person("kalvine", "ndel" )
# # dennis=Person()

# print(Person)
# elsie.printname()

# kalvine.printname()


# class Student(Person):
#     def __init__(self, fname, lname, course, id, subjects):
#         self.course=course
#         self.id=id
#         self.subjects=subjects

#         Person.__init__(self, fname, lname) #invoking the __init__ of the parent class
    
#     def studentdetails(self):
#         print(" my name is {1}, {0}".format(self.fname, self.lname))
#         print(" my Id is {}".format(self.id))
#         print(" my course is {}".format(self.course))
        


# monalisa= Student( "Monalisa", "Onyango", "SD","Python", "oop" )

# print(monalisa)

# # monalisa.printname()
# monalisa.studentdetails()

#Polymorphism - function that has the same but different signatures.
# len("breads") #inbuilt polymorphic function

# def add( x, y, z=1):
#     return x + y + z

# print(add(2,3))
# print(add(2,3,4))

# class Kenya():
#     def capital(self):
#         print("Nairobi is the capital of kenya")
    
#     def language(self):
#         print("Swahili is the most widely spoken language of Kenya")
    
#     def type(self):
#         print("Kenya is a developing country")
    
# class Germany():
#     def capital(self):
#         print("Berlin is the capital of kenya")
    
#     def language(self):
#         print("German is the most widely spoken language of Kenya")
    
#     def type(self):
#         print("Germany is a developed country")
    
# obj_kenya= Kenya()
# obj_ger= Germany()

# for country in (obj_kenya, obj_ger):
#     country.capital()
#     country.language()
#     country.type()

#Polymorphism with inheritance
# class Birds():
#     def intro(self):
#         print("These are birds and there are many types")

#     def flight(self):
#         print("Most birds can fly but some can't")
# class Dove(Birds):
#     def flight(self):
#         print("Doves can fly")

# class Chicken(Birds):
#     def flight(self):
#         print("Chickens cannot fly")

# obj_bird=Birds()
# obj_dove=Dove()
# obj_chicken=Chicken()

# obj_bird.intro()
# obj_bird.flight()

# obj_dove.intro()
# obj_dove.flight()

# obj_chicken.intro()
# obj_chicken.flight()

# class Animal:
#     def speak(self):
#         raise NotImplementedError("subclass must implement this method")

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# class Fish(Animal):
#     def speak(self):
#         pass

# animals=[Dog(), Cat()]

# for animal in animals:
#     print(animal.speak())

# class Vehicle:
#     def move(self):
#         raise NotImplementedError("subclass must implement abstract method")

# class Car(Vehicle):
#     def move(self):
#         return "Car is moving"
    
# class Bike(Vehicle):
#     def move(self):
#         return "Bike is moving"
    
# class Shop(Vehicle):
#     def move(self):
#         return "A shop is not a vehicle"
# vehicles=[Car(), Bike(), Shop()]

# for vehicle in vehicles:
#     print(vehicle.move())

# class Base():
#     __hidden=0

#     def add(self, increment):
#         self.__hidden +=increment
#         print(self.__hidden)

# myobj=Base()
# myobj.add(2)
# myobj.add(5)

# print(myobj.__hidden)

#Class Attributes and Class Methods

# class Dog:
#     no_of_puppies=0
#     MATE=["german-sheperd", "Labrador"]

#     def __init__(self, date,mate):
#         if self.check_mate(mate):
#             self.increment_puppy_no()
#             self.mate=mate
#             self.birthdate=date
#     def print(self, date):
#         self.birth=date
#         print("this puppy was born on {}".format(self.birth))
    
#     @classmethod
#     def check_mate(cls, mate):
#         return mate in cls.MATE

#     @classmethod
#     def increment_puppy_no(cls, increment=1):
#         cls.no_of_puppies += increment

# class Song:
#     all=[]

#     def __init__(self, name):
#         self.name=name
#         Song.add_song_to_all(self)
    
#     @classmethod
#     def add_song_to_all(cls, song):
#         cls.all.append(song)

#     @classmethod 
#     def show_name(cls):
#         print([song.name for song in cls.all])

# titanic=Song("titanic")

# print(Song.all)
# print(titanic.all)
# print(titanic)
# print(titanic.name)
# Song.show_name()

#Iterators
# __iter__() and __next__()

# mytuple=("grape", "apples", "orange", "Lemon")
# myIter= iter(mytuple)

# for x in mytuple:
#     print(x)


# class Mynumbers:

#     def __iter__(self):
#         self.a=1
#         return self
    
#     def __next__(self):
#        if self.a<=10: 
#             x=self.a
#             self.a +=1
#             return x
#        else:
#            raise StopIteration
    
# myclass=Mynumbers()
# myIter=iter(myclass)

# print(myIter)

# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))

#-----OBJECTS RELATIONSHIPS------

#Composition

# class Book:
#     def __init__(self, title, author):
#         self.title=title
#         self.author=author
    
#     def getdetails(self):
#         return f"'{self.title}' by {self.author}"

# class Library:

#     def __init__(self):
#         self.books=[]
    
#     def add_books(self, book):
#         self.books.append(book)

#     def show_books(self):
#         for book in self.books:
#             print(book.getdetails())

# #Create book instances
# book1=Book(title="Things fall apart", author="Chinua Achebe")
# book2=Book(title="Pride and Prejudice", author="Jane Austin")

# print(book2.getdetails())

# #creating a library instance
# library=Library()

# library.add_books(book1)
# library.add_books(book2)

# library.show_books()

# class CPU:
#     def __init__(self, cpu_type):
#         self.cpu_type=cpu_type
    
#     def getCpu(self):
#         return f"{self.cpu_type}"

# class Computer:
#     def __init__(self, cpu_type):
#         self.CPU= CPU(cpu_type)
    

# intel= CPU("core i5")

# hp=Computer(intel)

# print(intel.cpu_type)
# print(hp.getCpu())

#Aggregation

# class Department:

#     def __init__(self, name):
#         self.name=name
#         self.employees=[]
    
#     def add_employee(self, employee):
#         self.employees.append(employee)

#     def show_employees(self):
#         print(f"Department:{self.name}")
#         for employee in self.employees:
#             print(f"employee:{employee.name}")

# class Employee:
#     def __init__(self,name):
#         self.name=name

# accounting_dept=Department("Accounting")

# employee1=Employee("Imelda")
# employee2=Employee("Kevin")
# employee3=Employee("Isaac")

# #add employees to Accounting
# accounting_dept.add_employee(employee1)
# accounting_dept.add_employee(employee2)
# accounting_dept.add_employee(employee3)

# accounting_dept.show_employees()

# hr_dept=Department("HR")
# hr_dept.add_employee(employee2)
# hr_dept.add_employee(employee3)

# hr_dept.show_employees()

# #----Example 2------

# class Car:
#     def __init__(self, engine):
#         self.engine = engine
#         self.shockabsorbers=[]

#     def addshocks(self, shockabsorber):
#         self.shockabsorbers.append(shockabsorber)

#     def showdetails(self):
#         print(f"engine:{self.engine}")
#         for shock in self.shockabsorbers:
#             print(f"{shock.name}")


# class Engine:
#     def __init__(self, cylinders, fuelType):
#         self.cylinders = cylinders
#         self.fuelType = fuelType
# class Schockabsorber:
#     def __init__(self,name):
#         self.name=name

# four_cylinder_engine=Engine(4, "regular")
# honda=Car(four_cylinder_engine)
# toyotashocks=Schockabsorber("toyotashocks")

# toyota=Car()

# toyota.addshocks(toyotashocks)

#---Association---

# class Address:
#     def __init__(self, street, city, state):
#         self.street=street
#         self.city=city
#         self.state=state
    
#     def get_address(self):
#         return f"{self.street}, {self.city}, {self.state}"
    
# class Person:
#     def __init__(self, name, address):
#         self.name=name
#         self.address=address
    
#     def get_info(self):
#         return f"Name: {self.name} \n Address:{self.address.get_address()}"


# home_address= Address(street="Herbert Macualay", city="Newyork", state="Washington")

# kate=Person(name="kate", address=home_address)

# print(kate.get_info())

#---Final Example---

# class Student:
#     def __init__(self, name, student_id):
#         self.name=name
#         self.student_id=student_id
#         self.classes=[]

#     def enrol(self, course_running):
#         self.classes.append(course_running)
#         course_running.add_student(self)

# class Department:
#     def __init__(self, name, department_code):
#         self.name=name
#         self.department_code=department_code
#         self.courses={}

#     def add_course(self, description, course_code, credits):
#         self.courses[course_code]=Course(self,description, course_code, credits)

# class Course:
#     def __init__(self, description, course_code, credits, department):
#         self.description=description
#         self.course_code=course_code
#         self.credits=credits
#         self.department=department #aggregration relationship
#         self.department.add_course(self)

#         self.runnings=[]

#         def add_running(self, year):
#             self.runnings.append(CourseRunning(self,year))
#             return self.runnings[-1]
        
# class CourseRunning:
#     def __init___(self, course, year):
#         self.course=course
#         self.year=year
#         self.students=[]

#     def add_students(self, student):
#         self.students.append(student)

class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class LearnerMixin:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class TeacherMixin:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Tutor(Person, LearnerMixin, TeacherMixin):
    def __init__(self, *args, **kwargs):
        super(Tutor, self).__init__(*args, **kwargs)

jane = Tutor("Jane", "Smith", "SMTJNX045")
jane.enrol("a_postgrad_course")
jane.assign_teaching("an_undergrad_course")

#----Relapacing Inheritance with composition

class Learner:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number

        self.learner = learner
        self.teacher = teacher

jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())
jane.learner.enrol("a_postgrad_course")
jane.teacher.assign_teaching("an_undergrad_course")
class Bank:
    def bank_name(self):
        print("Bank: State Bank")
class Account(Bank):
    def account_type(self):
        print("Account Type: Savings Account")
a = Account()
a.bank_name()
a.account_type()
class Person:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print("Name:", self.name)
class Student(Person):
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def display_course(self):
        print("Course:", self.course)
s = Student("Kiran", "Python")
s.display_name()
s.display_course()


class Vehicle:
    def __init__(self, brand,color):
        self.brand = brand
        self.color=color
    def display_brand(self):
        print("Brand:", self.brand)
        print("color:", self.color)
class Car(Vehicle):
    def __init__(self, brand,color, model):
        super().__init__(brand,color)
        self.model = model
    def display_model(self):
        super().display_brand()
        print("Model:", self.model)
c = Car("Tata","red", "Nexon")
c.display_brand()
c.display_model()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    def display_developer(self):
        super().display_employee()
        print("Programming Language:", self.language)
d = Developer("Kiran", 40000, "Python")
d.display_developer()

class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Puppy(Dog):
    def play(self):
        print("Puppy plays")
p = Puppy()
p.eat()
p.bark()
p.play()

class Person:
    def __init__(self):
        print("Person constructor")
class Student(Person):
    def __init__(self):
        print("Student constructor")
class CollegeStudent(Student):
    def __init__(self):
        print("College Student constructor")
c = CollegeStudent()

class Office:
    def __init__(self):
        print("office constructor")
class CEO(Office):
    def __init__(self):
        super().__init__()
        print("CEO constructor")
class Employee(CEO):
    def __init__(self):
        super().__init__()
        print("Employee constructor")
e= Employee()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my age is " + str(self.age))  # Convert age to a string
 
p1 = Person("John", 36)

p1.age = 40  # Updating the age attribute

p1.myfunc()  # Calling the method
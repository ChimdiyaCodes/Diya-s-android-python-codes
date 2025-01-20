class Diya:
  def __init__(self, name, age, school):
    self.name = name
    self.age = age
    self.school = school

  def __str__(self):
    return f"{self.name}, {self.age}, {self.school}"

me = Diya("Chimdiya", 20, "University")
print(me)


class Person:
  def __init__(self, name, family, number, gift1 = None, gift2 = None):
      self.name = name
      self.family = family
      self.number = number
      self.gift1 = None
      self.gift2 = None

p1 = Person("Tyler", 4, 1)
print p1.name, p1.family, p1.number

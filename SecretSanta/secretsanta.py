class MyClass:
  def __init__(self, name, family, number, gift1, gift2):
      self.name = name
      self.family = family
      self.number = number
      self.gift1 = None
      self.gift2 = None

p1 = MyClass("Tyler", 4, 1, None, None)
print p1.name, p1.family, p1.number

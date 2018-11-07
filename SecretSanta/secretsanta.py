import random

class Person:
  def __init__(self, name, family, number, gift1 = None, gift2 = None, numGifts = 0):
      self.name = name
      self.family = family
      self.number = number
      self.gift1 = None
      self.gift2 = None
      self.numGifts = 0

santaList = [Person("Pat", 1, 1), Person("Missy", 1, 2), Person("Lisa", 1, 3), Person("Bernie", 2, 1), Person("Bonnie", 2, 2), Person("Joe", 3, 1), Person("Irene", 3, 2), Person("Alex", 3, 3), Person("Joey", 3, 4), Person("Tyler", 4, 1), Person("Ashley", 5, 1)]


### randomly pick secret santa gifts

for x in santaList:
    
    while(True):
        z = random.choice(santaList)
        if x.family != z.family and z.numGifts < 2 :
            x.gift1 = z.name
            z.numGifts += 1
            break
    while(True):
        z = random.choice(santaList)
        if x.family != z.family and z.numGifts < 2 and x.gift1 != z.name:
            x.gift2 = z.name
            z.numGifts += 1
            break


###

for x in santaList:
    print x.name, x.family, x.number, x.gift1, x.gift2, x.numGifts
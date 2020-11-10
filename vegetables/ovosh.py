from abc import ABC, abstractmethod

class Ovoshi(ABC):
  def counted(self, count=0):
    self.count = count
  
  def add(self):
    self.count += 1
    self.all_hp = self.hp * self.count

  @abstractmethod
  def list_display(self):
    pass
  
  @abstractmethod
  def eat(self):
    if self.all_hp == 0:
      print("Овощи съедены")
    else:
      self.all_hp -= 5

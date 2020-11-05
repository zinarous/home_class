class Ovoshi():

  def counted(self, count=0):

    self.count = count

  

  def add(self):

    self.count += 1

    self.all_hp = self.hp * self.count 



  def list_display(self):

    print("Количество овощей = ", self.count)

    

  def eat(self):

    if self.all_hp == 0:

      print("Овощи съедены")

    else:

      self.all_hp -= 5



class Tomato(Ovoshi):

  count = 1

  hp = 10



class Cucumber(Ovoshi):

  count = 1

  hp = 15



tom = Tomato()

cu = Cucumber()

tom.add()

tom.add()

tom.list_display()

tom.eat()

print(tom.all_hp, "- осталось ХП у помидора")

cu.add()

cu.list_display()

cu.eat()

print(tom.all_hp, "- осталось ХП у помидора")
ovosh.py
Отображается файл "ovosh.py"

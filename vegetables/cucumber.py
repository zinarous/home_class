from ovosh import Ovoshi
class Cucumber(Ovoshi):
    count = 1
    hp = 15
    def list_display(self):
        print("Количество огурцов = ", self.count)
        
    def eat(self):
        if self.all_hp == 0:
            print("Овощи съедены")
        else:
            self.all_hp -= 10
cu = Cucumber()
cu.add()
cu.list_display()
cu.eat()
print(cu.all_hp, "- осталось ХП у огурца")
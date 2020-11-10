from ovosh import Ovoshi

class Tomato(Ovoshi):
    count = 1
    hp = 10
    def list_display(self):
        print("Количество помидоров = ", self.count)
    def eat(self):
        super().eat
tom = Tomato()
tom.add()
tom.add()
tom.list_display()
tom.eat()
print(tom.all_hp, "- осталось ХП у помидора")
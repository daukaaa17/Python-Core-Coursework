class Bird:
    def __init__(self, name):
        self.name = name
    def fly(self):
        return self.name + ' bird can fly'
    def walk(self):
        return self.name + ' bird can walk'
    def __str__(self):
        return self.name + ' bird can walk'
class FlyingBird(Bird):
    def __init__(self, name, ration = 'grains'):
        super().__init__(name)
        self.ration = ration
    def fly(self):
        super().fly()
    def walk(self):
        super().walk()
    def eat(self):
        return "It eats mostly " + self.ration
    def __str__(self):
        return f"{self.name} bird can walk and fly"
class NonFlyingBird(FlyingBird):
    def __init__(self, name, ration = 'fish'):
        super().__init__(name)
        self.ration = ration
    def walk(self):
        super().walk()
    def fly(self):
        raise AttributeError(f"\"{self.name}\" object has no attribute \"fly\"")
    def swim(self):
        return self.name + ' bird can swim'
    def eat(self):
        return "It eats mostly " + self.ration
    def __str__(self):
        return f"{self.name} bird can walk and swim"
class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name, ration = 'fish'):
        super().__init__(name)
        self.ration = ration
    def walk(self):
        super().walk()
    def fly(self):
        super().fly()
    def swim(self):
        super().swim()
    def eat(self):
        return "It eats mostly " + self.ration
    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"
b = Bird("Any")
#print(b.walk())
p = NonFlyingBird("Penguin", "fish")
#print(p.swim())
#print(p.fly())
#print(p.eat())
c = FlyingBird("Canary")
#print(c.eat())
#s = SuperBird("Gull")
#print(s.eat())

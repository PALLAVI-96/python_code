class Animal:
    
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
    
    
    
    
    def eat(self):
        print(f"{self.name} will eat always")
        
        
        
    def sleep(self):
        print(f" {self.name} will sleep always")
        
class Dog(Animal):
    def __init__(self,breed,name):
        super().__init__(breed,name)
        
    def bark(self):
        super().eat()
        super().sleep()
        print(f"the dog {self.name} will bark")
        
        
    
class Cat(Animal):
    def __init__(self,breed,name):
        super().__init__(breed,name)
        
    def meow(self):
        super().eat()
        super().sleep()
        print(f"the cat {self.name} will meow")
    
    
    
dog1=Dog("tiger","Appu")
dog1.bark()
cat1=Cat("russian","kathu")
cat1.meow()
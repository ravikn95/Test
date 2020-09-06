class Car:
    def __init__(self,maxspeed,strng):
        
        self.maxspeed=maxspeed
        self.strng=strng
        
   
    def display(self):
        print("Car with the maximun speed of "+str(self.maxspeed)+" "+self.strng)
    

class Boat:
    def __init__(self,maxspeed):
       
        self.maxspeed=maxspeed
    
    def display(self):
        print("Boat with the maximum speed of "+str(self.maxspeed)+" knots")
    

obj1=Car(151,"mp/h")
obj2=Boat(77)

obj1.display()
obj2.display()

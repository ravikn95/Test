class test:
    def __init__(self,string,position,character):
        self.string=string
        self.position=position
        self.character=character


    def original(self):
        print("Befor")
        print(self.string)
        
    def replace_name(self):
        self.string=list(self.string)
        self.string[self.position]=self.character
        self.string="".join(self.string)
        print("After")
        print(self.string)
       

    
A=test("good morning",4,'_')
A.original()
A.replace_name()

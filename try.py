class rect:
    def __init__(self):
        self.height = 8
        self.width = 10
    def rectarea(self):
        return self.height*self.width
myRect=rect()
print("area is : ", myRect.rectarea()) 

# this one was easiest compared to the others
# python OOP is sure different from Java OOP
# aren't you afraid of people copying and pasting code?

class Rectangle:
    #Attrib
    width = 0
    height = 0

    #Constru
    def __init__(self, _width: int, _height: int):
        self.width = _width
        self.height = _height

    #Method
    def set_width(self, _width: int):
        self.width = _width
    
    def set_height(self, _height: int):
        self.height = _height

    def get_area(self) -> int:
        return (self.width * self.height)
    
    def get_perimeter(self) -> int:
        return ((self.width * 2) + (self.height * 2))

    def get_diagonal(self) -> float:
        return(((self.width ** 2) + (self.height ** 2)) ** 0.5 )

    def get_picture(self) -> str:
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else: 
            eminem = ""
            for n in range(self.height):
                eminem += "*" * self.width
                eminem += "\n"
            return eminem

    def get_amount_inside(self, shape) -> int:
        return int(self.get_area() / shape.get_area())
    
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    #Attrib
    
    #Constru
    def __init__(self, _side: int):
        super().__init__(_side,_side)

    #Method
    def set_side(self, _side: int):
        self.width = _side
        self.height = _side

    def set_width(self, _width: int):
        self.width = _width
        self.height = _width
    
    def set_height(self, _height: int):
        self.width = _height
        self.height = _height

    def __str__(self) -> str:
        return f"Square(side={self.width})"
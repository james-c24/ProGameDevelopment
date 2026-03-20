class Buildings:
    def __init__(self,height,floors,name):
        self.name = name
        self.height = height
        self.floors = floors       
    def find_height(self):
        print(self.name,"is",self.height,"metres tall")
building = Buildings("Burj Khalifa",830,163)

class Books:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages       
    def find_author(self):
        print(self.title,"is written by",self.author)
book = Books("The Lord of the Rings","J.R.R. Tolkien",1137)

class Countries:
    def __init__(self,name,population,continent):
        self.name = name
        self.population = population
        self.continent = continent
    def find_continent(self):
        print(self.name,"is located in",self.continent)
country = Countries("Italy",59000000,"Europe")

class Rectangles:
    def __init__(self,height,width,colour):
        self.height = height
        self.width = width
        self.colour = colour
    def find_area(self):
        print("This rectangle has an area of",self.height*self.width)
rectangle = Rectangles(500,200,"Blue")

class Materials:
    def __init__(self,name,feel,colour):
        self.name = name
        self.feel = feel
        self.colour = colour
    def find_colour(self):
        print(self.name,"looks",self.colour)
material = Materials("Metal","Solid","Grey")

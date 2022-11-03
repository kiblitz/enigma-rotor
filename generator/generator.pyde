ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TextBox():
    def __init__(self, x, y):
        self.string = ''
        self.ords = []
        self.pos = Vector2D(x, y)

    def type(self, c):
        self.string += c
        self.ords.append(ALPHABET.index(c))
        print(self.string, self.ords)

    def backspace(self):
        if len(self.ords) > 0:
            self.ords.pop()
            self.string = self.string[:len(self.string)-1]
        print(self.string, self.ords)
    
    def draw(self):
        fill(0)
        text(self.string, self.pos.x, self.pos.y)

textbox = TextBox(100, 100)

def setup():
    size(600, 400)
    fill(0)
    textSize(20)

def draw():
    background(255)
    fill(0)
    textbox.draw()

def keyTyped():
    if key >= 'A' and key <= 'z':
        textbox.type(str(key).lower())
    elif key == BACKSPACE:
        textbox.backspace()
    

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

WIDTH = 1800
HEIGHT = 600
FONT_SIZE = 20

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TextBox():
    def __init__(self, x, y):
        self.string = ''
        self.ords = [[]]
        self.pos = Vector2D(x, y)

    def type(self, c):
        self.string += c
        self.ords[len(self.ords) - 1].append(ALPHABET.index(c))
        print(self.string, self.ords)

    def backspace(self):
        if len(self.string) > 0:
            if len(self.ords[len(self.ords) - 1]) == 0:
                self.ords.pop()
            else:
                self.ords[len(self.ords) - 1].pop()
            self.string = self.string[:len(self.string)-1]
        print(self.string, self.ords)
    
    def space(self):
        self.ords.append([])
        self.string += ' '
    
    def draw(self):
        fill(0)
        text("\"" + self.string + "\"", self.pos.x, self.pos.y)

textbox = TextBox(WIDTH/2, HEIGHT - FONT_SIZE)

def setup():
    size(WIDTH, HEIGHT)
    fill(0)
    textSize(FONT_SIZE)
    textAlign(CENTER)

def draw():
    background(255)
    fill(0)
    textbox.draw()

def keyTyped():
    if key >= 'A' and key <= 'z':
        textbox.type(str(key).lower())
    elif key == BACKSPACE:
        textbox.backspace()
    elif key == ' ':
        textbox.space()

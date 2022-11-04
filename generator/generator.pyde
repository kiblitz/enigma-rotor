ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

WIDTH = 1800
HEIGHT = 600
FONT_SIZE = 20
GAP_SIZE = PI/10

MAX_DIM = 300
SPACING = 0.75
STROKE = 20

BACKGROUND = color(255, 255, 255)

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
        
        noFill()

        strokeCap(SQUARE)
        for word in self.ords:
            spacing = len(word) + 1
            max_dim = MAX_DIM
            strokeWeight(4. / (len(word) + 1) * STROKE * max_dim / MAX_DIM)
            for i in range(len(word)-1, -1, -1):
                ord = word[i]
                dim = max_dim * (i + 2) / spacing
                arc(WIDTH/2, HEIGHT/2, dim, dim, -PI/2 + ord * PI/13 + GAP_SIZE/2, 3*PI/2 + ord * PI/13 - GAP_SIZE/2)

textbox = TextBox(WIDTH/2, HEIGHT - FONT_SIZE)

def setup():
    size(WIDTH, HEIGHT)
    noFill()
    textSize(FONT_SIZE)
    textAlign(CENTER)

def draw():
    background(BACKGROUND)
    textbox.draw()

def keyTyped():
    if key >= 'A' and key <= 'z':
        textbox.type(str(key).lower())
    elif key == BACKSPACE:
        textbox.backspace()
    elif key == ' ':
        textbox.space()

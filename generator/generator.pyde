ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

WIDTH = 1800
HEIGHT = 600
FONT_SIZE = 20
GAP_SIZE = PI/10

MAX_DIM = 400
WORD_SPACING_RATIO = 0.22
STROKE = 26

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

    def backspace(self):
        if len(self.string) > 0:
            if len(self.ords[len(self.ords) - 1]) == 0:
                self.ords.pop()
            else:
                self.ords[len(self.ords) - 1].pop()
            self.string = self.string[:len(self.string)-1]
    
    def space(self):
        self.ords.append([])
        self.string += ' '
    
    def draw(self):
        fill(0)
        text("\"" + self.string + "\"", self.pos.x, self.pos.y)
        
        noFill()

        strokeCap(SQUARE)
        max_len = max([len(word) for word in self.ords])
        letter_spacing = max_len + 1
        word_spacing = MAX_DIM * WORD_SPACING_RATIO
        total_space = sum([MAX_DIM * (len(word) + 1) / letter_spacing + word_spacing for word in self.ords]) - word_spacing
        multiplier = 1
        if total_space + word_spacing * 2 > WIDTH:
            multiplier = WIDTH / (total_space + word_spacing * 2)
        offset = total_space / 2 * multiplier
        spacing = 0
        for word in self.ords:
            strokeWeight(4. / letter_spacing * STROKE * multiplier)
            total_dim = MAX_DIM * (len(word) + 1) / letter_spacing * multiplier
            for i in range(len(word)-1, -1, -1):
                ord = word[i]
                dim = MAX_DIM * (i + 2) / letter_spacing * multiplier
                gap_size = GAP_SIZE * 2 / (i + 2)
                arc(WIDTH/2 - offset + spacing + total_dim/2, HEIGHT/2, dim, dim, -PI/2 + ord * PI/13 + gap_size/2, 3*PI/2 + ord * PI/13 - gap_size/2)
            spacing += total_dim + word_spacing * multiplier

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

import pygame, random
pygame.init()
pygame.display.set_caption('Tronners!')
# Variables
WIDTH = 800
HEIGHT = 600
BORDER = 10
VELOCITY = 2

# Classes
class Player: # Using a capital for classes
    WIDTH = 10
    # note these are double underscores - they're called 'dunder' functions
    def __init__(self, name, x, y, vx, vy, color, controls, tail):
        self.name = name
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.playerColor = color
        self.controls = controls
        self.tail = tail
    def show(self,color):
        global screen
        pygame.draw.rect(screen, color, pygame.Rect(self.x,self.y,Player.WIDTH,Player.WIDTH))
    def update(self, opponentTail):
        self.tail.append((self.x, self.y))
        
        nextX = self.x + self.vx
        nextY = self.y + self.vy

        if (nextX, nextY) in self.tail:
            # Handle player hitting themselves.
            print(self.name + " stop hitting yourself.")
        elif (nextX, nextY) in opponentTail:
            # Handle player hitting opponent.
            print(self.name + " stop hitting your opponent!")
        if nextX < BORDER or nextX > WIDTH - BORDER:
            print(self.name + " hit the left or right wall.")
        if nextY < BORDER or nextY > HEIGHT - BORDER:
            print(self.name + " hit the top or bottom wall.")

        # self.show(bgColor)
        self.x = nextX
        self.y = nextY
        self.show(self.playerColor)
    def move(self, direction):
        if direction == self.controls[0]:
            self.vx = - VELOCITY
            self.vy = 0
        elif direction == self.controls[1]:
            self.vx = VELOCITY
            self.vy = 0
        elif direction == self.controls[2]:
            self.vx = 0
            self.vy = - VELOCITY
        elif direction == self.controls[3]:
            self.vx = 0
            self.vy = VELOCITY

# colorOptions = ['blue','red','pink','yellow','grey','green','purple','white']
bgColor = pygame.Color("black")
fgColor = pygame.Color("white")
player1Color = pygame.Color("white")
player2Color = pygame.Color("pink")

# Create objects
gameTimer = pygame.time.Clock()
player1 = Player( "Tom", 50, HEIGHT // 2 + 50, VELOCITY, 0, player1Color, [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN], [] ) # '//' returns the integer value of the division only
player2 = Player( "Che", 200, HEIGHT // 2 - 50, -VELOCITY, 0, player2Color, [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s], [] )

# Draw the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH-BORDER,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH-BORDER,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(WIDTH-BORDER,0,BORDER,HEIGHT))

# Show the objects for the first time
player1.show(player1Color)
print("Player 1 shown")
player2.show(player2Color)
print("Player 2 shown")

running = True
while running:
    pygame.display.flip()
    gameTimer.tick(60) # larger number for faster game speed.
    player1.update(player2.tail)
    player2.update(player1.tail)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player1.move(event.key)
            player2.move(event.key)
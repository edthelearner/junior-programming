import pygame, random
pygame.init()
pygame.display.set_caption('Pongers!')
# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 10
VELOCITY = 0.2

# Classes
class Player: # Using a capital for classes
    WIDTH = 10
    # note these are double underscores - they're called 'dunder' functions
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.playerColor = color
    def show(self,color):
        global screen
        pygame.draw.rect(screen, color, pygame.Rect(self.x,self.y,Player.WIDTH,Player.WIDTH))
    def update(self):
        global bgColor, VELOCITY

        nextX = self.x + self.vx
        nextY = self.y + self.vy

        self.show(bgColor)
        self.x = nextX
        self.y = nextY
        self.show(self.playerColor)
    def move(self, direction):
        if direction == pygame.K_LEFT:
            self.vx = - VELOCITY
            self.vy = 0
        elif direction == pygame.K_RIGHT:
            self.vx = VELOCITY
            self.vy = 0
        elif direction == pygame.K_UP:
            self.vx = 0
            self.vy = - VELOCITY
        elif direction == pygame.K_DOWN:
            self.vx = 0
            self.vy = VELOCITY

# Other colour options
# colorOptions = ['blue','red','pink','yellow','grey','green','purple','white']
bgColor = pygame.Color("black")
fgColor = pygame.Color("white")
player1Color = pygame.Color("white")
player2Color = pygame.Color("pink")

# Create objects
player1 = Player( 50, HEIGHT // 2, VELOCITY, 0, player1Color ) # '//' returns the integer value of the division only

# Draw the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH-BORDER,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH-BORDER,BORDER))
# TO DO - add border on right hand side

# Show the objects for the first time
player1.show(player1Color)
print("Player 1 shown")

running = True
while running:
    # player2.update(keys)
    pygame.display.flip()
    player1.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print("Update being called")
            player1.move(event.key)
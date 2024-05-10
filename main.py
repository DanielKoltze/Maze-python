import pygame
import random




def create_grid_cells(c,r):
    grid = []
    for i in range(int(c)):
        for j in range(int(r)):
            grid.append(Cell(i,j))
    return grid




class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"right":True,"left":True,"up":True,"down":True}

    def __str__(self) -> str:
        return f'{self.x} {self.y}'
    
    def draw(self):
        x = self.x * SQUARESSIZE
        y = self.y * SQUARESSIZE
        if self.visited:
            pygame.draw.rect(sc, BLACK, (x, y, SQUARESSIZE, SQUARESSIZE))

        if self.walls["up"]:
            pygame.draw.line(sc, WHITE, (x , y), (x + SQUARESSIZE, y), 2)
        if self.walls["right"]:
            pygame.draw.line(sc, WHITE, (x + SQUARESSIZE, y), (x + SQUARESSIZE, y + SQUARESSIZE), 2)
        if self.walls["down"]:
            pygame.draw.line(sc, WHITE, (x, y + SQUARESSIZE), (x + SQUARESSIZE, y + SQUARESSIZE), 2)
        if self.walls["left"]:
            pygame.draw.line(sc, WHITE, (x, y), (x, y + SQUARESSIZE), 2)
            
    def find_neighbor(self):
        neighbors = []
        top = self.check_neighbor(self.x,self.y-1)
        right = self.check_neighbor(self.x+1,self.y)
        down = self.check_neighbor(self.x,self.y+1)
        left = self.check_neighbor(self.x-1,self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if down and not down.visited:
            neighbors.append(down)
        if left and not left.visited:
            neighbors.append(left)
        #if len(neighbors) == 0:
        #    return False
        return random.choice(neighbors)

    def check_neighbor(self,y,x):
        if x < 0 or x > cols - 1 or y < 0 or y > rows -1:
            return False
        return grid_cells[x+y*cols]
            
    


# 0,0 1,0 2,0
# 0,1 1,1 2,1
# 0,2 1,2 2,2









WIDTH, HEIGHT = 300, 300
BUFFER = 1
SQUARESSIZE = 20
cols = WIDTH // SQUARESSIZE
rows = HEIGHT // SQUARESSIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
sc = pygame.display.set_mode((WIDTH+2,HEIGHT+2))
clock = pygame.time.Clock()
grid_cells = create_grid_cells(cols,rows)
next_cell = ''
stack = []
current_cell = grid_cells[0]
current_cell.visited = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    sc.fill(pygame.Color('Blue'))
    [cell.draw() for cell in grid_cells]
    next_cell = current_cell.find_neighbor()
    if next_cell:
        next_cell.visited = True
        current_cell = next_cell
    

    pygame.display.flip()
    clock.tick(5)


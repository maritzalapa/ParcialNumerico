import sys,pygame

class Point:
    def __init__(self,px,py,velx,vely):
        self.px = px
        self.py = py
        self.rad = 3
        self.color = 0,255,0
        self.vx = velx
        self.vy = vely
        self.started = False

    def update(self):
        self.px += self.vx
        self.py += self.vy
    



FPS = 60
pygame.init()
size = width, height = 600,400
black = 0,0,0
screen = pygame.display.set_mode(size)
last_fps = 0
points = []
count=0

for i in range(5):
    point = Point(20,25,20,0)
    points.append(point)
    
def update():
    if count<5: points[count].started=True
    for i in range(5):
        if points[i].started:
            points[i].update()

def draw():
    for i in range(5):
        if points[i].started:
            pygame.draw.circle(screen, points[i].color, (points[i].px,points[i].py), points[i].rad)        
            
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    if pygame.time.get_ticks() - last_fps > FPS:
        last_fps = pygame.time.get_ticks()
        draw()
        count+=1
        pygame.display.flip()
        update()
        

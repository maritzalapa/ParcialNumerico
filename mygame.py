import sys,pygame
FPS = 10
pygame.init()
size = width, height = 600,400
black = 0,0,0
screen = pygame.display.set_mode(size)
x=0
y=20
last_fps = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    pygame.draw.circle(screen, (0,255,0), (x,y), 3)
    pygame.display.flip()
    if pygame.time.get_ticks() - last_fps > FPS:
        last_fps = pygame.time.get_ticks()
        x= x+1

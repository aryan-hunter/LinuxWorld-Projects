import pygame 
pygame.init()
screen = pygame.display.set_mode((400, 300))
screen.fill((255, 255, 255))
pygame.display.set_caption("x 0 Game")
white = (255, 255, 255)
black = (0, 0, 0)
size = 40
bord = [["","",""],["","",""],["","",""]]
player = "x"
fontt = pygame.font.Font(None, 100)
run = True
screen.fill(white)
pygame.draw.line(screen,black,(200,0),(200,600),5)
pygame.draw.line(screen,black,(400,0),(400,600),5)
pygame.draw.line(screen,black,(200,0),(400,600),5)
pygame.draw.line(screen,black,(0,400),(600,400),5)
for row in range(3):
    for col in range(3):
        if bord[row][col] != "":
            text = fontt.render(bord[row][col], True, black)
            screen.blit(text, (col * size + 70), (row * size + 50))
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        row = mouse_y  //200
        col = mouse_x //200
        if bord[row][col] == "":
            bord[row][col] = player
            if player == "x":
                player = "0"
            else:
                player = "x"
    pygame.display.update()
pygame.quit()
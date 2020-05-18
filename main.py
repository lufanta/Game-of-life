import pygame
import numpy as np
import matplotlib.pyplot as plt
import time

size = widht, height = 700, 700

nXC= 120
nYC = 120
dimCW = (widht + 1) / nXC
dimCH = (height + 1) / nYC
bg = 25, 25, 25
screen = pygame.display.set_mode(size)


gameState = np.zeros((nXC, nYC))

fast = True
game = False

while True:

    if not fast:
        time.sleep(0.2)

    screen.fill(bg)
    new_gameState = np.copy(gameState)
    #Creando rejillas    
    #Calculando la iterraccion humana
    for eve in pygame.event.get()  :
        if eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_SPACE:
                game = not game
            if eve.key == pygame.K_RETURN:
                fast = not fast

        elif eve.type == pygame.QUIT:
                pygame.quit()
                exit()

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) >= 1:
            posx, posy = pygame.mouse.get_pos()
            
            celX, celY = int(np.floor(posx / dimCW)), int(np.floor(posy / dimCH))
            new_gameState[celX, celY] = not mouseClick[2] 


    for y in range(0, nYC):
        for x in range(0, nXC):
            if game: # Cuando game = True, cambiar el estado del juego
                #Calculamos el numero de vecinos vivos
                
                n_neight = gameState[(x -1) % nXC, (y -1) % nYC] + \
                    gameState[x % nXC, (y -1) % nYC] + \
                    gameState[(x + 1) % nXC, (y -1) % nYC] + \
                    gameState[(x -1) % nXC, (y) % nYC] + \
                    gameState[(x + 1) % nXC, (y) % nYC] + \
                    gameState[(x -1) % nXC, (y + 1) % nYC] + \
                    gameState[x % nXC, (y + 1) % nYC] + \
                    gameState[(x + 1) % nXC, (y + 1) % nYC]
    
                

                # Una celula muerta con exctamente tre celulas vecinas nace
                if gameState[x, y] == 0 and n_neight == 3:
                    new_gameState[x, y] = 1

                # Una celula viva con menos de dos o mas de tres celulas vecinas vivas muere.
                elif gameState[x, y] == 1 and (n_neight < 2 or n_neight > 3):
                    new_gameState[x, y] = 0
                    print("muere")
                    print(int(abs(1 - new_gameState[x,y])))

            #Pintar cada cuadrado
            poly = [((x) * dimCW,(y) * dimCH),
                        ((x + 1)* dimCW,(y)* dimCH),
                        ((x + 1) * dimCW, (y + 1) * dimCH), 
                        ((x) * dimCW, (y + 1)* dimCH)
                         ]
            
            pygame.draw.polygon(screen, (128, 128, 128), poly, int(abs(1 - gameState[x,y]))) # 0 = lleno, 1 = vacio

    gameState = new_gameState

    pygame.display.flip()

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame, sys
import numpy as np

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 20)
textifwin1 = myfont.render('PLAYER 1 HAS WON, PRESS R TO RESTART', False, (0, 0, 0))
textifwin2 = myfont.render('PLAYER 2 HAS WON, PRESS R TO RESTART', False, (0, 0, 0))
textifdraw = myfont.render('ITS A DRAW, PRESS R TO RESTART', False, (0, 0, 0))
WIDTH = 600
HEIGHT = 600
COLOR = (173, 216, 230)
CIRCLE = (255,255,255)
DIEZ = (0,0,0)
ROW = 3
COL = 3
game = np.zeros((ROW, COL))



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(COLOR)
pygame.draw.line(screen, (255, 0, 0), (0, 200), (600, 200), 10)
pygame.draw.line(screen, (255, 0, 0), (0, 400), (600, 400), 10)
pygame.draw.line(screen, (255, 0, 0), (200, 0), (200, 600), 10)
pygame.draw.line(screen, (255, 0, 0), (400, 0), (400, 600), 10)

def marked_square(row, col, player):
    game[row][col] = player

def check_board(row, col):
    return game[row][col] == 0

def figures():
    for row in range(ROW):
        for col in range(COL):
            if game[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE, (int(col * 200  + 100), int(row * 200  + 100)), 60, 15 )
            elif game[row][col] == 2:
                pygame.draw.line(screen, DIEZ, (col * 200 + 40 , row * 200 + 200 - 40) , (col * 200 + 200 - 40 , row * 200 + 40), 25)
                pygame.draw.line(screen, DIEZ, (col * 200 + 40 , row * 200 + 40) , (col * 200 + 200 - 40 , row * 200 + 200 - 40), 25)    

def win(player):
    for col in range(COL):
        if game[0][col] == player and game[1][col] == player and game[2][col] == player:
            draw_vert_winning_line(col, player)
            return True        
    
    for row in range(ROW):
        if game[row][0] == player and game[row][1] == player and game[row][2] == player:
            draw_horz_winning_line(col, player)
            return True
            
    if game[2][0] == player and game[1][1] == player and game [0][2] == player:
        draw_asc_diag_winning_line(player)
        return True
    
    if game[0][0] == player and game[1][1] == player and game [2][2] == player:
        draw_desc_diag_winning_line(player)

def draw_vert_winning_line(col, player):
    posX = col * 200 + 100
    
    if player == 1:
        color = CIRCLE
    elif player == 2:
        color = DIEZ
    
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)
    
def draw_horz_winning_line(row, player):
    posY = row * 200 + 100
    
    if player == 1:
        color = CIRCLE
    elif player == 2:
        color = DIEZ
    
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)    

def draw_asc_diag_winning_line(player):    
    
    if player == 1:
        color = CIRCLE
    elif player == 2:
        color = DIEZ
    
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_desc_diag_winning_line(player):    
    
    if player == 1:
        color = CIRCLE
    elif player == 2:
        color = DIEZ
    
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():
    screen.fill(COLOR)
    for row in range(ROW):
        for col in range(COL):
            game[row][col] == 0
    
player = 1
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            X = event.pos[0] 
            Y = event.pos[1] 
            
            clicked_row = int(Y // 200)
            clicked_col = int(X // 200)
            
            if check_board(clicked_row, clicked_col):
                if player == 1:
                    marked_square(clicked_row, clicked_col, 1)
                    if win(player):
                        screen.blit(textifwin1, (100, 300))
                        game_over = True
                    player = 2
                
                elif player == 2:
                    marked_square(clicked_row, clicked_col, 2)
                    if win(player):
                        screen.blit(textifwin2, (100, 300))
                        game_over = True
                    player = 1
                
                figures()
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            restart()
        
               
    pygame.display.update()
    


# In[ ]:





# In[ ]:





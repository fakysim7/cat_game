import pygame
from sys import exit 
from random import randint


def disp_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (60,60,60))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time




pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Jumper')
cloc = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
did_font = pygame.font.Font('font/Pixeltype.ttf', 100)
game_activ = True
start_time = 0
time_spd=5
score = 0

sity_surface = pygame.image.load('games/sity2d.png').convert_alpha()
sity_surface_slow = pygame.transform.scale(sity_surface, (800,400))

ground_surface = pygame.image.load('games/ground.png').convert_alpha()
ground_surface_sm = pygame.transform.scale(ground_surface, (800,100))

surface_wind_g = pygame.Surface((800, 50))
surface_wind_g.fill('#7FFF00')

#text
#score_surf = test_font.render('My game', False, (60,60,60))
#score_rect = score_surf.get_rect(center = (400, 50))
#did_surf = test_font.render('YOU DIED', False, 'black')
#did_rect = score_surf.get_rect(center = (400, 50))

#ulitka obstacles
animu_surf = pygame.image.load('games/ulitka1.png').convert_alpha()
ulitka_rect = animu_surf.get_rect(bottomright = (600,335))




#ulitka respawn
animu_surf_big = pygame.transform.scale(animu_surf, (320, 200))
animu_big_rect = animu_surf_big.get_rect(center = (400, 200))


#player
player_sur = pygame.image.load('games/player/player.png').convert_alpha()
player_rect = player_sur.get_rect(midbottom = (200,335))
player_gravity = 0

#text Game Over
rest_surf = test_font.render('Press RSHIFT to run ', False, 'black')
rest_rect = rest_surf.get_rect(center = (400, 350))
did_surf = test_font.render('YOU DIED', False, 'black')
did_rect = did_surf.get_rect(center = (400, 50))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1300)


while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  #EXIT to screen
            pygame.quit()
            exit()
        if game_activ:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >=335: 
                    player_gravity = -15
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >=335: 
                    player_gravity = -15


        
        else:
           if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
            game_activ = True
            ulitka_rect.left = 900
            start_time = int(pygame.time.get_ticks()/1000)

        
                


    if game_activ:    
        screen.blit(sity_surface_slow, (0,0))    
        screen.blit(ground_surface_sm, (0,300))
        #pygame.draw.rect(screen, '#8B8B83', score_rect)
        #pygame.draw.rect(screen, '#8B8B83', score_rect, 10)
        #screen.blit(score_surf, score_rect)
        disp_score()

        score = disp_score()

        #ulitka
        time_spd = 5
        ulitka_rect.left -=5
        if ulitka_rect.x <= -100: ulitka_rect.right = 900
        screen.blit(animu_surf, ulitka_rect)
        speed_= 1
        if score > time_spd:
            time_spd += 5 
            speed_ +=1
            ulitka_rect.left -=speed_
        
        

        #player
        screen.blit(player_sur, player_rect)
        player_gravity +=0.5
        player_rect.y += player_gravity
        if player_rect.bottom >= 335:
            player_rect.bottom = 335

        if ulitka_rect.colliderect(player_rect):
            game_activ = False

        
            
        

        

        

        
    
    else:
        screen.fill('#5A030D')
        screen.blit(did_surf, did_rect)
        score_message = test_font.render(f'Your score: {score}', False, 'black')
        score_message_rect = score_message.get_rect(center = (400,350))
        if score < 10:
            screen.blit(rest_surf, rest_rect)
        else:
            screen.blit(score_message, score_message_rect)
        screen.blit(animu_surf_big, animu_big_rect)
        
                



    

            
    pygame.display.update()
    cloc.tick(60)
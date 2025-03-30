import pygame

import time
import random

W = 600
H = 500

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('python game')

snake_pos = [80, 30]
snake_speed = 10  

clock = pygame.time.Clock()


snake_body = [[50, 30],[40, 30]]

fruit_pos = [random.randrange(1, (W//10)) * 10,random.randrange(1, (H//10)) * 10]

fruit = True 

score = 0
def show_score(): 
	font = pygame.font.SysFont('Arial', 20)
	Font = font.render('score : ' + str(score), True, 'white')	
	rect = Font.get_rect()	
	screen.blit(Font, rect)


def game_over():
	font = pygame.font.SysFont('Arial', 30)
	Font = font.render('game over      score: ' + str(score), True, 'white')
	rect = Font.get_rect()
	rect.midtop = (W/2, H/4)
	screen.blit(Font, rect)
	pygame.display.flip()
	time.sleep(2)
	pygame.quit()
	quit()



dir = 'RIGHT' 
next_dir = dir 

running = True

while running: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				next_dir = 'UP'
			if event.key == pygame.K_DOWN:
				next_dir = 'DOWN'
			if event.key == pygame.K_LEFT:
				next_dir = 'LEFT'
			if event.key == pygame.K_RIGHT:
				next_dir = 'RIGHT'

	if next_dir == 'UP' and dir != 'DOWN':
		dir = 'UP'
	if next_dir == 'DOWN' and dir != 'UP':
		dir = 'DOWN'
	if next_dir == 'LEFT' and dir != 'RIGHT':
		dir = 'LEFT'
	if next_dir == 'RIGHT' and dir != 'LEFT':
		dir = 'RIGHT'

	if dir == 'UP':
		snake_pos[1] -= 10
	if dir == 'DOWN':
		snake_pos[1] += 10
	if dir == 'LEFT':
		snake_pos[0] -= 10
	if dir == 'RIGHT':
		snake_pos[0] += 10

	
	snake_body.insert(0, list(snake_pos))
	
	if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]: 
		score += 1
		if score % 5 == 0:
			snake_speed += 5
			
		fruit = False
	else:
		snake_body.pop()
		
   
	if not fruit:
		fruit_pos = [random.randrange(1, (W//10)) * 10,random.randrange(1, (H//10)) * 10]
		
	fruit = True
	screen.fill('black')
	
	for pos in snake_body:
		pygame.draw.rect(screen, 'light green',(pos[0], pos[1], 10, 10))
		
	pygame.draw.circle(screen, 'red', (fruit_pos[0]+5, fruit_pos[1]+5),5)
	

	if snake_pos[0] < 0 or snake_pos[0] > W:
		game_over()
	if snake_pos[1] < 0 or snake_pos[1] > H:
		game_over()
	for block in snake_body[1:]:
		if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
			game_over()

	show_score()

	pygame.display.update()
	clock.tick(snake_speed)
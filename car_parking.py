import pygame
import random

n=4 
def isValid(n, maze, x, y, res):
	if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and res[x][y] == 0:
		return True
	return False

# A recursive utility function to solve Maze problem


def CarMaze(n, maze, move_x, move_y, x, y, res):
	# if (x, y is goal) return True
	if x == n-1 and y == n-1:
		return True
	for i in range(4):
		# Generate new value of x
		x_new = x + move_x[i]

		# Generate new value of y
		y_new = y + move_y[i]

		# Check if maze[x][y] is valid
		if isValid(len(maze), maze, x_new, y_new, res):

			# mark x, y as part of solution path
			res[x_new][y_new] = 1
			if CarMaze(len(maze), maze, move_x, move_y, x_new, y_new, res):
				return True
			res[x_new][y_new] = 0
	return False


def solveMaze(maze):
	# Creating a 4 * 4 2-D list
    
	res = [[0 for i in range(len(maze))] for i in range(len(maze))]
	res[0][0] = 1

	# x matrix for each direction
	move_x = [-1, 1, 0, 0]

	# y matrix for each direction
	move_y = [0, 0, -1, 1]

	if CarMaze(len(maze), maze, move_x, move_y, 0, 0, res):
		for i in range(n):
			for j in range(n):
				print(res[i][j], end=' ')
			print()
	else:
		print('Solution does not exist');return False
	return res

# Driver program to test above function
	# Initialising the maze


nomaze = [
    [1,0,1,1,0,0,1,1,0,0],
    [1,1,1,0,0,0,0,0,0,0],
    [1,0,1,1,0,0,1,1,0,0],
    [0,1,1,0,0,1,0,1,0,1],
    [1,0,1,1,0,0,1,1,0,0],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,0,0,1,1,0,0],
    [0,0,0,0,0,0,1,0,0,1],
    [0,0,1,1,0,0,1,1,1,1]
    
]

result = solveMaze(nomaze)





pygame.init()

h=w=50

x=y=50

display_height=600
display_width=600

win=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('game board')

win.fill((103,106,200))


blockCar = pygame.image.load('C:/Users/naras/Desktop/blocks_car.png')
blockCar = pygame.transform.scale(blockCar,(50,50))

mainCar = pygame.image.load('C:/Users/naras/Desktop/car_image.jfif')
mainCar = pygame.transform.scale(mainCar,(50,50))
mainCar = pygame.transform.rotate(mainCar,270)

def car(img,x,y):
    win.blit(img, (x,y))


boardcreation=True
#for board
for i in range(len(nomaze)):
    for j in range(len(nomaze[0])):
        if nomaze[i][j] ==0:
            #               root  color  (x,y,width,height)
            pygame.draw.rect(win,(0,0,0),(x+j*w,y+i*h,w,h))
            car(blockCar,x+j*w,y+i*h)
            
        else:
            pygame.draw.rect(win,(255,255,255),(x+j*w,y+i*h,w,h))
        
        if result and result[i][j]==1:
            pygame.draw.rect(win,(0,255,0),(x+w/4+j*w,y+h/4+i*h,w/2,h/2))
            # car(mainCar,x+j*w,y+i*h)
if result:
    car(mainCar,x+j*w,y+j*h)
else:
    car(mainCar,x,y)
pygame.display.flip()


#for tokens
while boardcreation:
    pass
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            boardcreation=False
    
pygame.quit()
exit()

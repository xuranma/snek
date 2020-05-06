import numpy as np
import pygame

# 0 is at bottom left of game board
# +x is to the right
# +y is up

# Play snake - game initializer

def playsnake(display, pixelsperpiece, boardcolour, snakecolour, foodcolour, tickspermove):
    
    '''
    Note: may need to make changes to UI to make this run cleaner, but this should work barebones
    '''
    
    # Start the game
    
    pygame.init()
    dis = pygame.display.set_mode(display)
    pygame.display.update()
    pygame.display.set_caption('Snek! By David and Jimmy')
    clock = pygame.time.Clock()
    
    game_over = False
    while not game_over:
        
        # Quit if x is clicked
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
                
        # Call board class to get board state (if not initialized, determine initial snake and food placement)
        
        '''
        Make the call to board here, outputting:
        - Coordinates of snake (list of tuples type snake)
        - Coordinates of food (tuple type food)
        - Game over? (binary integer type done)
        
        Feed the desired move if it has been initialized (otherwise tell board to initialize snake and food)
        Also feed necessary initialization variable: board size (display / pixelsperpiece)
        '''
        
        # If game over, close game (for now - could edit later)
        
        if done:
            game_over = True
        
        # Draw the snake in blue and food in red
        
        dis.fill(boardcolour)
        
        for segment in snake:
            pygame.draw.rect(dis, snakecolour, [segment[0] * pixelsperpiece, segment[1] * pixelsperpiece, pixelsperpiece, pixelsperpiece])
            
        pygame.draw.rect(dis, foodcolour, [food[0] * pixelsperpiece, food[1] * pixelsperpiece, pixelsperpiece, pixelsperpiece])
        
        pygame.display.update()
        
        # Get desired move
        
        '''
        Make call to program or keyboard to get desired move (up, down, left, right)
        Need to tell program to keep same movement direction if no move selected after x seconds
        '''
        
        clock.tick(tickspermove)
    
    pygame.quit()
    quit()
    
    # Get final score
    
    '''
    Make call to board to output final score variable (integer type score)
    '''
    
    return score

# Snake class

class snake:
    
    def __init__(self, bounds):
        
        # Function: generates 1-block snake
        
        # First element of snake is the head; last element is the tail
        # bounds is a tuple with size of board: either rectangle or square
        
        self.snake = [(np.random.randint(0, bounds[0]), np.random.randint(0, bounds[1]))]
        self.length = 1
        
        return self.snake, self.length
        
    def grow(self, state):
        
        # Function: grow snake at head if eating a block - board class will detect if food is available and movement is valid
        
        # State = (x, y) where x or y = +1 or -1
        
        newsnake = self.snake
        newsnake.insert(0, tuple(map(sum, zip(state, newsnake[0]))))
        self.snake = newsnake
        self.length = self.length += 1
        
        return self.snake, self.length
        
    def move(self, state):
        
        # Function: move snake forward in direction of state - board class will detect if movement is valid
        
        # State = (x, y) where x or y = +1 or -1
        
        newsnake = self.snake
        newsnake.insert(0, tuple(map(sum, zip(state, newsnake[0]))))
        newsnake = newsnake[:-1]
        self.snake = newsnake
        
        return self.snake, self.length

# Food class
        
class food:
    
    def __init__(self, bounds, snake):
        
        # Function: creates new position of food randomly in board
        
        # bounds is a tuple with size of board: either rectangle or square
        
        choices = [(x, y) for x in bounds[0] for y in bounds[1]]
        choices = [choice for choice in choices if choice not in snake]
        self.food = choices[np.random.randint(0, len(choices))]
        
        return self.food
    
    def eaten(self, snake, state):
        
        # Function: takes original snake and intended movement and checks if that movement would cause food to be eaten
        
        check = tuple(map(sum, zip(state, snake[0])))
        
        return self.food = check # True if food is eaten, False if not
    
    # If food is eaten, trigger a new instance of class with new snake position
    
# Main block: run game
    
if __name__ == "__main__":
    
    # Board size variables
    
    board = (25, 25)
    pixelsperpiece = 10 # 10 pixels per piece on the board
    display = tuple(pixelsperpiece * x for x in board)
    
    # Board colour variables
    
    boardcolour = (255, 255, 255) # white
    snakecolour = (0, 0, 0) # black
    foodcolour = (0, 255, 0) # green
    
    # Timing variables
    
    tickspermove = 30
    
    score = playsnake(display, pixelsperpiece, boardcolour, snakecolour, foodcolour, tickspermove)
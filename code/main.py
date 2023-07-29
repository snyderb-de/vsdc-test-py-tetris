from settings import *
from sys import exit

# create window
class Main:
    def __init__(self):

        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock() # for timers and fps
        pygame.display.set_caption('This is pyTet')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # exit all 
                    exit()
        
            # display
            self.display_surface.fill(GRAY)
            
            # update the game
            pygame.display.update()
            self.clock.tick(60) # 60 fps

if __name__ == '__main__':
    main = Main()
    main.run()

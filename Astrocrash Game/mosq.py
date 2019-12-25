# Mosquito
# Get mosquito moving on the screen

import random
from superwires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)


class Mosquito(games.Sprite):
    """ An mosquito which floats across the screen. """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    SPEED = 2
    images = {SMALL  : games.load_image("mos_small.bmp"),
              MEDIUM : games.load_image("mos_med.bmp"),
              LARGE  : games.load_image("mos_big.bmp") }

    
      
    def __init__(self, x, y, size):
        """ Initialize mosquito sprite. """
        super(Mosquito, self).__init__(
            image = Mosquito.images[size],
            x = x, y = y,
            dx = random.choice([1, -1]) * Mosquito.SPEED * random.random()/size, 
            dy = random.choice([1, -1]) * Mosquito.SPEED * random.random()/size)
        
        self.size = size

    def update(self):
        """ Wrap around screen. """    
        if self.top > games.screen.height:
            self.bottom = 0
 
        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width


def main():
    # establish background
    nebula_image = games.load_image("nebula.jpg")
    games.screen.background = nebula_image

    # create 8 asteroids
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Mosquito.SMALL, Mosquito.MEDIUM, Mosquito.LARGE])
        new_mosquito = Mosquito(x = x, y = y, size = size)
        games.screen.add(new_asteroid)
        
    games.screen.mainloop()

# kick it off!
main()


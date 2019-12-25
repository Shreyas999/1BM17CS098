from superwires import games
games.init(screen_width=640, screen_height=480, fps=50)
#makes screen with width, height, and frames per second
class Bouncy_Ball(games.Sprite):
    image = games.load_image("pizza.bmp")
    def __init__(self):
        super(Bouncy_Ball,self).__init__(image=Bouncy_Ball.image, x=320, y=240,dx=3,dy=3)
    def update(self): #this is empty by default but is called every frame
        if self.left<=0 or self.right>=640:#right and left edges to check if on edge
                #self.dx*=-1#reverse x velocity
            pass

        if self.top<=0 or self.bottom>=480:#top and bottom edges to check if on edge
            self.dy*=-1#reverse y velocity
            #games.screen.add(Bouncy_Ball())
def main():
    ballfield_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = ballfield_image
    #games.screen.background=load_image('ball_field.jpg')
    #games.screen.add(Sprite(games.load_image('ball_field.jpg'), x=320, y=240, dx=3, dy=3
    the_ball = Bouncy_Ball()
    games.screen.add(the_ball)
    games.screen.mainloop()
main()

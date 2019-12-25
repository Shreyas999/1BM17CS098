# Explosion
# Demonstrates creating an animation

from superwires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

nebula_image = games.load_image("nebula.jpg", transparent = 0)
games.screen.background = nebula_image

explosion_files = ["nwf1.png",
                   "nwf2.png",
                   "nwf3.png",
                   "nwf4.png",
                   "nwf5.png",
                   "nwf6.png",
                   "nwf8.png",
                   "nw10.png"]
          
explosion = games.Animation(images = explosion_files,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            n_repeats = 0,
                            repeat_interval = 10)
games.screen.add(explosion)

games.screen.mainloop()

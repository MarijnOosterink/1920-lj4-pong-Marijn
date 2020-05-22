import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"

score_1 = 0
score_2 = 0

#kleur van de tekst
text_color = arcade.color.BLACK

class Ball():
    def __init__(self, x, y, radius, color):
     self.x = x
     self.y = y
     self.radius = radius
     self.color = color
     self.delta_x = 0
     self.delta_y = 0
    
    
    def on_draw(self):
     arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)
    
    def on_update(self, delta_time):
     self.x = self.x + self.delta_x
     self.y = self.y + self.delta_y    
    
class Paddle():
    def __init__(self, width, height, x, y, color, delta_y):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.delta_y = 0
    
    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)
    
    def on_update(self, delta_time):
        self.y = self.y + self.delta_y

class Line():
    def __init__(self, width, height, x, y, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)


    

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        #zet de achtergrond kleur
        arcade.set_background_color(arcade.color.JAPANESE_INDIGO)
        
        #zet de variabelen voor de verschillende onderdelen
        self.my_ball = Ball(400, 300, 20, arcade.color.HAN_PURPLE)

        self.my_paddle = Paddle(20, 125, 20, 100, arcade.color.AIR_SUPERIORITY_BLUE, 0)
        self.my_paddle2 = Paddle(20, 125, 780, 100, arcade.color.ALLOY_ORANGE, 0)

        self.my_line = Line(5, 600, 1, 300, arcade.color.BLACK)
        self.my_line2 = Line(5, 600, 799, 300, arcade.color.BLACK)

     

    def setup(self):
       pass

    def on_draw(self): 
        
        #start de render en render de onderstaande onderdelen
        arcade.start_render()
        arcade.draw_text(f"press space to continue", 400, 400, text_color, 30, align="center", anchor_x="center", anchor_y="center")
        self.my_ball.on_draw()
        self.my_paddle.on_draw()
        self.my_paddle2.on_draw()
        self.my_line.on_draw()
        self.my_line2.on_draw()
    

        #teken het scoreboard
        arcade.draw_text(f"player 1: {score_1}      player 2: {score_2}", 400, 570, arcade.color.BLACK, 15, align="center", anchor_x="center", anchor_y="center")
        
       
        


    def on_update(self, delta_time):

        #delta_time voor bewegende onderdelen
        self.my_paddle.on_update(delta_time)
        self.my_paddle2.on_update(delta_time)
        self.my_ball.on_update(delta_time)

        #paddles kunnen niet hoger en lager dan het scherm
        if self.my_paddle.y + self.my_paddle.height/2 >= SCREEN_HEIGHT:
             self.my_paddle.delta_y = 0
        if self.my_paddle2.y + self.my_paddle2.height/2 >= SCREEN_HEIGHT:
             self.my_paddle2.delta_y = 0
        if self.my_paddle.y - self.my_paddle.height/2 <= 0:
             self.my_paddle.delta_y = 0
        if self.my_paddle2.y - self.my_paddle.height/2 <= 0:
             self.my_paddle2.delta_y = 0 
        
       
        #bal stuitert tegen de boven en onderkant
        if self.my_ball.y == SCREEN_HEIGHT - self.my_ball.radius:
             self.my_ball.delta_y = self.my_ball.delta_y * -1
        if self.my_ball.y == 0 + self.my_ball.radius:
             self.my_ball.delta_y = self.my_ball.delta_y * -1

        #paddle links tegen bal
        if self.my_ball.x - self.my_ball.radius <= self.my_paddle.x + self.my_paddle.width/2 and \
            self.my_ball.y >= (self.my_paddle.y - self.my_paddle.height/2) and \
            self.my_ball.y <= (self.my_paddle.y + self.my_paddle.height/2):
             self.my_ball.delta_x = self.my_ball.delta_x * -1
        
        #paddle rechts tegen bal
        if self.my_ball.x + self.my_ball.radius >= self.my_paddle2.x - self.my_paddle2.width/2 and \
            self.my_ball.y >= (self.my_paddle2.y - self.my_paddle2.height/2) and \
            self.my_ball.y <= (self.my_paddle2.y + self.my_paddle2.height/2):
             self.my_ball.delta_x = self.my_ball.delta_x * -1

        #resetten van + score voor player 1
        if self.my_ball.x <= self.my_line.x:
            self.my_ball.x = 400
            self.my_ball.y = 300
            self.my_ball.delta_x = 0
            self.my_ball.delta_y = 0 
            global score_2
            score_2 = score_2 + 1

        #resetten van bal + score voor player 2
        if self.my_ball.x >= self.my_line2.x:
            self.my_ball.x = 400
            self.my_ball.y = 300
            self.my_ball.delta_x = 0
            self.my_ball.delta_y = 0       
            global score_1 
            score_1 = score_1 + 1
        
            

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        #de beweging voor de paddles
        if key == arcade.key.UP and self.my_paddle2.y < SCREEN_HEIGHT - self.my_paddle2.height/2:
            self.my_paddle2.delta_y = 10
        if key == arcade.key.DOWN and self.my_paddle2.y > 0 + self.my_paddle2.height/2:
            self.my_paddle2.delta_y = -10
        if key == arcade.key.W and self.my_paddle.y < SCREEN_HEIGHT - self.my_paddle.height/2:
            self.my_paddle.delta_y = 10
        if key == arcade.key.S and self.my_paddle.y > 0 + self.my_paddle.height/2:
            self.my_paddle.delta_y = -10
        #druk op spatie om het spel te starten
        if key == arcade.key.SPACE and self.my_ball.delta_x == 0 and self.my_ball.delta_y == 0:
            self.my_ball.delta_x = 5
            self.my_ball.delta_y = 5
            global text_color
            text_color = arcade.color.JAPANESE_INDIGO
        


    def on_key_release(self, key, key_modifiers):
        #als je de toets loslaat van het bewegen stopt de paddle met bewegen
        if key == arcade.key.UP:
            self.my_paddle2.delta_y = 0
        if key == arcade.key.DOWN:
            self.my_paddle2.delta_y = 0
        if key == arcade.key.W:
            self.my_paddle.delta_y = 0
        if key == arcade.key.S:
            self.my_paddle.delta_y = 0



def main():
    """ Main method """
    #run de game
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

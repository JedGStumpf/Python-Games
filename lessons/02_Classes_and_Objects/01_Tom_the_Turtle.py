""" Turtle in Pygame

We really miss the turtle module from Python's standard library. It was a great
way to introduce programming, so let's make something similar in PyGame, using
objects. 

"""
import math

import pygame


def event_loop():
    """Wait until user closes the window"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


class Turtle:
    def __init__(self, screen, x: int, y: int):
        self.x = x
        self.y = y
        self.screen = screen
        self.angle = 0  # Angle in degrees, starting facing right

    def forward(self, distance, color):
        # Calculate new position based on current angle
        radian_angle = math.radians(self.angle)

        start_x = self.x  # Save the starting position
        start_y = self.y

        # Calculate the new position displacement
        dx = math.cos(radian_angle) * distance
        dy = math.sin(radian_angle) * distance

        # Update the turtle's position
        self.x += dx
        self.y -= dy

        # Draw line to the new position
        pygame.draw.line(self.screen, color, (start_x, start_y), (self.x, self.y), 2)

    def turn(self, angle: int, right_turn: bool = False):
        """
        Turns the turtle left by default.
        Set right_turn to True to turn Right
        """
        # Turn left by adjusting the angle counterclockwise

        
        if right_turn and self.angle > 0:
            self.angle = ((self.angle + angle) % 360)*-1
        else:
            self.angle = (self.angle + angle) % 360



class NewTurtle(Turtle):
    def __init__(self, screen, x: int, y: int, color: tuple = black):
        super().__init__(screen, x, y)
        self.color = color

    def forward(self, distance: int, color: tuple):
        return super().forward(distance, self.color)
    
    def penup(self, no_draw: bool = False):
        if no_draw:
            self.color = white
        else:
            self.color = red
    
    def get_x_and_y(self):
        print(f'X: {self.x}   Y: {self.y}')



# Main loop

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Turtle Style Drawing")



screen.fill(white)
turtle = NewTurtle(screen, screen.get_width() // 2, screen.get_height() // 2, red)  # Start at the center of the screen
print(turtle.color)
# Draw a square using turtle-style commands
for x in range(9):

    turtle.forward(100, red)  # Move forward by 100 pixels
    if x % 3 == 0:
        turtle.turn(90, True)    # Turn left by 90 degrees
        turtle.penup(True)
    else:
        turtle.turn(90)
        turtle.penup(False)
    turtle.get_x_and_y()
    # print(turtle.color)




    


    

    

















# Display the drawing
pygame.display.flip()

# Wait to quit
event_loop()

# Quit Pygame
pygame.quit()

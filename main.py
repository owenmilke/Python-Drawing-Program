"""
Python Drawing Program
Owen Milke
CS021 F
Program that allows the user to draw on a canvas with various
brush colors and sizes and save the file as a .png.
"""

# Imports
from brush import *
from button import *

# Canvas setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Drawing Program")
screen.fill(BACKGROUND_COLOR)
drawing_location = pygame.Rect((0, 0), (WIDTH, HEIGHT - TOOLBAR_HEIGHT))
toolbar_location = pygame.draw.rect(screen, TOOLBAR_COLOR,
                                    pygame.Rect((0, HEIGHT - TOOLBAR_HEIGHT), (WIDTH, TOOLBAR_HEIGHT)))

# Button setup
button_y = HEIGHT - TOOLBAR_HEIGHT / 2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, ORANGE),
    Button(190, button_y, 50, 50, YELLOW),
    Button(250, button_y, 50, 50, GREEN),
    Button(310, button_y, 50, 50, BLUE),
    Button(370, button_y, 50, 50, INDIGO),
    Button(430, button_y, 50, 50, VIOLET),
    Button(490, button_y, 50, 50, WHITE, "Small", BLACK),
    Button(550, button_y, 50, 50, WHITE, "Med", BLACK),
    Button(610, button_y, 50, 50, WHITE, "Large", BLACK),
    Button(670, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(730, button_y, 50, 50, WHITE, "Clear", BLACK),
    Button(790, button_y, 50, 50, WHITE, "Save", BLACK)
]

# Starting brush variables
brush_color = BLACK
previous_color = brush_color
brush_size = SMALL

# Loop setup
running = True
clock = pygame.time.Clock()


if __name__ == "__main__":
    while running:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()

        # Adds buttons to toolbar
        for button in buttons:
            button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quits the program
                running = False
            if pygame.mouse.get_pressed()[0]:
                if drawing_location.collidepoint(pos):
                    # Draws on the canvas when the left mouse button is pressed
                    x, y = pos
                    brush(screen, brush_color, x, y, brush_size)
                if toolbar_location.collidepoint(pos):
                    # Determines what the effect of the clicked button is
                    for button in buttons:
                        if button.clicked():
                            # If there is no button text; brush color changed to button color
                            previous_color = brush_color
                            brush_color = button.color
                            if button.text == "Small":
                                # Changes brush size to small
                                brush_size = SMALL
                                brush_color = previous_color
                            if button.text == "Med":
                                # Chagnes brush size to medium
                                brush_size = MED
                                brush_color = previous_color
                            if button.text == "Large":
                                # Changs brush size to large
                                brush_size = LARGE
                                brush_color = previous_color
                            if button.text == "Clear":
                                # Clears the canvas
                                screen.fill(WHITE, drawing_location)
                                brush_color = previous_color
                            if button.text == "Save":
                                # Saves the canvas to a .png file
                                if file_number < 10:
                                    file_name = "drawing0" + str(file_number) + ".png"
                                else:
                                    file_name = "drawing" + str(file_number) + ".png"
                                file_number += 1
                                image = screen.subsurface(drawing_location)
                                pygame.image.save(image, "drawings/" + file_name)
                                brush_color = previous_color
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Quits the program
                    running = False

        pygame.display.flip()

    pygame.quit()

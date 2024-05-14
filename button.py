from settings import *

pygame.init()


class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        """
        :param x: x-coordinate of the button
        :param y: y-coordinate of the button
        :param width: width of the button
        :param height: height of the button
        :param color: color of the button
        :param text: optional text the button can have
        :param text_color: text color for optional text
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

        # Colision for button
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self, surface):
        """
        :param surface: screen for button to be drawn onto
        :return: a unique button
        """
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 2)

        if self.text:
            # Text variables for if text is utilized on a button
            button_font = pygame.font.SysFont("Arial", 15)
            text_surface = button_font.render(self.text, True, self.text_color)
            surface.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2,
                                        self.y + self.height / 2 - text_surface.get_height() / 2))

    def clicked(self):
        # Determines if a button has been clicked
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pos):
                return True
        return False

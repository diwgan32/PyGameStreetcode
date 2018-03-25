import pygame
import collections

Point = collections.namedtuple('Point', 'x y')

class Sprite:
    def __init__(self, x, y, width, height, color, uuid):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._velocity = [0, 0]
        self._uuid = uuid

    def get_next_frame_bounding_box(self):
        return [self._x + self._width/2.0 + self._velocity[0],
                self._y + self._height/2.0 + self._velocity[1],
                self._width,
                self._height]

    def get_current_frame_bounding_box(self):
        return [self._x + self._width/2.0,
                self._y + self._height/2.0,
                self._width,
                self._height]

    def uuid(self):
        return self._uuid

    def move(self, velocity):
        self._velocity[0] += velocity[0]
        self._velocity[1] += velocity[1]

    def reset_velocity(self):
        self._velocity = [0, 0]

    def set_velocity(self, velocity):
        self._velocity = [velocity[0], velocity[1]]

    def apply_velocity(self):
        self._x += self._velocity[0]
        self._y += self._velocity[1]
        self.reset_velocity()

    def get_position(self):
        return Point(x = self._x + self._width/2.0 + self._velocity[0], \
                     y = self._y + self._height/2.0 + self._velocity[1])


class Rectangle(Sprite):
    def __init__(self, x, y, width, height, color, uuid):
        Sprite.__init__(self, x, y, width, height, color, uuid)

    def draw(self, screen):
        pygame.draw.rect(screen, self._color,
                         pygame.Rect([self._x, self._y, self._width, self._height]))


class Circle(Sprite):
    def __init__(self, x, y, radius, color, uuid):
        Sprite.__init__(self, x - radius, y - radius, radius * 2,
                        radius * 2, color, uuid)
        self._radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self._color,
                           (int(self._x + self._radius), int(self._y + self._radius)), self._radius)

    def get_position(self):
        return Point(x = self._x + self._velocity[0], y = self._y + self._velocity[1])

class Text(Sprite):
    def __init__(self, x, y, text, color, uuid, font, size):
        Sprite.__init__(self, x, y, 0, 0, color, uuid)
        self._font = pygame.font.Font('/Library/Fonts/' + font + '.ttf', size)
        self._text = text

    def set_text(self, text):
        self._text = text

    def get_text(self, text):
        return self._text

    def draw(self, screen):
        textsurface = self._font.render(self._text, True, self._color)
        screen.blit(textsurface, (self._x, self._y))

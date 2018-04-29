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
        self._next_move = [0, 0]
        self._uuid = uuid

    def get_next_frame_bounding_box(self):
        return [self._x + self._width/2.0 + self._velocity[0] + self._next_move[0],
                self._y + self._height/2.0 + self._velocity[1] + self._next_move[1],
                self._width,
                self._height]

    def get_current_frame_bounding_box(self):
        return [self._x + self._width/2.0,
                self._y + self._height/2.0,
                self._width,
                self._height]

    def uuid(self):
        return self._uuid

    def move(self, vector):
        self._next_move[0] += vector[0]
        self._next_move[1] += vector[1]

    def set_velocity(self, velocity):
        self._velocity = [velocity[0], velocity[1]]

    def get_velocity(self):
        return Point(x = self._velocity[0], y = self._velocity[1])

    def apply_velocity(self):
        self._x += self._next_move[0] + self._velocity[0]
        self._y += self._next_move[1] + self._velocity[1]
        self._next_move = [0, 0]

    def get_position(self):
        return Point(x = self._x + self._velocity[0] + self._next_move[0], \
                     y = self._y + self._velocity[1] + self._next_move[1])

    def set_position(self, new_pos):
        self._x = new_pos[0]
        self._y = new_pos[1]

    def x(self):
        return self.get_position().x

    def y(self):
        return self.get_position().y

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        self._color = new_color


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

    def get_position(self):
        return Point(x = self._x + self._radius + self._velocity[0] + self._next_move[0], \
                     y = self._y + self._radius + self._velocity[1] + self._next_move[1])

    def set_position(self, new_pos):
        self._x = new_pos[0] - self._radius
        self._y = new_pos[1] - self._radius


    def draw(self, screen):
        pygame.draw.circle(screen, self._color,
                           (int(self._x + self._radius), int(self._y + self._radius)), self._radius)

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

class Image(Sprite):
    def __init__(self, x, y, image, uuid, transparant=True):
        self._transparant = True
        self.set_image(image)
        Sprite.__init__(
            self,
            x, y,
            self._image.get_width(),
            self._image.get_height(),
            None, uuid)

    def set_image(self, image):
        self._image = pygame.image.load('../resources/Sprites/'+image)
        if self._transparant:
            col = self._image.get_at((0, self._image.get_height()-1))
            self._image.set_colorkey((col.r, col.g, col.b))
        else:
            self._image.set_colorkey(None)

    def draw(self, screen):
        screen.blit(self._image, (self._x, self._y))

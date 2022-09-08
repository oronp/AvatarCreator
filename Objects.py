DEFAULT_COLOR = 'white'
DEFAULT_SHAPE = [1000, 1000]
IMAGES_DIR = '/images'


class Background:

    def __init__(self, color=DEFAULT_COLOR, shape=DEFAULT_SHAPE, location=IMAGES_DIR, name=''):
        self.color = color
        self.shape = shape
        self.location = location
        self.name = name


class Arms:

    def __init__(self, color=DEFAULT_COLOR, location=IMAGES_DIR, name=''):
        self.color = color
        self.location = location
        self.name = name


class Shirt:

    def __init__(self, color=DEFAULT_COLOR, location=IMAGES_DIR, name=''):
        self.color = color
        self.location = location
        self.name = name


class Legs:

    def __init__(self, color=DEFAULT_COLOR, location=IMAGES_DIR, name=''):
        self.color = color
        self.location = location
        self.name = name


class Head:

    def __init__(self, color=DEFAULT_COLOR, location=IMAGES_DIR, name=''):
        self.color = color
        self.location = location
        self.name = name


class Pants:

    def __init__(self, color=DEFAULT_COLOR, location=IMAGES_DIR, name=''):
        self.color = color
        self.location = location
        self.name = name
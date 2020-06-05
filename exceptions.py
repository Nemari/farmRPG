import pygame
def except_import():
    try:
        import pygame
    except ImportError:
        pass

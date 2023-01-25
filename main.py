import pygame as pg
import cv2

class Convertisseur:
    def __init__(self, chemin='img/HandsomeSquidward.jpg'):
        pg.init()
        self.chemin = chemin
        self.image = cv2.imread(self.chemin)
        self.RESOLUTION = self.larg, self.haut = self.image.shape[0], self.image.shape[1]
        self.surface = pg.display.set_mode(self.RESOLUTION)
        self.horloge = pg.time.Clock()

    def prendre_image(self):
        pass

    def dessiner(self):
        pg.surfarray.blit_array(self.surface, self.image)
        cv2.imshow('img', self.image)

    def execute(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()
            self.dessiner()
            pg.display.set_caption(str(self.horloge.get_fps()))
            self.horloge.tick()

if __name__ == '__main__':
    app = Convertisseur()
    app.execute()
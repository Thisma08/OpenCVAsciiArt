import pygame as pg
import cv2

class Convertisseur:
    def __init__(self, chemin='img/HandsomeSquidward.jpg'):
        pg.init()
        self.chemin = chemin
        self.image = self.prendre_image()
        self.RESOLUTION = self.larg, self.haut = self.image.shape[0], self.image.shape[1]
        self.surface = pg.display.set_mode(self.RESOLUTION)
        self.horloge = pg.time.Clock()

    def prendre_image(self):
        self.cv2_image = cv2.imread(self.chemin)
        image_transposee = cv2.transpose(self.cv2_image)
        image_rgb = cv2.cvtColor(image_transposee, cv2.COLOR_RGB2BGR)
        return image_rgb

    def dessiner_cv2_image(self):
        cv2_image_redim = cv2.resize(self.cv2_image, (640, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow('img', cv2_image_redim)

    def dessiner(self):
        pg.surfarray.blit_array(self.surface, self.image)
        self.dessiner_cv2_image()

    def execute(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()
            self.dessiner()
            pg.display.set_caption(str(self.horloge.get_fps()))
            pg.display.flip()
            self.horloge.tick()

if __name__ == '__main__':
    app = Convertisseur()
    app.execute()

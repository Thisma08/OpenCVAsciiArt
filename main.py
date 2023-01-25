import pygame as pg
import cv2

class Convertisseur:
    def __init__(self, chemin='img/cat.jpg', taille_police=12):
        pg.init()
        self.chemin = chemin
        self.image = self.prendre_image()
        self.RESOLUTION = self.LARG, self.HAUT = self.image.shape[0], self.image.shape[1]
        self.surface = pg.display.set_mode(self.RESOLUTION)
        self.horloge = pg.time.Clock()

        self.CARS_ASCII = '.",:;!~+-xmo*#W&8@'
        self.COEFF_ASCII = 255//(len(self.CARS_ASCII)-1)

        self.police = pg.font.SysFont('Courier', taille_police, bold=True)
        self.ETAPE_CARS = int(taille_police * 0.6)
        self.CARS_ASCII_RENDUS = [self.police.render(car, False, 'white') for car in self.CARS_ASCII]


    def dessiner_image_convertie(self):
        indices_cars = self.image // self.COEFF_ASCII
        for x in range(0, self.LARG, self.ETAPE_CARS):
            for y in range(0, self.HAUT, self.ETAPE_CARS):
                indice_car = indices_cars[x, y]
                if indice_car:
                    self.surface.blit(self.CARS_ASCII_RENDUS[indice_car], (x, y))

    def prendre_image(self):
        self.cv2_image = cv2.imread(self.chemin)
        image_transposee = cv2.transpose(self.cv2_image)
        image_grise = cv2.cvtColor(image_transposee, cv2.COLOR_BGR2GRAY)
        return image_grise

    def dessiner_cv2_image(self):
        cv2_image_redim = cv2.resize(self.cv2_image, (640, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow('img', cv2_image_redim)

    def dessiner(self):
        self.surface.fill('black')
        self.dessiner_image_convertie()
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

import pygame as pg
import numpy as np
import cv2

class Convertisseur:
    def __init__(self, chemin='img/cat.jpg', taille_police=12, niv_couleur=8):
        pg.init()
        self.chemin = chemin
        self.NIV_COULEUR = niv_couleur
        self.image, self.image_grise = self.prendre_image()
        self.RESOLUTION = self.LARG, self.HAUT = self.image.shape[0], self.image.shape[1]
        self.surface = pg.display.set_mode(self.RESOLUTION)
        self.horloge = pg.time.Clock()

        self.CARS_ASCII = ' ixzao*#MW&8%B@$'
        self.COEFF_ASCII = 255//(len(self.CARS_ASCII)-1)

        self.police = pg.font.SysFont('Courier', taille_police, bold=True)
        self.ESPACEMENT_CARS = int(taille_police * 0.6)
        self.PALETTE, self.COEFF_COULEUR = self.creer_palette()

    def dessiner_image_convertie(self):
        indices_cars = self.image_grise // self.COEFF_ASCII
        indices_couleurs = self.image // self.COEFF_COULEUR
        for x in range(0, self.LARG, self.ESPACEMENT_CARS):
            for y in range(0, self.HAUT, self.ESPACEMENT_CARS):
                indice_car = indices_cars[x, y]
                if indice_car:
                    car = self.CARS_ASCII[indice_car]
                    couleur = tuple(indices_couleurs[x, y])
                    self.surface.blit(self.PALETTE[car][couleur], (x, y))

    def creer_palette(self):
        couleurs, coeff_couleur = np.linspace(0, 255, num=self.NIV_COULEUR, dtype=int, retstep=True)
        palette_couleur = [np.array([r, g, b]) for r in couleurs for g in couleurs for b in couleurs]
        palette = dict.fromkeys(self.CARS_ASCII, None)
        coeff_couleur = int(coeff_couleur)
        for car in palette:
            palette_cars = {}
            for couleur in palette_couleur:
                cle_couleur = tuple(couleur // coeff_couleur)
                palette_cars[cle_couleur] = self.police.render(car, False, tuple(couleur))
            palette[car] = palette_cars
        return palette, coeff_couleur

    def prendre_image(self):
        self.cv2_image = cv2.imread(self.chemin)
        image_transposee = cv2.transpose(self.cv2_image)
        image = cv2.cvtColor(image_transposee, cv2.COLOR_BGR2RGB)
        image_grise = cv2.cvtColor(image_transposee, cv2.COLOR_BGR2GRAY)
        return image, image_grise

    def dessiner_cv2_image(self):
        cv2_image_redim = cv2.resize(self.cv2_image, (640, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow('img', cv2_image_redim)

    def dessiner(self):
        self.surface.fill('black')
        self.dessiner_image_convertie()
        self.dessiner_cv2_image()

    def sauvegarder(self):
        img_pg = pg.surfarray.array3d(self.surface)
        img_cv2 = cv2.transpose(img_pg)
        cv2.imwrite('output/img/converted_image.jpg', img_cv2)
        print("Image sauvegardée")

    def execute(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()
                elif e.type == pg.KEYDOWN:
                    if e.key == pg.K_s:
                        self.sauvegarder()
            self.dessiner()
            pg.display.set_caption(str(self.horloge.get_fps()))
            pg.display.flip()
            self.horloge.tick()

if __name__ == '__main__':
    app = Convertisseur()
    app.execute()

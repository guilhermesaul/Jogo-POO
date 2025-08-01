import pygame
import os

pygame.init()
pygame.font.init()

class Hud:
    def __init__(self):
        self.mostrar = False
        self.mensagem = "100"
        self.tamanho = 40
        self.cor = (0, 0, 0)
        self.fonte = pygame.font.SysFont("arial", self.tamanho, True)
        self.texto_formatado = self.fonte.render(self.mensagem, True, self.cor)
        self.municao = "| 12 munições"
        self.texto_munição = self.fonte.render(self.municao, True, self.cor)
        
    def exibe_vida(self, tela):
        self.caminho = os.path.join(os.path.dirname(__file__), "..", "data", "images", "hud", "coracao1.png")
        self.imagem = pygame.image.load(self.caminho)
        self.imagem = pygame.transform.scale(self.imagem, (16*2.75, 16*2.75))
        tela.blit(self.imagem, (940, 22.5))
        return self.texto_formatado
    
    def exibe_fome(self, tela):
        self.caminho = os.path.join(os.path.dirname(__file__), "..", "data", "images", "hud", "fome1.png")
        self.imagem = pygame.image.load(self.caminho)
        self.imagem = pygame.transform.scale(self.imagem, (16*2, 16*2))
        tela.blit(self.imagem, (1065, 30))
        return self.texto_formatado
    
    def exibe_sede(self, tela):
        self.caminho = os.path.join(os.path.dirname(__file__), "..", "data", "images", "hud", "sede1.png")
        self.imagem = pygame.image.load(self.caminho)
        self.imagem = pygame.transform.scale(self.imagem, (16*2.75, 16*2.75))
        tela.blit(self.imagem, (1160, 21))
        return self.texto_formatado
    
    def exibir_arma(self, tela, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    self.mostrar = not self.mostrar
        if self.mostrar:
            self.caminho = os.path.join(os.path.dirname(__file__), "..", "data", "images", "glock.png")
            self.imagem = pygame.image.load(self.caminho)
            self.imagem = pygame.transform.scale(self.imagem, (32*2, 32*2))
            tela.blit(self.imagem, (70, 20))
            tela.blit(self.texto_munição, (140, 25))
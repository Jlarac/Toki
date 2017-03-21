import pygame
import funciones

SCREEN_SIZE = screen_width, screen_height = 1200, 600

class boton(object):	
	def __init__(self, img1,img2,h,l):
		self.imgn=img1
		self.imgs=img2
		self.imga=self.imgn
		self.rect=self.imga.get_rect()
		self.rect.left,self.rect.top=(h,l)

	def update(self,screen,cursor):
		if cursor.colliderect(self.rect):
			self.imga=self.imgs
		else: self.imga=self.imgn

		screen.blit(self.imga,self.rect)

fuente="./fonts/DejaVuSerif.ttf"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DODGER_BLUE = (30, 144, 255)
STEEL_BLUE = (70, 130, 180)
RED=(255,0,0)
GREEN=(0,255,0)
other=(234,115,94)
#######################################################Valores############################################################## 
xm=ym=fg=centx=centy=st=0.0
tg=1.0
xy_cor = [400,300]
centx=xy_cor[0]
centy=xy_cor[1]
###############################################Imagenes##################################################
checkb=pygame.image.load("./icons/bien.png")
checka=pygame.image.load("./icons/bien(1).png")
warningr=pygame.image.load("./icons/mal(1).png")
uvlogo=pygame.image.load("./icons/Logo-UV2.jpg")
cirmenosb=pygame.image.load("./icons/circle.png")
cirmenosa=pygame.image.load("./icons/circle (1).png")
cirmasb=pygame.image.load("./icons/technology.png")
cirmasa=pygame.image.load("./icons/technology (1).png")

fondoneg=pygame.image.load("./icons/fondoneg.jpg")
gris=pygame.image.load("./icons/color_gris.jpg")

connect=pygame.image.load("./icons/wifi-llena.png")
unconnect=pygame.image.load("./icons/wifi-llena (1).png")

buv=boton(uvlogo,uvlogo,450,75)

bcone=boton(connect,connect,1132,2)
bucone=boton(unconnect,unconnect,1132,2)

bmasgnr=boton(cirmasb,cirmasa,1075,70)
bmenosgnr=boton(cirmenosb,cirmenosa,1075,90)

bwarncoor=boton(warningr,warningr,1130,430)
bacepbz=boton(checkb,checka,1130,430)

bacepcf=boton(checkb,checka,1130,430)
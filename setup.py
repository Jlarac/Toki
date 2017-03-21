#!/usr/bin/env python

import time, math, pygame,string,socket,os,threading
from pygame.locals import *
import variables 
import funciones
import cininv

global UDP_PORTs,UDP_IPs,socks,UDP_IPe,socke,stcon 
stcheck=1
stcon=1

class comunication(object):
	def connect(self):
		print "[Hilo]: Encendido"
		global UDP_PORTs,UDP_IPs,socks,UDP_IPe,socke,stcon
		while True:
			self.mensaje(0,[UDP_IPs,0,0,0,0],UDP_PORTs,UDP_IPe,socks)
			socke.settimeout(2.0)
			try:
				data, addr = socke.recvfrom(1024)
				#print data
				cuenta=0
				mensaje_entrada=["","","","","",""]
				if data!="":
					for i in range(len(data)):
						if data[i]==":":
							cuenta+=1
						else:
							mensaje_entrada[cuenta]+=data[i]
					if mensaje_entrada[0]=="1":
						stcon=0
					elif mensaje_entrada[0]=="8":
						print mns, a13, a23,a33,a43,a53
					elif mensaje_entrada[0]=="9":
						break
			except socket.timeout:
				stcon=1
		print "[Hilo]: Apagado"

	def mensaje(self,st,a,UDP_PORTs,UDP_IPe,socks):
		MESSAGE = str(st)+":"+str(a[0])+":"+str(a[1])+":"+str(a[2])+":"+str(a[3])+":"+str(a[4])+":"
		socks.sendto(MESSAGE, (UDP_IPe, UDP_PORTs))

	def get_ip(self):
		s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		s.connect(("8.8.8.8",80))
		return s.getsockname()[0]

class text(object):
	def __init__(self,FontSize, FontName): 
		pygame.font.init()
		self.font=pygame.font.Font(FontName,FontSize)
		self.size=FontSize
	def render(self,surface,text,color,pos):
		text=unicode(text,"UTF-8")
		x,y=pos
		for i in text.split("\r"):
			surface.blit(self.font.render(i,1,color),(x,y))
			y += self.size

class cursor(pygame.Rect):
	def __init__(self): 
		pygame.Rect.__init__(self,0,0,1,1)

	def update(self):
		self.left,self.top=pygame.mouse.get_pos()

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
	
class toolbox(object):
	def updatefun(self,screen,message,xmss,ymss,xc,yc): 
		fontobject = pygame.font.Font("./fonts/DejaVuSerif.ttf",20)
		pygame.draw.rect(screen,variables.BLACK,[xmss,ymss,xc,yc])
		pygame.draw.rect(screen,variables.BLACK,[0,529,1000,71])
		chtext.render(screen,message,variables.WHITE,(xmss,ymss))
		chtext.render(screen,"Editando...  Salir con Enter",variables.WHITE,(10,530))
		pygame.display.flip()
	def update(self,screen,message,xmss,ymss):
		fontobject = pygame.font.Font("./fonts/DejaVuSerif.ttf",20)
		chtext.render(screen,message,variables.WHITE,(xmss,ymss))
	def fun(self,screen,xmss,ymss,xc,yc):
		pygame.font.init()
		current_string = []
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				inkey = event.key
				if inkey == K_BACKSPACE:
					current_string = current_string[0:-1]
				elif inkey == 13:
					break
				elif inkey == K_MINUS:
					current_string.append("-")
				elif inkey>47 and inkey<58:
					current_string.append(chr(inkey))
			tb.updatefun(screen,string.join(current_string,""),xmss,ymss,xc,yc)
		try:
			return int(string.join(current_string,""))
		except:
			return 0
	def funstring(self,screen,xmss,ymss,xc,yc):
		pygame.font.init()
		current_string = []
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				inkey = event.key
				if inkey == K_BACKSPACE:
					current_string = current_string[0:-1]
				elif inkey == 13:
					break
				elif inkey == K_MINUS:
					current_string.append("-")
				elif inkey>47 and inkey<58 or inkey==46:
					current_string.append(chr(inkey))
			tb.updatefun(screen,string.join(current_string,""),xmss,ymss,xc,yc)
		if string.join(current_string,"")=="":
			return "0.0.0.0"
		else:
			return string.join(current_string,"")

def bezier(screen,t,xant,yant,zant,aant,termx,termy,termz,a,l,ar,limangmy,limangmn,p): 			
	text3.render(screen,str("{0:.2f}".format(t*100))+"%",variables.WHITE,(5,60)) 
	text3.render(screen,"Posicion Anterior",variables.DODGER_BLUE,(50,100))
	text3.render(screen,"X: "+str(xant),variables.WHITE,(50,150))
	text3.render(screen,"Y: "+str(yant),variables.WHITE,(50,180))
	text3.render(screen,"Z: "+str(zant),variables.WHITE,(50,210))
	text3.render(screen,"Ang1: "+str("{0:.2f}".format(aant[0])),variables.WHITE,(75,250))
	text3.render(screen,"Ang2: "+str("{0:.2f}".format(aant[1])),variables.WHITE,(75,280))
	text3.render(screen,"Ang3: "+str("{0:.2f}".format(aant[2])),variables.WHITE,(75,310))
	text3.render(screen,"Ang4: "+str("{0:.2f}".format(aant[3])),variables.WHITE,(75,340))
	text3.render(screen,"Posicion Actual",variables.DODGER_BLUE,(400,100))
	text3.render(screen,"X: "+str(termx),variables.WHITE,(400,150))
	text3.render(screen,"Y: "+str(termy),variables.WHITE,(400,180))
	text3.render(screen,"Z: "+str(termz),variables.WHITE,(400,210))
	text3.render(screen,"Ang1: "+str("{0:.2f}".format(a[0])),variables.WHITE,(425,250))
	text3.render(screen,"Ang2: "+str("{0:.2f}".format(a[1])),variables.WHITE,(425,280))
	text3.render(screen,"Ang3: "+str("{0:.2f}".format(a[2])),variables.WHITE,(425,310))
	text3.render(screen,"Ang4: "+str("{0:.2f}".format(a[3])),variables.WHITE,(425,340))
	x,y,z,ar,p=funciones.cd(l,a,ar,limangmy,limangmn,p)
	pygame.draw.line(screen, variables.WHITE, p[0], p[1],3)
	pygame.draw.line(screen, variables.WHITE, p[1], p[2],3)
	pygame.draw.line(screen, variables.WHITE, p[2], p[3],3)
	pygame.draw.line(screen, variables.WHITE, p[3], p[4],3)
	pygame.draw.circle(screen, variables.DODGER_BLUE, (p[1]), 3)
	pygame.draw.circle(screen, variables.DODGER_BLUE, (p[2]), 3)
	pygame.draw.circle(screen, variables.DODGER_BLUE, (p[3]), 3)
	pygame.draw.circle(screen, variables.DODGER_BLUE, (p[4]), 3)
	pygame.draw.circle(screen, variables.GREEN, (p[5]), 5)

def ciclotrayectorias(screen,t,xant,yant,zant,aant,termx,termy,termz,a):
	chtext.render(screen,str("{0:.2f}".format(t*100))+"%",variables.WHITE,(205,60)) 
	chtext.render(screen,"Posicion Anterior",variables.DODGER_BLUE,(250,100))
	chtext.render(screen,"X: "+str(xant),variables.WHITE,(250,150))
	chtext.render(screen,"Y: "+str(yant),variables.WHITE,(250,180))
	chtext.render(screen,"Z: "+str(zant),variables.WHITE,(250,210))
	chtext.render(screen,"Ang1: "+str("{0:.2f}".format(aant[0])),variables.WHITE,(275,250))
	chtext.render(screen,"Ang2: "+str("{0:.2f}".format(aant[1])),variables.WHITE,(275,280))
	chtext.render(screen,"Ang3: "+str("{0:.2f}".format(aant[2])),variables.WHITE,(275,310))
	chtext.render(screen,"Ang4: "+str("{0:.2f}".format(aant[3])),variables.WHITE,(275,340))
	chtext.render(screen,"Posicion Actual",variables.DODGER_BLUE,(600,100))
	chtext.render(screen,"X: "+str(termx),variables.WHITE,(600,150))
	chtext.render(screen,"Y: "+str(termy),variables.WHITE,(600,180))
	chtext.render(screen,"Z: "+str(termz),variables.WHITE,(600,210))
	chtext.render(screen,"Ang1: "+str("{0:.2f}".format(a[0])),variables.WHITE,(625,250))
	chtext.render(screen,"Ang2: "+str("{0:.2f}".format(a[1])),variables.WHITE,(625,280))
	chtext.render(screen,"Ang3: "+str("{0:.2f}".format(a[2])),variables.WHITE,(625,310))
	chtext.render(screen,"Ang4: "+str("{0:.2f}".format(a[3])),variables.WHITE,(625,340))

def dibujobrazo(screen,a,l,ar,limangmy,limangmn,p):
	x,y,z,ar,p=funciones.cd(l,a,ar,limangmy,limangmn,p)
	pygame.draw.line(screen, variables.WHITE, p[0], p[1],3)
	pygame.draw.line(screen, variables.WHITE, p[1], p[2],3)
	pygame.draw.line(screen, variables.WHITE, p[2], p[3],3)
	pygame.draw.line(screen, variables.WHITE, p[3], p[4],3)
	pygame.draw.circle(screen, variables.DODGER_BLUE, (p[1]), 3)
	pygame.draw.circle(screen, variables.DODGER_BLUE, (p[2]), 3)
	pygame.draw.circle(screen, variables.DODGER_BLUE, (p[3]), 3)
	pygame.draw.circle(screen, variables.DODGER_BLUE, (p[4]), 3)
	pygame.draw.circle(screen, variables.GREEN, (p[5]), 5)

def grid(screen):
	y=0 
	for i in range(12):
		x=0
		for ii in range(26):
			xchtext.render(screen,"("+str(x)+","+str(y)+")",variables.WHITE,(x,y))
			x+=50
		y+=50

	y=50
	for i in range(12):
		pygame.draw.line(screen, variables.WHITE, (0,y), (1200,y),1)
		y+=50

	x=50
	for i in range(26):
		pygame.draw.line(screen, variables.WHITE, (x,0), (x,600),1)
		x+=50


def main():	
	global stcheck,UDP_PORTs,UDP_IPs,socks,UDP_IPe,socke,stcon
	pygame.init()	

	clock = pygame.time.Clock() 																		
	screen = pygame.display.set_mode(variables.SCREEN_SIZE) 	
	pygame.display.set_caption("Toki")

	UDP_IPe=""				
	UDP_PORTe=0
	UDP_IPs=""
	UDP_PORTs=0
	sft=xci=yci=zci=0
	stconfig=0
	l=[0,0,0,0]
	a=[0,0,0,0,0]
	am=[0,0,0,0,0]
	ar=[0,0,0,0,0]
	atemporal=[0,0,0,0,0]
	angr=[0,0,0,0,0]
	lamy=[0,0,0,0,0]
	lamn=[0,0,0,0,0]
	arad=[0,0,0,0,0]
	p=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
	comp=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	limangmy=[0,0,0,0,0]
	limangmn=[0,0,0,0,0]
	stdibujo=1
	termx=0
	termy=0
	termz=0
	xant=0
	yant=0
	zant=0
	aant=[0,0,0,0,0]
	dx=0
	dy=0
	dz=0
	rbz=0
	st=0
	lbp2=0
	seg=10
	lbp2,l,a,limangmy,limangmn,UDP_IPe, UDP_PORTe,UDP_IPs, UDP_PORTs=funciones.carconfig(lbp2,l,a,limangmy,limangmn,UDP_IPe, UDP_PORTe,UDP_IPs, UDP_PORTs)
	
	UDP_IPs=comunicacion.get_ip()
	socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 				
	socke = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	socke.bind(("0.0.0.0", UDP_PORTe))

	checkconnect=threading.Thread(target=comunicacion.connect) 				
	checkconnect.start()

	running = True
	while running: 		
		cursor1.update()									 
		for event in pygame.event.get():
			if event.type == QUIT:
				stcheck=2
				running=False
				comunicacion.mensaje(9,[0,0,0,0,0],UDP_PORTs,UDP_IPe,socks)
			try:
				if event.type == pygame.MOUSEBUTTONUP:
					if st!=0:
						if cursor1.colliderect(bcinematicas):
							st=1
						if cursor1.colliderect(btrayectorias):
							st=2
						if cursor1.colliderect(bconfiguracion):
							st=3
						if cursor1.colliderect(bacerca):
							st=4
						if cursor1.colliderect(bbezier1):
							st=10
							npunto=0
							n=0
						if cursor1.colliderect(bbezier2):
							st=11
							npunto=0
							n=0
						if cursor1.colliderect(bbeziertpred):
							st=14
					if st==1:
						if cursor1.colliderect(bang1):
							sft=1
						if cursor1.colliderect(bang2):
							sft=2
						if cursor1.colliderect(bang3):
							sft=3
						if cursor1.colliderect(bang4):
							sft=4
						if cursor1.colliderect(bang5):
							sft=5
						if cursor1.colliderect(bhome):
							a=[0,0,0,0,0]
						if cursor1.colliderect(bx):
							sft=6
						if cursor1.colliderect(by):
							sft=7
						if cursor1.colliderect(bz):
							sft=8
					if st==2:
						if cursor1.colliderect(bbezier3d):
							st=10
							npunto=0
							n=0
						if cursor1.colliderect(bbezier2d):
							st=11
							npunto=0
							n=0
						if cursor1.colliderect(bbezierpred):
							st=14
					if st==3:
						if cursor1.colliderect(bips):
							sft=1
						if cursor1.colliderect(bipe):
							sft=2
						if cursor1.colliderect(bports):
							sft=3
						if cursor1.colliderect(bporte):
							sft=4
						if cursor1.colliderect(variables.bacepcf.rect): 														
							print("[Setup]: Cambios guardados")
							r2=open('config.txt', 'w') 																		
							r2.write("a={}\n". format(int(l[0]))) 															
							r2.write("b={}\n". format(int(l[1])))
							r2.write("c={}\n". format(int(l[2])))
							r2.write("d={}\n". format(int(l[3])))
							r2.write("e={}\n". format(int(a[0])))
							r2.write("f={}\n". format(int(a[1])))
							r2.write("g={}\n". format(int(a[2])))
							r2.write("h={}\n". format(int(a[3])))
							r2.write("i={}\n". format(int(a[4])))
							r2.write("j={}\n". format(int(limangmy[0])))
							r2.write("k={}\n". format(int(limangmn[0])))
							r2.write("l={}\n". format(int(limangmy[1])))
							r2.write("m={}\n". format(int(limangmn[1])))
							r2.write("n={}\n". format(int(limangmy[2])))
							r2.write("o={}\n". format(int(limangmn[2])))
							r2.write("p={}\n". format(int(limangmy[3])))
							r2.write("q={}\n". format(int(limangmn[3])))
							r2.write("r={}\n". format(int(limangmy[4])))
							r2.write("s={}\n". format(int(limangmn[4])))
							r2.write("t={}\n". format(UDP_IPs))
							r2.write("u={}\n". format(UDP_IPe))
							r2.write("v={}\n". format(int(UDP_PORTs)))
							r2.write("w={}\n". format(int(UDP_PORTe)))
							r2.close()
							lbp2,l,a,limangmy,limangmn,UDP_IPs,UDP_IPe,UDP_PORTs,UDP_PORTe=funciones.carconfig(lbp2,l,a,limangmy,limangmn,UDP_IPe, UDP_PORTe,UDP_IPs, UDP_PORTs)
							funciones.mensaje(0,[UDP_IPe,0,0,0,0],UDP_PORTs,UDP_IPs,socks)
					if st==10:
						if cursor1.colliderect(variables.bacepbz.rect):
							st=12
							n=n-1

						if cursor1.colliderect(bnpuntos):
							sft=1
						if cursor1.colliderect(bmodx):
							sft=2
						if cursor1.colliderect(bmody):
							sft=3
						if cursor1.colliderect(bmodz):
							sft=4
						if cursor1.colliderect(bsegmentos):
							sft=5

						if npunto<=n and npunto>=0:
							if npunto==n:
								if cursor1.colliderect(variables.bmenosgnr.rect):
									npunto-=1
							if npunto==1:
								if cursor1.colliderect(variables.bmasgnr.rect):
									npunto+=1
							else:
								if cursor1.colliderect(variables.bmasgnr.rect):
									npunto+=1
								if cursor1.colliderect(variables.bmenosgnr.rect):
									npunto-=1
					if st==11:
						if cursor1.colliderect(variables.bacepbz.rect):
							st=13
							n=n-1

						if cursor1.colliderect(bnpuntos):
							sft=1

						if cursor1.colliderect(bmodx):
							sft=2

						if cursor1.colliderect(bmody):
							sft=3

						if cursor1.colliderect(bcentrox):
							sft=4

						if cursor1.colliderect(bcentroy):
							sft=5

						if cursor1.colliderect(bcentroz):
							sft=6

						if cursor1.colliderect(bradio):
							sft=7
						if cursor1.colliderect(bsegmentos):
							sft=8

						if npunto<=n and npunto>=0:
							if npunto==n:
								if cursor1.colliderect(variables.bmenosgnr.rect):
									npunto-=1
							elif npunto==1:
								if cursor1.colliderect(variables.bmasgnr.rect):
									npunto+=1
							else:
								if cursor1.colliderect(variables.bmasgnr.rect):
									npunto+=1
								if cursor1.colliderect(variables.bmenosgnr.rect):
									npunto-=1
			except:
				pass

		if stconfig==70:
			st=1
			lbp2=0

		screen.blit(variables.fondoneg,(0,0)) 																
		#screen.blit(variables.gris,(0,0))
		#grid(screen)

		if stcon==1: 																							
			variables.bucone.update(screen,cursor1)
		elif stcon==0:
			variables.bcone.update(screen,cursor1)

		if st!=0:
			pygame.draw.line(screen, variables.WHITE, (200,25), (200,575),2)

			bcinematicas=pygame.draw.rect(screen,variables.BLACK,[25,50,150,30])
			btrayectorias=pygame.draw.rect(screen,variables.BLACK,[25,100,150,30])
			bconfiguracion=pygame.draw.rect(screen,variables.BLACK,[25,220,150,30])
			bacerca=pygame.draw.rect(screen,variables.BLACK,[25,270,150,30])
			bbezier1=pygame.draw.rect(screen,variables.BLACK,[65,140,50,14])
			bbezier2=pygame.draw.rect(screen,variables.BLACK,[65,160,50,14])
			bbeziertpred=pygame.draw.rect(screen,variables.BLACK,[65,180,50,14])

			if cursor1.colliderect(bcinematicas):
				chtext.render(screen,"Cinematicas",variables.GREEN,(25,50))
			else:
				chtext.render(screen,"Cinematicas",variables.DODGER_BLUE,(25,50))
			if cursor1.colliderect(btrayectorias):
				chtext.render(screen,"Trayectorias",variables.GREEN,(25,100))
			else:
				chtext.render(screen,"Trayectorias",variables.DODGER_BLUE,(25,100))

			if cursor1.colliderect(bbezier1):
				xchtext.render(screen,"Bezier 3D",variables.GREEN,(65,140))
			else:
				xchtext.render(screen,"Bezier 3D",variables.DODGER_BLUE,(65,140))

			if cursor1.colliderect(bbezier2):
				xchtext.render(screen,"Bezier 2D",variables.GREEN,(65,160))
			else:
				xchtext.render(screen,"Bezier 2D",variables.DODGER_BLUE,(65,160))

			if cursor1.colliderect(bbeziertpred):
				xchtext.render(screen,"Predeterminadas",variables.GREEN,(65,180))
			else:
				xchtext.render(screen,"Predeterminadas",variables.DODGER_BLUE,(65,180))

			if cursor1.colliderect(bconfiguracion):
				chtext.render(screen,"Configuracion",variables.GREEN,(25,220))
			else:
				chtext.render(screen,"Configuracion",variables.DODGER_BLUE,(25,220))
			if cursor1.colliderect(bacerca):
				chtext.render(screen,"Acerca de...",variables.GREEN,(25,270))
			else:
				chtext.render(screen,"Acerca de...",variables.DODGER_BLUE,(25,270))
		if st==0:   #Inicio 
			variables.buv.update(screen,cursor1)															
			ltext.render(screen,"Interfaz de control para el brazo Toki-1",variables.WHITE,(200,0))
			ltext.render(screen,"Universidad Veracruzana",variables.WHITE,(10,550))
			stconfig+=1
		elif st==1:	#Menu cinematicas
			stconfig=0
			chtext.render(screen,"Cinematica directa:",variables.DODGER_BLUE,(215,75))
			chtext.render(screen,"Ang. 1:",variables.DODGER_BLUE,(250,100))
			chtext.render(screen,"Ang. 2:",variables.DODGER_BLUE,(250,125))
			chtext.render(screen,"Ang. 3:",variables.DODGER_BLUE,(250,150))
			chtext.render(screen,"Ang. 4:",variables.DODGER_BLUE,(250,175))
			chtext.render(screen,"Ang. 5:",variables.DODGER_BLUE,(250,200))
			
			x,y,z,ar,p=funciones.cd(l,a,ar,limangmy,limangmn,p)
			chtext.render(screen,"Posicion final:",variables.DODGER_BLUE,(500,100))
			chtext.render(screen,"X:  " + str("{0:.2f}".format(x)),variables.WHITE,(530,125))
			chtext.render(screen,"Y:  " + str("{0:.2f}".format(y)),variables.WHITE,(530,150))
			chtext.render(screen,"Z:  " + str("{0:.2f}".format(z)),variables.WHITE,(530,175))
			
			bang1=pygame.draw.rect(screen,variables.BLACK,[325,100,75,20])
			bang2=pygame.draw.rect(screen,variables.BLACK,[325,125,75,20])
			bang3=pygame.draw.rect(screen,variables.BLACK,[325,150,75,20])
			bang4=pygame.draw.rect(screen,variables.BLACK,[325,175,75,20])
			bang5=pygame.draw.rect(screen,variables.BLACK,[325,200,75,20])

			bhome=pygame.draw.rect(screen,variables.BLACK,[900,450,100,75])
			
			chtext.render(screen,"Cinematica inversa",variables.DODGER_BLUE,(215,350))
			chtext.render(screen,"X:",variables.DODGER_BLUE,(250,375))
			chtext.render(screen,"Y:",variables.DODGER_BLUE,(250,400))
			chtext.render(screen,"Z:",variables.DODGER_BLUE,(250,425))
			
			bx=pygame.draw.rect(screen,variables.BLACK,[275,375,75,20])
			by=pygame.draw.rect(screen,variables.BLACK,[275,400,75,20])
			bz=pygame.draw.rect(screen,variables.BLACK,[275,425,75,20])
			a1=a2=a3=a4=a5=0
			
			nxp=math.sqrt(pow(xci,2)+pow(yci,2))
			nyp=zci
			pd=(950+(int(nxp)*7),528-(int(nyp)*7))
			pygame.draw.circle(screen, variables.RED, (pd), 3)

			chtext.render(screen,"Valores de los angulos:",variables.DODGER_BLUE,(475,325))
			chtext.render(screen,"Ang. 1:  " + str("{0:.2f}".format(a[0])),variables.WHITE,(500,350))
			chtext.render(screen,"Ang. 2:  " + str("{0:.2f}".format(a[1])),variables.WHITE,(500,375))
			chtext.render(screen,"Ang. 3:  " + str("{0:.2f}".format(a[2])),variables.WHITE,(500,400))
			chtext.render(screen,"Ang. 4:  " + str("{0:.2f}".format(a[3])),variables.WHITE,(500,425))
			chtext.render(screen,"Ang. 5:  " + str("{0:.2f}".format(a[4])),variables.WHITE,(500,450))
			 
			pygame.draw.line(screen, variables.WHITE, p[0], p[1],3)
			pygame.draw.line(screen, variables.WHITE, p[1], p[2],3)
			pygame.draw.line(screen, variables.WHITE, p[2], p[3],3)
			pygame.draw.line(screen, variables.WHITE, p[3], p[4],3)
			pygame.draw.circle(screen, variables.DODGER_BLUE, (p[1]), 3)
			pygame.draw.circle(screen, variables.DODGER_BLUE, (p[2]), 3)
			pygame.draw.circle(screen, variables.DODGER_BLUE, (p[3]), 3)
			pygame.draw.circle(screen, variables.DODGER_BLUE, (p[4]), 3)
			pygame.draw.circle(screen, variables.GREEN, (p[5]), 5)

			if sft!=1:
				tb.update(screen,str("{0:.2f}".format(a[0])),340,100)
			if sft!=2:
				tb.update(screen,str("{0:.2f}".format(a[1])),340,125)
			if sft!=3:
				tb.update(screen,str("{0:.2f}".format(a[2])),340,150)
			if sft!=4:
				tb.update(screen,str("{0:.2f}".format(a[3])),340,175)
			if sft!=5:
				tb.update(screen,str("{0:.2f}".format(a[4])),340,200)
			if sft!=6:
				tb.update(screen,str("{0:.2f}".format(xci)),285,375)
			if sft!=7:
				tb.update(screen,str("{0:.2f}".format(yci)),285,400)
			if sft!=8:
				tb.update(screen,str("{0:.2f}".format(zci)),285,425)

			atemporal[0]=a[0]
			atemporal[1]=a[1]
			atemporal[2]=-a[2]
			atemporal[3]=-a[3]
			atemporal[4]=a[4]

			if am[2]!=0:
				am[2]=-am[2]
			if am[0]!=0:
				am[0]=-am[0]
			
			am=funciones.testep(atemporal)
			comunicacion.mensaje(1,[am[0],am[1],am[2],am[3],am[4]],UDP_PORTs,UDP_IPe,socks)

			if sft==1:
				a[0]=tb.fun(screen,340,100,75,20)
				sft=0
				stdibujo=1	
			elif sft==2:
				a[1]=tb.fun(screen,340,125,75,20)
				sft=0
				stdibujo=1	
			elif sft==3:
				a[2]=tb.fun(screen,340,150,75,20)
				sft=0
				stdibujo=1
			elif sft==4:
				a[3]=tb.fun(screen,340,175,75,20)
				sft=0
				stdibujo=1
			elif sft==5:
				a[4]=tb.fun(screen,340,200,75,20)
				sft=0
				stdibujo=1
			elif sft==6:
				xci=tb.fun(screen,285,375,75,20)
				sft=0	
				stdibujo=2
			elif sft==7:
				yci=tb.fun(screen,285,400,75,20)
				sft=0	
				stdibujo=2
			elif sft==8:
				zci=tb.fun(screen,285,425,75,20)
				sft=0
				stdibujo=2

			stcoor=0
			if (pow(xci,2)+pow(yci,2)+pow(zci,2))>(pow(l[1]+l[2]+l[3],2)) and stdibujo==2:
				variables.bwarncoor.update(screen,cursor1)
				chtext.render(screen,"No se pueden llevar a cabo dichas coordenadas: El punto es muy lejano",variables.WHITE,(10,530))
				stcoor=2
			elif zci<14 and stdibujo==2:
				variables.bwarncoor.update(screen,cursor1)
				chtext.render(screen,"No se pueden llevar a cabo dichas coordenadas: El punto esta muy debajo",variables.WHITE,(10,530))
				stcoor=2
			elif xci==0 and yci==0 and stdibujo==2:
				variables.bwarncoor.update(screen,cursor1)
				chtext.render(screen,"No se pueden llevar a cabo dichas coordenadas: Singularidad",variables.WHITE,(10,530))
				stcoor=2

			if stdibujo==2 and stcoor!=2:
				a=[0,0,0,0,0]
				arad,a,nxp,nyp=cininv.posf(l,xci,yci,zci,a,limangmy,limangmn)
				stdibujo+=1	
			pygame.draw.line(screen, variables.GREEN, (25,68), (150,68),2)
		elif st==2:	#Menu trayectorias
			bbezier3d=pygame.draw.rect(screen,variables.BLACK,[300,75,350,50])
			bbezier2d=pygame.draw.rect(screen,variables.BLACK,[300,150,550,50])
			bbezierpred=pygame.draw.rect(screen,variables.BLACK,[300,225,550,50])

			if cursor1.colliderect(bbezier3d):
				mtext.render(screen,"Bezier 3D Por Usuario",variables.GREEN,(300,75))
			else:
				mtext.render(screen,"Bezier 3D Por Usuario",variables.WHITE,(300,75))

			if cursor1.colliderect(bbezier2d):
				mtext.render(screen,"Bezier 2D y proyeccion Por Usuario",variables.GREEN,(300,150))
			else:
				mtext.render(screen,"Bezier 2D y proyeccion Por Usuario",variables.WHITE,(300,150))

			if cursor1.colliderect(bbezierpred):
				mtext.render(screen,"Trayectorias predeterminadas",variables.GREEN,(300,225))
			else:
				mtext.render(screen,"Trayectorias predeterminadas",variables.WHITE,(300,225))
			pygame.draw.line(screen, variables.GREEN, (25,118), (150,118),2)
		elif st==3:	#Menu configuracion
			chtext.render(screen,"Eslabones: "+ str(l),variables.DODGER_BLUE,(215,65))
			chtext.render(screen,"Angulos iniciales: "+ str(a),variables.DODGER_BLUE,(215,95))
			chtext.render(screen,"Angulos maximos: "+ str(limangmy),variables.DODGER_BLUE,(215,125))
			chtext.render(screen,"Angulos minimos:"+ str(limangmn),variables.DODGER_BLUE,(215,155))
			chtext.render(screen,"IP robot:",variables.DODGER_BLUE,(215,365))
			chtext.render(screen,"IP computador:",variables.DODGER_BLUE,(215,395))
			chtext.render(screen,"Puerto computador:",variables.DODGER_BLUE,(215,425))
			chtext.render(screen,"Puerto robot:",variables.DODGER_BLUE,(215,455))
			variables.bacepcf.update(screen,cursor1)

			for i in range(5):
				lamy[i]=angr=math.radians(limangmy[i])
				lamn[i]=angr=math.radians(limangmn[i])

			x,y,z=cininv.ang(l,a)
			x1,y1=cininv.distancias(l,a)

			trash1,trash2,x2my,y2my,trash3,trash4,trash5,trash6=cininv.distancias2(l,lamy[1],0,0)
			trash1,trash2,x2mn,y2mn,trash3,trash4,trash5,trash6=cininv.distancias2(l,lamn[1],0,0)
			trash1,trash2,trash3,trash4,x3my,y3my,trash5,trash6=cininv.distancias2(l,0,lamy[2],0)
			trash1,trash2,trash3,trash4,x3mn,y3mn,trash5,trash6=cininv.distancias2(l,0,lamn[2],0)
			trash1,trash2,trash3,trash4,trash5,trash6,x4my,y4my=cininv.distancias2(l,0,0,lamy[3])
			trash1,trash2,trash3,trash4,trash5,trash6,x4mn,y4mn=cininv.distancias2(l,0,0,lamn[3])	

			pinicio=(850,528)
			p1=(850-(int(x1[0])*7),528-(int(y1[0])*7))
			p2=(pinicio[0]+(int(x1[1])*7),pinicio[1]-(int(y1[1])*7))
			p3=(pinicio[0]+(int(x1[2])*7),pinicio[1]-(int(y1[2])*7))
			p4=(pinicio[0]+(int(x1[3])*7),pinicio[1]-(int(y1[3])*7))
			p2my=(pinicio[0]+(int(x2my)*7),pinicio[1]-(int(y2my)*7))
			p2mn=(pinicio[0]+(int(x2mn)*7),pinicio[1]-(int(y2mn)*7))
			p3my=(pinicio[0]+(int(x3my)*7),pinicio[1]-(int(y3my)*7))
			p3mn=(pinicio[0]+(int(x3mn)*7),pinicio[1]-(int(y3mn)*7))
			p4my=(pinicio[0]+(int(x4my)*7),pinicio[1]-(int(y4my)*7))
			p4mn=(pinicio[0]+(int(x4mn)*7),pinicio[1]-(int(y4mn)*7))

			pygame.draw.line(screen, variables.WHITE, pinicio, p1,3)
			pygame.draw.line(screen, variables.WHITE, p1, p2,3)
			pygame.draw.line(screen, variables.WHITE, p2, p3,3)
			pygame.draw.line(screen, variables.WHITE, p3, p4,3)
			pygame.draw.circle(screen, variables.BLACK, (pinicio), 3)
			pygame.draw.circle(screen, variables.BLACK, (p1), 3)
			pygame.draw.circle(screen, variables.BLACK, (p2), 3)
			pygame.draw.circle(screen, variables.BLACK, (p3), 3)
			pygame.draw.circle(screen, variables.GREEN, (p4), 3)
			pygame.draw.line(screen, variables.DODGER_BLUE, p1, p2my,3)
			pygame.draw.line(screen, variables.RED, p1, p2mn,3)
			pygame.draw.line(screen, variables.DODGER_BLUE, p2, p3my,3)
			pygame.draw.line(screen, variables.RED, p2, p3mn,3)
			pygame.draw.line(screen, variables.DODGER_BLUE, p3, p4my,3)
			pygame.draw.line(screen, variables.RED, p3, p4mn,3)
			pygame.draw.circle(screen, variables.BLACK, (p2my), 3)
			pygame.draw.circle(screen, variables.BLACK, (p2mn), 3)
			pygame.draw.circle(screen, variables.BLACK, (p3my), 3)
			pygame.draw.circle(screen, variables.BLACK, (p3mn), 3)
			pygame.draw.circle(screen, variables.BLACK, (p4my), 3)
			pygame.draw.circle(screen, variables.BLACK, (p4mn), 3)

			bips=pygame.draw.rect(screen,variables.BLACK,[425,365,175,25])
			bipe=pygame.draw.rect(screen,variables.BLACK,[425,395,175,25])
			bports=pygame.draw.rect(screen,variables.BLACK,[425,425,175,25])
			bporte=pygame.draw.rect(screen,variables.BLACK,[425,455,175,25])
			tb.update(screen,str(UDP_IPe),430,365)
			tb.update(screen,str(UDP_IPs),430,395)
			tb.update(screen,str(UDP_PORTs),430,425)
			tb.update(screen,str(UDP_PORTe),430,455)

			if sft==1:
				UDP_IPe=tb.funstring(screen,430,365,175,25)
				sft=0	
			elif sft==2:
				UDP_IPs=tb.funstring(screen,430,395,175,25)
				sft=0	
			elif sft==3:
				UDP_PORTs=tb.fun(screen,430,425,175,25)
				sft=0
			elif sft==4:
				UDP_PORTe=tb.fun(screen,430,455,175,25)
				sft=0
			pygame.draw.line(screen, variables.GREEN, (25,238), (160,238),2)
		elif st==4:	#Menu acerca de...

			chtext.render(screen,"Proyecto de Servicio Social Brazo Toki-1",variables.WHITE,(500,80))
			chtext.render(screen,"Alumno: Jairo Lara Cruz",variables.WHITE,(575,130))
			chtext.render(screen,"Academico: Dr. Jose Alejandro Vazquez Santacruz",variables.WHITE,(465,180))
			chtext.render(screen,"Universidad Veracruzana",variables.WHITE,(573,230))
			chtext.render(screen,"Modelo Hardware: Blue 5.0",variables.WHITE,(215,470))
			chtext.render(screen,"Modelo Software: Raptor 10.0",variables.WHITE,(215,500))
			pygame.draw.line(screen, variables.GREEN, (25,288), (150,288),2)
		elif st==10:#Menu Bezier 3D
			lbp3=0
			variables.bmasgnr.update(screen,cursor1)
			variables.bmenosgnr.update(screen,cursor1)

			chtext.render(screen,"Numero de Puntos: ",variables.WHITE,(215,70))
			chtext.render(screen,"Modificacion del punto: " + str(npunto),variables.WHITE,(800,70))
			chtext.render(screen,"Modificacion X: ",variables.WHITE,(800,140))
			chtext.render(screen,"Modificacion Y: ",variables.WHITE,(800,180))
			chtext.render(screen,"Modificacion Z: ",variables.WHITE,(800,220))

			chtext.render(screen,"Segmentos: ",variables.WHITE,(215,500))

			for i in range(n):
				chtext.render(screen,"Punto  "+str(i+1)+":     X= "+str(comp[i+1][0])+"  Y= "+str(comp[i+1][1])+"  Z= "+str(comp[i+1][2]),variables.WHITE,(210,100+(i*20)))

			bnpuntos=pygame.draw.rect(screen,variables.BLACK,[420,65,50,38])
			bmodx=pygame.draw.rect(screen,variables.BLACK,[960,135,50,38])
			bmody=pygame.draw.rect(screen,variables.BLACK,[960,175,50,38])
			bmodz=pygame.draw.rect(screen,variables.BLACK,[960,215,50,38])
			bsegmentos=pygame.draw.rect(screen,variables.BLACK,[340,485,50,38])
			tb.update(screen,str(n),420,71)
			tb.update(screen,str(seg),340,501)
			tb.update(screen,str(comp[npunto][0]),960,141)
			tb.update(screen,str(comp[npunto][1]),960,181)
			tb.update(screen,str(comp[npunto][2]),960,221)
			stcoor=0

			if (pow(comp[npunto][0],2)+pow(comp[npunto][1],2)+pow(comp[npunto][2],2))>(pow(l[1]+l[2]+l[3],2)):
				variables.bwarncoor.update(screen,cursor1)
				chtext.render(screen,"No se pueden llevar a cabo dichas coordenadas: El punto es muy lejano",variables.WHITE,(210,530))
				stcoor=2
			elif comp[npunto][2]<14:
				variables.bwarncoor.update(screen,cursor1)
				chtext.render(screen,"No se pueden llevar a cabo dichas coordenadas: El punto esta muy debajo",variables.WHITE,(210,530))
				stcoor=2
			elif comp[npunto][0]==0 and comp[npunto][1]==0:
				variables.bwarncoor.update(screen,cursor1)
				chtext.render(screen,"No se pueden llevar a cabo dichas coordenadas: Singularidad",variables.WHITE,(210,530))
				stcoor=2

			if stcoor!=2:
				variables.bacepbz.update(screen,cursor1)

			if sft==1:
				n=tb.fun(screen,420,71,50,38)
				sft=0	
			elif sft==2:
				comp[npunto][0]=tb.fun(screen,960,141,50,38)
				sft=0	
			elif sft==3:
				comp[npunto][1]=tb.fun(screen,960,181,50,38)
				sft=0
			elif sft==4:
				comp[npunto][2]=tb.fun(screen,960,221,50,38)
				sft=0
			elif sft==5:
				seg=tb.fun(screen,340,501,50,20)
				sft=0
			pygame.draw.line(screen, variables.GREEN, (65,150), (115,150),2)
		elif st==11:#Menu Bezier 2D
			lbp3=0
			variables.bmasgnr.update(screen,cursor1)
			variables.bmenosgnr.update(screen,cursor1)

			chtext.render(screen,"Numero de Puntos: ",variables.WHITE,(215,70))
			chtext.render(screen,"Modificacion del punto: " + str(npunto),variables.WHITE,(800,70))
			chtext.render(screen,"Modificacion X: ",variables.WHITE,(800,140))
			chtext.render(screen,"Modificacion Y: ",variables.WHITE,(800,180))

			for i in range(n):
				chtext.render(screen,"Punto  "+str(i+1)+":     X= "+str(comp[i+1][0])+"  Y= "+str(comp[i+1][1]),variables.WHITE,(210,100+(i*20)))

			bnpuntos=pygame.draw.rect(screen,variables.BLACK,[420,65,50,29])
			bmodx=pygame.draw.rect(screen,variables.BLACK,[960,135,50,29])
			bmody=pygame.draw.rect(screen,variables.BLACK,[960,175,50,29])
			bcentrox=pygame.draw.rect(screen,variables.BLACK,[850,315,50,29])
			bcentroy=pygame.draw.rect(screen,variables.BLACK,[850,345,50,29])
			bcentroz=pygame.draw.rect(screen,variables.BLACK,[850,375,50,29])
			bradio=pygame.draw.rect(screen,variables.BLACK,[850,490,50,29])

			chtext.render(screen,"Segmentos: ",variables.WHITE,(215,500))
			bsegmentos=pygame.draw.rect(screen,variables.BLACK,[340,485,50,38])
			tb.update(screen,str(seg),340,501)

			chtext.render(screen,"Centro de la esfera",variables.WHITE,(800,275))
			chtext.render(screen,"X: ",variables.WHITE,(825,315))
			chtext.render(screen,"Y: ",variables.WHITE,(825,345))
			chtext.render(screen,"Z: ",variables.WHITE,(825,375))
			chtext.render(screen,"Radio de la esfera",variables.WHITE,(800,450))
			chtext.render(screen,"R: ",variables.WHITE,(825,490))
			tb.update(screen,str(n),420,71)
			tb.update(screen,str(comp[npunto][0]),960,141)
			tb.update(screen,str(comp[npunto][1]),960,181)
			tb.update(screen,str(dx),850,315)
			tb.update(screen,str(dy),850,345)
			tb.update(screen,str(dz),850,375)
			tb.update(screen,str(rbz),850,490)

			stcoor=0
			if rbz<=13:
				variables.bwarncoor.update(screen,cursor1)
				chtext.render(screen,"No se pueden llevar a cabo dichas coordenadas: El radio es muy chico",variables.WHITE,(210,530))
				stcoor=2
			elif comp[npunto][0]==0 and comp[npunto][1]==0:
				variables.bwarncoor.update(screen,cursor1)
				chtext.render(screen,"No se pueden llevar a cabo dichas coordenadas: Singularidad",variables.WHITE,(210,530))
				stcoor=2

			if stcoor!=2:
				variables.bacepbz.update(screen,cursor1)

			if sft==1:
				n=tb.fun(screen,420,71,50,29)
				sft=0	
			elif sft==2:
				comp[npunto][0]=tb.fun(screen,960,141,50,29)
				sft=0	
			elif sft==3:
				comp[npunto][1]=tb.fun(screen,960,181,50,29)
				sft=0
			elif sft==4:
				dx=tb.fun(screen,850,315,50,29)
				sft=0	
			elif sft==5:
				dy=tb.fun(screen,850,345,50,29)
				sft=0
			elif sft==6:
				dz=tb.fun(screen,850,375,50,29)
				sft=0	
			elif sft==7:
				rbz=tb.fun(screen,850,490,50,29)
				sft=0
			elif sft==8:
				seg=tb.fun(screen,340,501,50,20)
				sft=0
			pygame.draw.line(screen, variables.GREEN, (65,170), (115,170),2)
		elif st==12:#Menu Trayectoria Bezier 3D Terminada
			resultado = funciones.trianguloPascal(n)
			h=len(resultado[n])
			step=1.0/seg
			finstep=1.0+step
			if lbp3==0:
				for t in cininv.frange(0.0,finstep,step):
					screen.blit(variables.fondoneg, (205, 0))
					st2=n
					for i in range(h):
						termx+=resultado[n][i]*pow(t,i)*pow((1-t),st2)*comp[i+1][0]
						termy+=resultado[n][i]*pow(t,i)*pow((1-t),st2)*comp[i+1][1]
						termz+=resultado[n][i]*pow(t,i)*pow((1-t),st2)*comp[i+1][2]
						st2-=1
					a=[0,0,0,0,0]
					arad,a,nxp1,nyp1=cininv.posf(l,int(termx),int(termy),int(termz),a,limangmy,limangmn)

					am=funciones.testep(a)
					#funciones.mensaje(1,[am[0],am[1],am[2],am[3],am[4]],UDP_PORTs,UDP_IPs,socks)

					xfr,yfr,zfr=cininv.ang(l,arad)
					#bezier(screen,t,xant,yant,zant,aant,termx,termy,termz,a,l,ar,limangmy,limangmn,p)
					ciclotrayectorias(screen,t,xant,yant,zant,aant,termx,termy,termz,a)
					dibujobrazo(screen,a,l,ar,limangmy,limangmn,p)
					print "******"
					print "t: " + str(t)
					print "-------------"
					print "Termx:  " + str(termx)
					print "Termy:  " + str(termy)
					print "Termz:  " + str(termz)
					print "Ang1:  " + str(a[0])
					print "Ang2:  " + str(a[1])
					print "Ang3:  " + str(a[2])
					print "Ang4:  " + str(a[3])
					pygame.display.flip()
					time.sleep(5)
					xant=termx
					yant=termy
					zant=termz
					for i in range(4):
						aant[i]=a[i]
					termx=termy=termz=0
				lbp3=1
			bezier(screen,t,xant,yant,zant,aant,xant,yant,zant,a,l,ar,limangmy,limangmn,p)

			pygame.draw.line(screen, variables.GREEN, (25,118), (150,118),2)	
		elif st==13:#Menu Trayectoria Bezier 2D Terminada
			resultado = funciones.trianguloPascal(n)
			h=len(resultado[n])
			if dx==0:
				dx=1
			if dy==0:
				dy=1
			if dz==0:
				dz=1
			step=1.0/seg
			finstep=1.0+step
			if lbp3==0:
				for t in cininv.frange(0.0,finstep,step):
					screen.blit(variables.fondoneg, (205, 0))
					st2=n
					for i in range(h):
						termx+=resultado[n][i]*pow(t,i)*pow((1-t),st2)*comp[i+1][0]
						termy+=resultado[n][i]*pow(t,i)*pow((1-t),st2)*comp[i+1][1]
						st2-=1
					print rbz, termx, termy, dy, dz, math.pow(rbz,2),math.pow(termx,2),math.pow(termy,2), dz
					termz=math.sqrt(math.pow(rbz,2)-math.pow(termx,2)-math.pow(termy,2))
					print termx, termy, termz
					a=[0,0,0,0,0]
					arad,a,nxp1,nyp1=cininv.posf(l,int(termx),int(termy),int(termz),a,limangmy,limangmn)

					am=funciones.testep(a)
					#funciones.mensaje(1,[am[0],am[1],am[2],am[3],am[4]],UDP_PORTs,UDP_IPs,socks)

					xfr,yfr,zfr=cininv.ang(l,arad)
					bezier(screen,t,xant,yant,zant,aant,termx,termy,termz,a,l,ar,limangmy,limangmn,p)
					print "******"
					print "t: " + str(t)
					print "-------------"
					print "Termx:  " + str(termx)
					print "Termy:  " + str(termy)
					print "Termz:  " + str(termz)
					print "Ang1:  " + str(a[0])
					print "Ang2:  " + str(a[1])
					print "Ang3:  " + str(a[2])
					print "Ang4:  " + str(a[3])
					pygame.display.flip()
					time.sleep(3)
					xant=termx
					yant=termy
					zant=termz
					for i in range(4):
						aant[i]=a[i]
					termx=termy=termz=0
				lbp3=1
			bezier(screen,t,xant,yant,zant,aant,xant,yant,zant,a,l,ar,limangmy,limangmn,p)
			pygame.draw.line(screen, variables.GREEN, (25,118), (150,118),2)
		elif st==14:#Menu trayectorias predeterminadas
			bbezier3d=pygame.draw.rect(screen,variables.BLACK,[300,75,350,50])
			bbezier2d=pygame.draw.rect(screen,variables.BLACK,[300,150,550,50])
			bbezierpred=pygame.draw.rect(screen,variables.BLACK,[300,225,550,50])

			if cursor1.colliderect(bbezier3d):
				mtext.render(screen,"Tomar objeto banda",variables.GREEN,(300,75))
			else:
				mtext.render(screen,"Tomar objeto banda",variables.WHITE,(300,75))

			if cursor1.colliderect(bbezier2d):
				mtext.render(screen,"Llevar objeto banda",variables.GREEN,(300,150))
			else:
				mtext.render(screen,"Llevar objeto banda",variables.WHITE,(300,150))

			if cursor1.colliderect(bbezierpred):
				mtext.render(screen,"Saludo",variables.GREEN,(300,225))
			else:
				mtext.render(screen,"Saludo",variables.WHITE,(300,225))
			pygame.draw.line(screen, variables.GREEN, (65,190), (150,190),2)
		pygame.display.flip()

	pygame.quit()
	#os.system("clear")

if __name__ == '__main__':
	print "[Setup]: Programa iniciado"
	comunicacion=comunication()
	ltext=text(40,variables.fuente)
	mtext=text(30,variables.fuente)
	chtext=text(20,variables.fuente)
	xchtext=text(10,variables.fuente)
	cursor1=cursor()
	tb=toolbox()
	main()
	print "[Setup]: Programa terminado"
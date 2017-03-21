import pygame,math
import cininv
import numpy

def carconfig(lbp2,l,a,limangmy,limangmn,UDP_IPe, UDP_PORTe,UDP_IPs, UDP_PORTs):
	if lbp2==0:
		r = open('config.txt', 'r')
		t=r.read()
		g=len(t)

		cuenta=0
		valores_configuracion=[]
		for i in range(g):
			if t[i]==':':
				cuenta+=1
				valores_configuracion.append("")
			else:
				valores_configuracion[cuenta]+=t[i]
		print valores_configuracion
		lbp2=1
		#print "Configuraciones cargadas"
	else:
		pass

	return lbp2,l,a,limangmy,limangmn,UDP_IPe, UDP_PORTe,UDP_IPs, UDP_PORTs

def cd(l,a,ar,limangmy,limangmn,p):
	for i in range(5):
		if a[i]>=limangmy[i]:
			a[i]=limangmy[i]
		elif a[i]<=limangmn[i]:
			a[i]=limangmn[i]

		ar[i]=math.radians(a[i])

	x,y,z=cininv.ang(l,ar)

	xd,yd=cininv.distancias(l,ar)
	p[0]=(950,528)
	p[1]=(950-(int(xd[0])*7),528-(int(yd[0])*7))
	p[2]=(p[0][0]+(int(xd[1])*7),p[0][1]-(int(yd[1])*7))
	p[3]=(p[0][0]+(int(xd[2])*7),p[0][1]-(int(yd[2])*7))
	p[4]=(p[0][0]+(int(xd[3])*7),p[0][1]-(int(yd[3])*7))
	p[5]=(p[0][0]+(int(math.sqrt(pow(x,2)+pow(y,2)))*7),p[0][1]-(int(z)*7))

	return x,y,z,ar,p

def trianguloPascal(n):
	lista = [[1],[1,1]]
	for i in range(1,n):
		linea = [1]
		for j in range(0,len(lista[i])-1):
			linea.extend([ lista[i][j] + lista[i][j+1] ])

		linea += [1]
		lista.append(linea)

	return lista

def trayectorias(n,comp):
	resultado = trianguloPascal(n)
	h=len(resultado[n])
	if lbp3==0:
		for t in cininv.frange(0.0,1.1,0.1):
			if t==1:
				lbp3=1

			st2=n
			print "******"
			print "t: " + str(t)
			for i in range(h):
				termx+=resultado[n][i]*pow(t,i)*pow((1-t),st2)*comp[i+1][0]
				termy+=resultado[n][i]*pow(t,i)*pow((1-t),st2)*comp[i+1][1]
				termz+=resultado[n][i]*pow(t,i)*pow((1-t),st2)*comp[i+1][2]
				st2-=1

			print "-------------"
			print "Termx:  " + str(termx)
			print "Termy:  " + str(termy)
			print "Termz:  " + str(termz)
			print "-------------"
			a1,a2,a3,a4,nxp1,nyp1=cininv.posf(l1,l2,l3,l4,termx,termy,termz,limang5my,limang5mn,limang4my,limang4mn,limang3my,limang3mn,limang2my,limang2mn,limang1my,limang1mn)
			xfr,yfr,zfr=cininv.ang(l1,l2,l3,l4,a1,a2,a3,a4,a5)
			p1=math.degrees(a1)
			p2=math.degrees(a2)
			p3=math.degrees(a3)
			p4=math.degrees(a4)
			print "Ang1:  " + str(p1)
			print "Ang2:  " + str(p2)
			print "Ang3:  " + str(p3)
			print "Ang4:  " + str(p4)
			print "******"

			if p1>0:
				p11=150-p1
			elif p1<0:
				p11=150+abs(p1)
			elif p1==0:
				p11=150

			if p2>0:
				p22=150-p2
			elif p2<0:
				p22=150+abs(p2)
			elif p2==0:
				p22=150

			if p3>0:
				p33=150-p3
			elif p3<0:
				p33=150+abs(p3)
			elif p3==0:
				p33=150

			if p4>0:
				p44=150-p4
			elif p4<0:
				p44=150+abs(p4)
			elif p4==0:
				p44=150

			np1=(p11*1023)/300
			np2=(p22*1023)/300
			np3=(p33*1023)/300
			np4=(p44*1023)/300
			np5=0

			mensaje(p1,p2,p3,p4,0)
			time.sleep(4)

			termx=termy=termz=0.0
		

	variables.botonx.update(screen,cursor1)
	variables.bhome.update(screen,cursor1)

def mousepos(xm,ym):
	xm,ym=pygame.mouse.get_pos()
	return (xm, ym)

"""def mensaje(st,a,UDP_PORTs,UDP_IPs,socks):
	MESSAGE = str(st)+":"+str(a[0])+":"+str(a[1])+":"+str(a[2])+":"+str(a[3])+":"+str(a[4])+":"
	print MESSAGE
	socks.sendto(MESSAGE, ("192.168.1.65", UDP_PORTs))"""

def testep(a):
	am=[0,0,0,0,0]
	if (a[0]*2)>0:
		am[0]=((150-(int(a[0])*2))*1023)/300
	elif (a[0]*2)<0:
		am[0]=((150-(int(a[0])*2))*1023)/300
	elif (a[0]*2)==0:
		am[0]=(150*1023)/300

	for i in range(1,5):
		if a[i]>0:
			am[i]=((150-int(a[i]))*1023)/300
		elif a[i]<0:
			am[i]=((150-int(a[i]))*1023)/300
		elif a[i]==0:
			am[i]=(150*1023)/300

	return am

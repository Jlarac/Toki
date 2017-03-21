#cininv.py
import math, time, os

def ang(l,a):
	z=l[0]+(l[1]*math.cos(a[1]))+(l[2]*math.cos(a[1]+a[2]))+(l[3]*math.cos(a[1]+a[2]+a[3]))
	x=((l[1]*math.sin(a[1]))+(l[2]*math.sin(a[1]+a[2]))+(l[3]*math.sin(a[1]+a[2]+a[3])))*math.cos(a[0])
	y=((l[1]*math.sin(a[1]))+(l[2]*math.sin(a[1]+a[2]))+(l[3]*math.sin(a[1]+a[2]+a[3])))*math.sin(a[0])

	return x,y,z

def distancias(l,a):
	x=[0,0,0,0]
	y=[0,0,0,0]
	x[0]=0.0
	y[0]=float(l[0])
	x[1]=l[1]*math.sin(a[1])
	y[1]=l[0]+l[1]*math.cos(a[1])
	x[2]=l[1]*math.sin(a[1])+l[2]*math.sin(a[1]+a[2])
	y[2]=l[0]+l[1]*math.cos(a[1])+l[2]*math.cos(a[1]+a[2])
	x[3]=l[1]*math.sin(a[1])+l[2]*math.sin(a[1]+a[2])+l[3]*math.sin(a[1]+a[2]+a[3])
	y[3]=l[0]+l[1]*math.cos(a[1])+l[2]*math.cos(a[1]+a[2])+l[3]*math.cos(a[1]+a[2]+a[3])
	return x,y

def distancias2(l,a2,a3,a4):
	x1=0
	y1=l[0]
	x2=l[1]*math.sin(a2)
	y2=l[0]+l[1]*math.cos(a2)
	x3=l[1]*math.sin(a2)+l[2]*math.sin(a2+a3)
	y3=l[0]+l[1]*math.cos(a2)+l[2]*math.cos(a2+a3)
	x4=l[1]*math.sin(a2)+l[2]*math.sin(a2+a3)+l[3]*math.sin(a2+a3+a4)
	y4=l[0]+l[1]*math.cos(a2)+l[2]*math.cos(a2+a3)+l[3]*math.cos(a2+a3+a4)
	return x1,y1,x2,y2,x3,y3,x4,y4
	
def solveang(n,l,x3,y3,x4,y4,nxp,nyp,a,limangmy,limangmn):
	rx=x4-x3
	ry=y4-y3

	sx=nxp-x3
	sy=nyp-y3

	num=(rx*sx)+(ry*sy)
	den=math.sqrt(pow(rx,2)+pow(ry,2))*(math.sqrt(pow(sx,2)+pow(sy,2)))
	gj=num/den

	if gj>1:
		gj=gj-1

	try:
		angulotest=math.acos(gj)
	except :
		print gj

	temp1=a[n]
	temp2=a[n]

	a[n]=angulotest
	angt=a[n]

	for fg in range(1,3):
		if fg==1:
			temp1+=a[n]
			if math.degrees(temp1)>limangmy:
				a[n]=math.radians(limangmy)
				fgs=math.radians(limangmy)
			elif math.degrees(temp1)<limangmn:
				a[n]=math.radians(limangmn)
				fgs=math.radians(limangmn)
			else:
				a[n]=temp1
				fgs=temp1

			x4t=l[1]*math.sin(a[1])+l[2]*math.sin(a[1]+a[2])+l[3]*math.sin(a[1]+a[2]+a[3])
			y4t=l[0]+l[1]*math.cos(a[1])+l[2]*math.cos(a[1]+a[2])+l[3]*math.cos(a[1]+a[2]+a[3])

		elif fg==2:
			temp2-=angt
			if math.degrees(temp2)>limangmy:
				a[n]=math.radians(limangmy)
				fh=math.radians(limangmy)
			elif math.degrees(temp2)<limangmn:
				a[n]=math.radians(limangmn)
				fh=math.radians(limangmn)
			else:
				a[n]=temp2
				fh=temp2

			x4t2=l[1]*math.sin(a[1])+l[2]*math.sin(a[1]+a[2])+l[3]*math.sin(a[1]+a[2]+a[3])
			y4t2=l[0]+l[1]*math.cos(a[1])+l[2]*math.cos(a[1]+a[2])+l[3]*math.cos(a[1]+a[2]+a[3])

	if (math.sqrt(pow(nxp-x4t,2)+pow(nyp-y4t,2)) < math.sqrt(pow(nxp-x4t2,2)+pow(nyp-y4t2,2)) ):
		a[n]=fgs
	else:
		a[n]=fh

	return a

def work(n,l,nxp,nyp,a,limangmy,limangmn):
	x=[0,0,0,0]
	y=[0,0,0,0]
	x,y=distancias(l,a)
	a=solveang(n-1,l,x[n-2],y[n-2],x[3],y[3],nxp,nyp,a,limangmy[n-1],limangmn[n-1])
	
	return a

def nciclos(l,nxp,nyp,a,limangmy,limangmn):
	for i in range(0,30):
		a=work(4,l,nxp,nyp,a,limangmy,limangmn)
		a=work(3,l,nxp,nyp,a,limangmy,limangmn)
		a=work(2,l,nxp,nyp,a,limangmy,limangmn)
	return a

def posf(l,xp,yp,zp,a,limangmy,limangmn):
	if xp==0 and yp>0:
		a[0]=math.radians(limangmy[0])
	elif xp==0 and yp<0:
		a[0]=math.radians(limangmn[0])
	elif xp==0 and yp==0:
		a[0]=math.radians(0)
	elif xp<0 and yp>0:
		rf=float(xp)/float(yp)
		a[0]=math.atan(rf)
		a[0]=math.degrees(a[0])
		a[0]=90.0-a[0]
		a[0]=math.radians(a[0])
		if math.degrees(a[0])>limangmy[0]:
			a[0]=math.radians(limangmy[0])
		elif math.degrees(a[0])<limangmn[0]:
			a[0]=math.radians(limangmn[0])
		else:
			pass
	elif xp<0 and yp<0:
		rf=float(yp)/float(xp)
		a[0]=math.atan(rf)
		a[0]=math.degrees(a[0])
		a[0]=180.0+a[0]
		a[0]=math.radians(a[0])
		if math.degrees(a[0])>limangmy[0]:
			a[0]=math.radians(limangmy[0])
		elif math.degrees(a[0])<limangmn[0]:
			a[0]=math.radians(limangmn[0])
		else:
			pass
	else:
		rf=float(yp)/float(xp)
		a[0]=math.atan(rf)
		if math.degrees(a[0])>limangmy[0]:
			a[0]=math.radians(limangmy[0])
		elif math.degrees(a[0])<limangmn[0]:
			a[0]=math.radians(limangmn[0])
		else:
			pass

	nxp=math.sqrt(pow(xp,2)+pow(yp,2))
	nyp=zp

	arad=nciclos(l,nxp,nyp,a,limangmy,limangmn)

	a[0]=math.degrees(arad[0])
	a[1]=math.degrees(arad[1])
	a[2]=math.degrees(arad[2])
	a[3]=math.degrees(arad[3])
	a[4]=math.degrees(arad[4])

	return arad,a,nxp,nyp

def frange(start,end,inc):
	if end == None:
		end=start+0.0
		start=0.0

	if inc==None:
		inc=1.0
	L=[]

	while 1:
		next=start+len(L)*inc
		if inc>0 and next>=end:
			break
		elif inc<0 and next<=end:
			break
		L.append(next)

	return L
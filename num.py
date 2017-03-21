import numpy,os

def main():
	valores=[]
	while True:
		num=input("Ingresa el valor del numero a partir: \t")
		y=input("En cuantas cantidades se dividira: \t")

		for i in range(0,y):
			x=input("Ingresa el valor #"+str(i+1)+" :")
			valores.append(x)

		for i in range(0,y):
			k=num/valores[i]
			print "Para el #"+str(i+1)+" se encontro:"+str(k)
			l=num-k
			num=l


		st=0
		if st==0:
			break

if __name__ == '__main__':
	os.system("clear")
	main()
import curses
import numpy as np
import os
from select import select
import sys
matriz=[]
tamano=30
jugador=[[1],[1]]

puntaje=0
for i in range(tamano):
	a=[]
	for k in range(2*tamano):
		a.append(0)
	matriz.append(a)
t=0
#Creando los bordes
for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		if i==0 or j==0 or i==len(matriz)-1 or j==len(matriz[i])-1:
			matriz[i][j]=1

#Los 1 son bordes el 2 es el jugador y el 3 es comida

while t!='1':		
	os.system('clear')
	
	for i in range(len(matriz)):
		print ' '
		for j in range(len(matriz[i])):
			if matriz[i][j]==1:
				print '=',
			if matriz[i][j]==0:
				print ' ',	
	print ' '		
	print 'AJUSTE PANTALLA, CUANDO ESTE LISTO, PRESIONE 1 E INTRO'
	t=raw_input("1: ")


#posicionar la comida en otro x,y
def comer(jugador):
	x,y=0,0
	cond=0
	while (x==0 or y==0) and cond==0:
		x=np.random.randint(tamano-1)
		y=np.random.randint(2*tamano-1)
		for i in range(len(jugador[0])):
			if x==jugador[0][i] and y==jugador[1][i]:
				cond=1
	return x,y
	
def posicion(matriz,jugador):
	for i in range(1,len(matriz)-1):
		for j in range(1,len(matriz[i])-1):
			if matriz[i][j]!=3:
				matriz[i][j]=0
	for i in range(len(jugador[0])):
		matriz[jugador[0][i]][jugador[1][i]]=2
	return matriz
	
def movimiento(matriz,jugador,new,puntaje):
	if new=='w':
		if jugador[0][len(jugador[0])-1]>1:
			temp1=[]
			temp2=[]
			for i in range(len(jugador[0])):
				temp1.append(int(jugador[0][i]))
				temp2.append(int(jugador[1][i]))
			
			print jugador
			jugador[0][len(jugador[0])-1]+=-1
			print jugador , '1'
			for i in range(len(jugador[0])-1):
				jugador[0][i]=int(temp1[i+1])
				jugador[1][i]=int(temp2[i+1])
			print jugador,'2'
			#Si hay comida, gana puntaje	
			if matriz[jugador[0][len(jugador[0])-1]][jugador[1][len(jugador[1])-1]]==3:
				x,y=comer(jugador)
				matriz[x][y]=3
				puntaje+=1
				temp1.append(int(jugador[0][len(jugador[0])-1]))
				temp2.append(int(jugador[1][len(jugador[1])-1]))
				jugador[0]=temp1
				jugador[1]=temp2
			
	if new=='s':
		if jugador[0][len(jugador[0])-1]<len(matriz)-2:
			
			
			temp1=[]
			temp2=[]
			for i in range(len(jugador[0])):
				temp1.append(int(jugador[0][i]))
				temp2.append(int(jugador[1][i]))
			
			jugador[0][len(jugador[0])-1]+=+1
			
			for i in range(len(jugador[0])-1):
				jugador[0][i]=int(temp1[i+1])
				jugador[1][i]=int(temp2[i+1])
			
			
			
			#Si hay comida, gana puntaje	
			if matriz[jugador[0][len(jugador[0])-1]][jugador[1][len(jugador[1])-1]]==3:
				x,y=comer(jugador)
				matriz[x][y]=3
				puntaje+=1
				temp1.append(int(jugador[0][len(jugador[0])-1]))
				temp2.append(int(jugador[1][len(jugador[1])-1]))
				jugador[0]=temp1
				jugador[1]=temp2
					
	if new=='a':
		if jugador[1][len(jugador[1])-1]>1:
			
			temp1=[]
			temp2=[]
			for i in range(len(jugador[0])):
				temp1.append(int(jugador[0][i]))
				temp2.append(int(jugador[1][i]))
			
			jugador[1][len(jugador[1])-1]+=-1
			
			for i in range(len(jugador[0])-1):
				jugador[0][i]=int(temp1[i+1])
				jugador[1][i]=int(temp2[i+1])
			
			
			
				
			#Si hay comida, gana puntaje	
			if matriz[jugador[0][len(jugador[0])-1]][jugador[1][len(jugador[1])-1]]==3:
				x,y=comer(jugador)
				matriz[x][y]=3
				puntaje+=1
				temp1.append(int(jugador[0][len(jugador[0])-1]))
				temp2.append(int(jugador[1][len(jugador[1])-1]))
				jugador[0]=temp1
				jugador[1]=temp2
				
	if new=='d':
		if jugador[1][len(jugador[1])-1]<len(matriz[1])-2:
			
			temp1=[]
			temp2=[]
			for i in range(len(jugador[0])):
				temp1.append(int(jugador[0][i]))
				temp2.append(int(jugador[1][i]))
			
			jugador[1][len(jugador[1])-1]+=1
			for i in range(len(jugador[0])-1):
				jugador[0][i]=int(temp1[i+1])
				jugador[1][i]=int(temp2[i+1])
			
			
			
			#Si hay comida, gana puntaje	
			if matriz[jugador[0][len(jugador[0])-1]][jugador[1][len(jugador[1])-1]]==3:
				x,y=comer(jugador)
				matriz[x][y]=3
				puntaje+=1
				temp1.append(int(jugador[0][len(jugador[0])-1]))
				temp2.append(int(jugador[1][len(jugador[1])-1]))
				jugador[0]=temp1
				jugador[1]=temp2
	matriz=posicion(matriz,jugador)	
			
	return matriz,jugador,puntaje
	
def pantalla(matriz,puntaje):
	os.system('clear')
	for i in range(len(matriz)):
		print ' '
		for j in range(len(matriz[i])):
			if matriz[i][j]==1:
				print '=',
			if matriz[i][j]==0:
				print ' ',
			if matriz[i][j]==2:
				print '<',
			if matriz[i][j]==3:
				print '@',			
	print ' '
	print 'Puntaje: ' + str(puntaje)		
	return True

matriz[jugador[0][len(jugador[0])-1]][jugador[1][len(jugador[1])-1]]=2
q,w=comer(jugador)
matriz[q][w]=3	
#pantalla(matriz,puntaje)
print 'lol'
timeout=0
while timeout<=0.1 or timeout>1.0:
	timeout=int(raw_input("Ingrese nivel (1-9): "))
	timeout=1.0/timeout

#timeout=0.1
c='d'
new=c
while True:
	print "\n Movimiento? (W/A/S/D)"
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
		c = str(sys.stdin.readline())[0]
	else:
		print "No input. Moving on..."
	if c in 'wasd':
		if (new=='a' and c!='d') or (new=='s' and c!='w') or (new=='d' and c!='a') or (new=='w' and c!='s'):
			new=str(c)
	#new=raw_input("ASD")		
	matriz,jugador,puntaje=movimiento(matriz,jugador,new,puntaje)
	pantalla(matriz,puntaje)


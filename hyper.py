import math
from math import sin
from math import cos
print("A program to calculate flowfields for hypersonic flows")
print("Start with property change across an oblique shock")
print("starting with default flow properties")

#properties = [V (m/s), a (m/s) ,P (kPa) ,p (kg/m3) ,T (K), y]
flow1 = [3360,336,100,1.225,300, 1.4] #this is an example array of some hypersonic flow at M=10


def oblique(prop,oblang): #this function applies the exact oblique shock equations to a flow and generates the new properties
	M1 = prop[0]/prop[1]
	a = prop[1]
	V1 = prop[0]
	P1 = prop[2]
	p1 = prop[3]
	T1 = prop[4]
	y = prop[5]
	B = math.pi*oblang/180
	#some commonly seen terms
	MsB = (M1**2)*((sin(B))**2)
	
	
	#calculate p2
	P2 = P1*(1+ 2*y*(1/(2*y + 1))*(MsB-1))
	p2 = p1*((y+1)*MsB)*(1/((y-1)*MsB + 2))
	T2 = T1*(P2/P1)*(p1/p2)
	u2 = V1*(1-(2*(MsB-1))*(1/((y+1)*(M1**2))))
	v2 = V1*2*cos(B)*(MsB-1)*(1/((y+1)*(M1**2)))
	print(P2)
	print(p2)
	print(T2)
	print(u2)
	print(v2)
	checkV = pow(u2**2 + v2**2,0.5)
	print(checkV)


def oblique_third(a,y):
#this function takes a list as an argument and adds 5 to the 1st element of that list
	M1 = prop[0]/prop[1]
	a = prop[1]
	V1 = prop[0]
	P1 = prop[2]
	p1 = prop[3]
	T1 = prop[4]
	y = prop[5]
	B = math.pi*oblang/180

###################################################

	P2 = P1 * ( (2 * y / (y + 1) ) * M1 * (sin(B)**2) )

	p2 = p1 * ( y + 1 / y - 1 )

	T2 = T1 * ( 2*y * (y - 1) / ((y + 1)**2) * (M1**2)* (sin(B)**2) )

	u2 = v1 * (1 - ( 2 * (sin(B)**2)/(y+1) ) )

	v2 = v1 * ( sin(2*B)  / ( y + 1) )

	Cp = (4 / (y+1)) * (sin(B)**2)

	return([V1,a,P2,p2,T2,y])

####################################################
	
"""---------------main-------------"""
print(flow1)
oblique(flow1,10)

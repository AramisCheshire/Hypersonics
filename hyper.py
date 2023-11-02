import math
from math import sin
from math import cos
from math import pi
print("A program to calculate flowfields for hypersonic flows")
print("Start with property change across an oblique shock")
print("starting with default flow properties")

#velocity vector = [ Vx, Vy, Vz]
vel1 = [3360,0,0]
#props = [V (m/s),a (m/s) ,P (kPa) ,p (kg/m3) ,T (K), y]
flow1 = [vel1,336,100,1.225,300, 1.4]


#the exact equations for flow property changes across an oblique shock
def oblique(prop,oblang): 
	#this function applies the exact oblique shock equations to a flow and generates the new properties
	Vx = prop[0][0] #reading Vx from V inside of flow1
	a = prop[1]
	M1 = Vx/a
	P1 = prop[2]
	p1 = prop[3]
	T1 = prop[4]
	y = prop[5]
	B = pi*oblang/180 #converting the shock wave angle from degrees to radians
	
	
	#combining the term (M1^2)*(SinB^2) into one variable to reduce clutter
	MsB = (M1**2)*((sin(B))**2)
	
	
	#calculate p2
	P2 = P1*(1+ 2*y*(1/(2*y + 1))*(MsB-1))
	p2 = p1*((y+1)*MsB)*(1/((y-1)*MsB + 2))
	T2 = T1*(P2/P1)*(p1/p2)
	u = Vx*(1-(2*(MsB-1))*(1/((y+1)*(M1**2)))) #note that for input flow we use the notation Vx/Vy/Vz but for output flow we use u,v,w
	v = Vx*2*cos(B)*(MsB-1)*(1/((y+1)*(M1**2)))
	w = 0 #in this case the function only considers 2 dimensional flow so w is 0, but we will keep the input format consistent with 3D flow

	 
	return [[u,v,w],a,P2,p2,T2,y]

#the equations for flow property changes across an oblique shock at the hypersonic limit
def oblique_limit(x,y):
#this function takes a list as an argument and adds 5 to the 1st element of that list
	v1 = x[0][0] #reading V1 from V inside of flow1
	a = x[1]
	M1 = v1/a
	P1 = x[2]
	p1 = x[3]
	T1 = x[4]
	y = x[5]
	B = pi*y/180 #converting the shock wave angle from degrees to radians
	

	P2 = P1 * ( (2 * y / (y + 1) ) * M1 * (sin(B)**2) )

	p2 = p1 * ( y + 1 / y - 1 )

	T2 = T1 * ( 2*y * (y - 1) / ((y + 1)**2) * (M1**2)* (sin(B)**2) )

	u = v1 * (1 - ( 2 * (sin(B)**2)/(y+1) ) )  #note that for input flow we use the notation Vx/Vy/Vz but for output flow we use u,v,w

	v = v1 * ( sin(2*B)  / ( y + 1) )

	w = 0 #in this case the function only considers 2 dimensional flow so w is 0, but we will keep the input format consistent with 3D flow

	Cp = (4 / (y+1)) * (sin(B)**2)

	return [[u,v,w],a,P2,p2,T2,y]

####################################################
	
"""---------------main-------------"""
print("original: ")
print(flow1)
print("exact: ")
flow2_ex = oblique(flow1,10)
print(flow2_ex)
print("at limit: ")
flow2_lim = oblique_limit(flow1,10)
print(flow2_lim)


#some math checks - delete later
R1 = flow1[3]/(flow1[2]*1000*flow1[4])

R2 = flow2_ex[3]/(flow2_ex[2]*1000*flow2_ex[4])
print(R1)
print(R2)

R3 = flow1[3]/(flow1[2]*1000*flow1[4])

R4 = flow2_lim[3]/(flow2_lim[2]*1000*flow2_lim[4])
print(R3)
print(R4)

import math
from math import sin
from math import cos
from math import pi
from math import radians
from math import tan
from math import atan




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
	M2B2 = (M1**2)*((sin(B))**2)
	
	
	#pressure
	numP2 = 2*y*(M2B2 - 1)
	denP2 = y + 1
	P2 = P1*(1+(numP2/denP2))
	
	#density
	nump2 = (y+1)*M2B2
	denp2 = (y-1)*M2B2
	p2 = p1*nump2/denp2
	
	#temperature
	T2 = T1*(P2/P1)*(p1/p2)
	
	#u2
	numu2 = 2*(M2B2 - 1)
	denu2 = (y+1)*(M1**2)
	u2 = Vx*(1-(numu2/denu2))
	
	#v2
	numv2 = 2*cos(B)*(M2B2 - 1)
	denv2 = (y+1)*(M1**2)
	v2 = Vx*(numv2)*(denv2)
	
	w2 = 0 #in this case the function only considers 2 dimensional flow so w is 0, but we will keep the input format consistent with 3D flow

	 
	return [[u2,v2,w2],a,P2,p2,T2,y]

#the equations for flow property changes across an oblique shock at the hypersonic limit
def oblique_limit(x,obl):
#this function takes a list as an argument and adds 5 to the 1st element of that list
	v1 = x[0][0] #reading V1 from V inside of flow1
	a = x[1]
	M1 = v1/a
	P1 = x[2]
	p1 = x[3]
	T1 = x[4]
	y = x[5]
	B = pi*obl/180 #converting the shock wave angle from degrees to radians
	

	P2 = P1 * ( (2 * y / (y + 1) ) * (M1**2) * (sin(B)**2) )

	p2 = p1 * ( (y + 1) / (y - 1) )

	T2 = T1 * ( 2*y * (y - 1) / ((y + 1)**2) * (M1**2)* (sin(B)**2) )

	u = v1 * (1 - ( 2 * (sin(B)**2)/(y+1) ) )  #note that for input flow we use the notation Vx/Vy/Vz but for output flow we use u,v,w

	v = v1 * ( sin(2*B)  / ( y + 1) )

	w = 0 #in this case the function only considers 2 dimensional flow so w is 0, but we will keep the input format consistent with 3D flow

	Cp = (4 / (y+1)) * (sin(B)**2)

	return [[u,v,w],a,P2,p2,T2,y]

	
	
def ThetaBeta(M1,Bdeg,y):
	B = radians(Bdeg)
	num = ((M1**2)*(sin(B)**2))-1
	c2b = cos(2*B)
	den = 2 + (M1**2)*(y+c2b)
	g = 2*(num/den)*(1/tan(B))
	theta = atan(g)*180/pi
	return theta 


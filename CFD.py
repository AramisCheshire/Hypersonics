import random
import time

def wall3pt1st(val1,val2,val3,val4,dx):
    ddx =(-11*val1 + 18*val2 - 9*val3 + 2*val4)/(6*dx)
    return ddx

def central2nd(val1,val2,val3,dx):
	d2x2 =(val3 - 2*val2 + val1)/(dx**2)
	return d2x2


#a CFD software
#result matrix - temperature in a 1D medium through time
def creatematrix(x,y):
	xarray = []
	for i in range(0,x):

		yarray = []
		for i in range(0,y):
			yarray.append(0)#append(random.randint(0,100))
		xarray.append(yarray)
	return xarray
		
#display numbers
def displaymatrix(mtx):
	length = len(mtx)
	for i in range(length):
		
		#print(mtx[i])
		sstr = "%2i: "%i
		ii = i
		for item in mtx[ii]:
			str = " %3i"%(item)
			sstr = sstr + str
		print(sstr)	
		
		
#display labels
def displaymatrixlabels(mtx):
	length = len(mtx)
	for i in range(length):
		#print(mtx[i])
		sstr = ""
		for item in mtx[i]:
			if item > 25:
				item = "hot!"
			else:
				item = "cold!"
			str = " %6s"%(item)
			sstr = sstr + str
		print(sstr)	
        
#display labels
def displaymatrixsymbols(mtx):
	length = len(mtx)
	for i in range(length):
		#print(mtx[i])
		sstr = ""
		for item in mtx[i]:
			if item > 25:
				item = "h"
			else:
				item = "."
			str = " %s"%(item)
			sstr = sstr + str
		print(sstr)	
        
        
        
        
#initialising only
Result = creatematrix(50,20)
	
#print("created a fresh matrix:")
#displaymatrix(Result)

k= 0
xl = len(Result)
yl = len(Result[0])


#displaymatrix(Result)

for i in range(0,xl):

	for j in range(0,yl):

		#Result[i][j] = i**j
		k = k +1
	
	
#set boundary condition on a particular row (time-based)

#set boundary condition on a patricular coloumn (x-based)

#set specific individual points
Result[0][0] = 100

for rowi in range(0,len(Result[0])):
	Result[0][rowi] = 100
for rowi in range(0,len(Result[0])):
	Result[2][rowi] = 100
# Result[3][0] = 100
# Result[11][0] = 100
# Result[5][0] = 100
# Result[23][0] = 100
# Result[4][0] = 100
# Result[19][0] = 100
# Result[42][0] = 100
# Result[44][0] = 100
# Result[45][0] = 100
# Result[46][0] = 100
#displaymatrix(Result)
print("------------------")
dT = 0.01 #seconds
a = 4 #from random google search
dx = 0.5 #0.1m ie 10cm

Endtime = len(Result[0])
Endwall = len(Result)

#Endtime = 9

start_calc = time.time()

for timestep in range(1,Endtime):
    #need to calculate the next generation of T values
    for xitem in range(1,Endwall-1): 
        To = Result[xitem][timestep-1]
        Tm1 = Result[xitem-1][timestep-1] 
        Tp1 = Result[xitem+1][timestep-1]
        d2Tdx2 = central2nd(Tm1,To,Tp1,dx)
        dTdt = a*d2Tdx2 
        T = To + dTdt*dT
        Result[xitem][timestep] = T
    #by the time we get here, xitem is at 8
    u1 = Result[Endwall-1][timestep-1] #wall value
    u2 = Result[Endwall-2][timestep-1]
    u3 = Result[Endwall-3][timestep-1]
    u4 = Result[Endwall-4][timestep-1]
    d2Tdx2 = wall3pt1st(u1,u2,u3,u4,dx)
    dTdt = a*d2Tdx2
    T = To + dTdt*dT
    Result[Endwall-1][timestep] = T

#displaymatrix(Result)

#print(k)
displaymatrix(Result)
#print("xitem: %5i timestep: %5i To: %5i T-1: %5i T+1: %5i d2Tdx2: %5i dTdt: %5i T: %5i"%(xitem, timestep, To,Tm1,Tp1,d2Tdx2,dTdt,T))
for item in range(0,Endwall-1):
    print(Result[item][Endtime-1])
calctime = time.time() - start_calc
print("calculation time: %5fs"%calctime)
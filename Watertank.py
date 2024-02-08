#a 2D Euler solver for an isentropic liquid box

import math
from meshoperations import displaymeshnumbers, displaymeshsymbols, Elems, create2Dmesh, create2DmeshEmpty, create2DwallEmpty
from methods import Continuity2D, XMomentum2D, YMomentum2D, Continuity2D_secondorder, Balls2theWalls
#eg example dictionary
#global fluids = dictionary{"water1":[9,99,999,9999,99999]}

#create the mesh- take user input dimensions

#dimensions of desired box (m):
xdim = 0.2
ydim = 0.2
zdim = 0.4

#mesh granularity- needs to adapt to desired dx

dx = 0.01 #ie 1cm
dt = 0.00001 #seconds

   



def continuity2D(e,mesh,walls,NumX,NumY,dx,dt):
    from methods import central1st as fst
    from methods import wall3pt1st as wst
    
    ddx = ddy = 0
    
    #this should find the right values in the mesh, apply approximations, return d/dt
    if walls[e] == "w":
        #call wall function
        print("wall")
        
        #check for corners first
        if e%NumX == 0 and e < NumX:
            #bottom left corner
            print("yy")
            
        if e%NumX == 0 and e > i+NumX*(NumY-1):
            #top left corner
            print("hgh")
        
        if e%(NumX-1) == 0 and e<NumX:
            print("bottom right")
            
        if e%(NumX-1) == 0 and e>NumX*(NumY-1):
            print("top right")
        
        
        
        # #x:
        # if e%NumX == 0:
            # #on left wall
            # print("left")
            # val1 = mesh[e][0]*mesh[e][3]
            # val2 = mesh[e+1][0]*mesh[e+1][3]
            # val3 = mesh[e+2][0]*mesh[e+2][3]
            # val4 = mesh[e+3][0]*mesh[e+3][3]
            # ddx = wst(val1,val2,val3,val4,dx)
            
            
            
            # if e < NumX:
                # val1 = mesh[e][1]*mesh[e][3]
                # val2 = mesh[e+NumX][1]*mesh[e+NumX][3]
                # val3 = mesh[e+2*NumX][1]*mesh[e+2*NumX][3]
                # val4 = mesh[e+3*NumX][1]*mesh[e+3*NumX][3]
                # ddy = wst(val1,val2,val3,val4,dx) 
            
            # elif e > i+NumX*(NumY-1):
                # val1 = mesh[e][1]*mesh[e][3]
                # val2 = mesh[e-NumX][1]*mesh[e-NumX][3]
                # val3 = mesh[e-2*NumX][1]*mesh[e-2*NumX][3]
                # val4 = mesh[e-3*NumX][1]*mesh[e-3*NumX][3]
                # ddy = wst(val1,val2,val3,val4,dx) 
                
                
            # else:
                # val3 = mesh[e+NumX][1]*mesh[e+NumX][3]
                # val1 = mesh[e-NumX][1]*mesh[e-NumX][3]
                # ddy = fst(val1,val3,dx)
            
            
        # if e%(NumX-1) == 0:
            # #on right wall
            # print("right")
            # val1 = mesh[e][0]*mesh[e][3]
            # val2 = mesh[e-1][0]*mesh[e-1][3]
            # val3 = mesh[e-2][0]*mesh[e-2][3]
            # val4 = mesh[e-3][0]*mesh[e-3][3]
            # ddx = wst(val1,val2,val3,val4,dx)
            # if e < NumX:
                # val1 = mesh[e][1]*mesh[e][3]
                # val2 = mesh[e+NumX][1]*mesh[e+NumX][3]
                # val3 = mesh[e+2*NumX][1]*mesh[e+2*NumX][3]
                # val4 = mesh[e+3*NumX][1]*mesh[e+3*NumX][3]
                # ddy = wst(val1,val2,val3,val4,dx) 
            
            # elif e > i+NumX*(NumY-1):
                # val1 = mesh[e][1]*mesh[e][3]
                # val2 = mesh[e-NumX][1]*mesh[e-NumX][3]
                # val3 = mesh[e-2*NumX][1]*mesh[e-2*NumX][3]
                # val4 = mesh[e-3*NumX][1]*mesh[e-3*NumX][3]
                # ddy = wst(val1,val2,val3,val4,dx) 
                
                
            # else:
                # val3 = mesh[e+NumX][1]*mesh[e+NumX][3]
                # val1 = mesh[e-NumX][1]*mesh[e-NumX][3]
                # ddy = fst(val1,val3,dx)           
            
            
        # # for i in range(0,NumY):
    # # walls[i*NumX] = "w"
    # # walls[i*NumX + NumX-1] = "w"
    
        
        # #y: check what type of boundary the wall belongs to
        # if e < NumX: #then its on the bottom

            # val1 = mesh[e][1]*mesh[e][3]
            # val2 = mesh[e+NumX][1]*mesh[e+NumX][3]
            # val3 = mesh[e+2*NumX][1]*mesh[e+2*NumX][3]
            # val4 = mesh[e+3*NumX][1]*mesh[e+3*NumX][3]
            # ddy = wst(val1,val2,val3,val4,dx) 
            
            # if e%NumX == 0:
            # #on left wall
                # print("left")
                # val1 = mesh[e][0]*mesh[e][3]
                # val2 = mesh[e+1][0]*mesh[e+1][3]
                # val3 = mesh[e+2][0]*mesh[e+2][3]
                # val4 = mesh[e+3][0]*mesh[e+3][3]
                # ddx = wst(val1,val2,val3,val4,dx)
            
            # elif e%(NumX-1) == 0:
            # #on right wall
                # print("right")
                # val1 = mesh[e][0]*mesh[e][3]
                # val2 = mesh[e-1][0]*mesh[e-1][3]
                # val3 = mesh[e-2][0]*mesh[e-2][3]
                # val4 = mesh[e-3][0]*mesh[e-3][3]
                # ddx = wst(val1,val2,val3,val4,dx)
                
                
               
            # else:
                # val3 = mesh[e+1][0]*mesh[e+1][3]
                # val1 = mesh[e-1][0]*mesh[e-1][3]
                # ddx = fst(val1,val3,dx)
            
            
        # if e > i+NumX*(NumY-1):
        
        # #top
            # print("top")
                    
            # val1 = mesh[e][1]*mesh[e][3]
            # val2 = mesh[e-NumX][1]*mesh[e-NumX][3]
            # val3 = mesh[e-2*NumX][1]*mesh[e-2*NumX][3]
            # val4 = mesh[e-3*NumX][1]*mesh[e-3*NumX][3]
            # ddy = wst(val1,val2,val3,val4,dx) 
            
            
            
            
            
            # if e%NumX == 0:
            # #on left wall
                # print("left")
                # val1 = mesh[e][0]*mesh[e][3]
                # val2 = mesh[e+1][0]*mesh[e+1][3]
                # val3 = mesh[e+2][0]*mesh[e+2][3]
                # val4 = mesh[e+3][0]*mesh[e+3][3]
                # ddx = wst(val1,val2,val3,val4,dx)
            
            # elif e%(NumX-1) == 0:
            # #on right wall
                # print("right")
                # val1 = mesh[e][0]*mesh[e][3]
                # val2 = mesh[e-1][0]*mesh[e-1][3]
                # val3 = mesh[e-2][0]*mesh[e-2][3]
                # val4 = mesh[e-3][0]*mesh[e-3][3]
                # ddx = wst(val1,val2,val3,val4,dx)
            # else:
                # val3 = mesh[e+1][0]*mesh[e+1][3]
                # val1 = mesh[e-1][0]*mesh[e-1][3]
                # ddx = fst(val1,val3,dx)
    else:
        #call internal function
        #use the two neighbouring elements, e-1 and e+1, to calculate dpudx for e
        val3 = mesh[e+1][0]*mesh[e+1][3]
        val1 = mesh[e-1][0]*mesh[e-1][3]
        ddx = fst(val1,val3,dx)
        
        #use the two opposite elements, e+NumX and e-NumX, to calculate dpvdy for e
        val3 = mesh[e+NumX][1]*mesh[e+NumX][3]
        val1 = mesh[e-NumX][1]*mesh[e-NumX][3]
        ddy = fst(val1,val3,dx)
    
    
    
    dpdt = -1*(ddx+ddy)
    return dpdt




Elem = Elems(xdim,ydim,dx)
NumX = Elem[0]
NumY = Elem[1]

print("\n")
mesh = create2Dmesh(NumX,NumY)

#change element at (0,3)
#mesh[3*21][0] = 1000001

#print(mesh)



timemesh = []

#need a mesh for the walls

walls = create2DwallEmpty(NumX,NumY)

#add the floor at elems 0 - NumX
 
#rows
for i in range(0,NumX):
    walls[i] = "w"
    walls[i+NumX*(NumY-1)] = "w"
 
#coloumns 
for i in range(0,NumY):
    walls[i*NumX] = "w"
    walls[i*NumX + NumX-1] = "w"
    
#add initial conditions:
for i in range(2,7):
    walls[2*NumX+i] = "u"
    mesh[2*NumX+i][3] = 1
    
    walls[3*NumX+i] = "u"
    mesh[3*NumX+i][3] = 1


mesh[200][0] = 1
  
#print(walls)


displaymeshsymbols(walls,NumX,NumY)
print("\n\n")

displaymeshnumbers(mesh,NumX,NumY,0)
print("\n\n")
#print(mesh)
#nextmesh = create2Dmesh(NumX,NumY)

nextmesh = mesh[:]
#print(nextmesh)


#initialise gas constant
TRa = mesh[0][4]/mesh[0][3]

for timestep in range(0,1):
    #at each timestep, update the matrix
    
    
    for element in range(0,len(mesh)):
        
        
        
        
        #wall condition only applies to velocities
        
        dpdt = Continuity2D(element,mesh,NumX,NumY,dx)
        dp2dt = Continuity2D_secondorder(element,mesh,NumX,NumY,dx)
        
        nextmesh[element][3] = mesh[element][3] + dpdt*dt + dp2dt*(dt**2)/2
        
        
        
        #check for wall and treat separately - check for left/right first for u and top/bottom for v
        
        
        if element%NumX == 0 or (element+1)%NumX == 0:
            #left/right wall so u is zero
            nextmesh[element][0] = 0
        else: 
            
            dudt = XMomentum2D(element,mesh,NumX,NumY,dx)
        
        
            nextmesh[element][0] = mesh[element][0] + dudt*dt
        
        if (element < NumX) or (element > (NumX*NumY - NumX - 1)):
            #top or bottom so v is zero
            nextmesh[element][1] = 0

        else:
          
        
            dvdt = YMomentum2D(element,mesh,NumX,NumY,dx)
        
            nextmesh[element][1] = mesh[element][1] + dvdt*dt
        #print(Co)
        
        nextmesh[element][4] = mesh[element][3]*TRa
        
        
    # fr = open("base.csv","a")
    # fr.write(nextmesh)
    # fr.close()
    mesh=nextmesh[:]
    print(timestep)
    displaymeshnumbers(mesh,NumX,NumY,0)
   #print(mesh[338])
    
    
    
#displaymeshnumbers(mesh,NumX,NumY,0)


Balls2theWalls(10,mesh,NumX,NumY,dx)
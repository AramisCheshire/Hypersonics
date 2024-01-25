#a 2D Euler solver for an isentropic liquid box

import math
from meshoperations import displaymeshnumbers, displaymeshsymbols, Elems, create2Dmesh, create2DmeshEmpty, create2DwallEmpty

#eg example dictionary
#global fluids = dictionary{"water1":[9,99,999,9999,99999]}

#create the mesh- take user input dimensions

#dimensions of desired box (m):
xdim = 0.2
ydim = 0.2
zdim = 0.4

#mesh granularity- needs to adapt to desired dx

dx = 0.01 #ie 1cm
dt = 0.001 #seconds

# def displaymeshnumbers(mesh,NumX,NumY,property):
    # ss = ""
    # k = 0
    # for item in range(0,len(mesh)):
        # ss = ss + "%i"%(mesh[item][property])
        # k = k +1
        # if k == NumX:
           
            # print(ss)
            # ss = ""
            # k = 0
            
# def displaymeshsymbols(mesh,NumX,NumY):
    # ss = ""
    # k = 0
    # for item in range(0,len(mesh)):
        # ss = ss + "%s"%(mesh[item])
        # k = k +1
        # if k == NumX:
           
            # print(ss)
            # ss = ""
            # k = 0
        
 
# def Elems(x,y,dx):
    # NumX = math.floor(x/dx) + 1
    # NumY = math.floor(y/dx) + 1
    
    # return [NumX,NumY]
    
# def create2Dmesh(NumX,NumY):


    # #now, create a multi-D array where the position of the element reveals whether its x or y based
    # #every NumX elements = one y value, repeat NumY times

    # mesh = []
    # for i in range(0,NumX*NumY):
        # #prop can be loaded from a settings file or a dictionary variable
        # prop = [0,0,0,1.225,100,292,1.4]
        # mesh.append(prop)
    
    # return mesh
 

# def create2DmeshEmpty(NumX,NumY):


# #now, create a multi-D array where the position of the element reveals whether its x or y based
# #every NumX elements = one y value, repeat NumY times

    # mesh = []
    # for i in range(0,NumX*NumY):
        # #prop can be loaded from a settings file or a dictionary variable
        # mesh.append(0)

    # return mesh      
    
    
    
# def create2DwallEmpty(NumX,NumY):


# #now, create a multi-D array where the position of the element reveals whether its x or y based
# #every NumX elements = one y value, repeat NumY times

    # mesh = []
    # for i in range(0,NumX*NumY):
        # #prop can be loaded from a settings file or a dictionary variable
        # mesh.append(".")

    # return mesh      



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
    mesh[2*NumX+i][0] = 1
    
    walls[3*NumX+i] = "u"
    mesh[3*NumX+i][0] = 1

  
#print(walls)


displaymeshsymbols(walls,NumX,NumY)
print("\n\n")

displaymeshnumbers(mesh,NumX,NumY,0)
#print(mesh)
nextmesh = create2Dmesh(NumX,NumY)

for element in range(0,len(nextmesh)):
    nextmesh[element] = continuity2D(element,mesh,walls,NumX,NumY,dx,dt)
    
displaymeshnumbers(nextmesh,NumX,NumY,0)
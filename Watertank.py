#a 2D Euler solver for an isentropic liquid box

import math
from meshoperations import displaymeshnumbers, displaymeshsymbols, Elems, create2Dmesh, create2DmeshEmpty, create2DwallEmpty
from methods import Continuity2D, XMomentum2D, YMomentum2D, Continuity2D_secondorder, Balls2theWalls, wallsfnc, corners, governing_2d 
#from viz import createimage
#eg example dictionary
#global fluids = dictionary{"water1":[9,99,999,9999,99999]}

#create the mesh- take user input dimensions

#dimensions of desired box (m):
xdim = 2
ydim = 2
zdim = 0.4

#mesh granularity- needs to adapt to desired dx

dx = 0.1 #ie 1cm
dt = 0.00001 #seconds

   








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
    mesh[2*NumX+i][4] = 150000
    
    walls[3*NumX+i] = "u"
    mesh[3*NumX+i][4] = 150000


#mesh[200][0] = 1
  
#print(walls)


displaymeshsymbols(walls,NumX,NumY)
print("\n\n")

#displaymeshnumbers(mesh,NumX,NumY,4)
#print("\n\n")
#print(mesh)
#nextmesh = create2Dmesh(NumX,NumY)

nextmesh = mesh[:]
#print(nextmesh)


#initialise gas constant
TRa = mesh[0][4]/mesh[0][3]


#print(NumX)
#print(NumY)

displaymeshnumbers(mesh,NumX,NumY,4)

ders = create2DmeshEmpty(NumX,NumY)

for timestep in range(0,10):
    #at each timestep, update the matrix
    
    u_coeff = 1
    v_coeff = 1

    nextmesh = mesh[:]

    for element in range(0,len(mesh)):
        u_coeff = 1
        v_coeff = 1
        #print(element)
        #first check for corners and walls. apply appropriate space generator. then use space function.
        #for corners and walls, boundary conditions should ignore some of the derivative values.
        
        
        if element == 0 or element == (NumX*NumY -1) or element == (NumX-1) or element == (NumX*NumY - NumX):
            #either of 4 corners
            space = corners(element,mesh,NumX,NumY,dx)
        
        elif element < NumX or element > (NumX*NumY - NumX - 1) or element%NumX == 0 or (element+1)%NumX==0:
            space = wallsfnc(element,mesh,NumX,NumY,dx)
            
    
        else:
            space = Balls2theWalls(element,mesh,NumX,NumY,dx)
        
        
        
        #print(space)
        #space has 3 diff ways to be generated but the result will be used in the time-der calculator:
        
        ttd = governing_2d(space)
        
        # if element == 44:
            # print("dudt,dvdt,dpdt,dPdt,du2dt2,dv2dt2,dp2dt2,dP2dt2")
            
            # print(ttd)
            # print("space:")
            # print(space)
            
        
        ders[element] = ttd[0]
        
        
        #now apply the ders in forming the next timestep elements
        
        #but need to apply boundary conditions
        
        if element%NumX == 0:# or (element-1)%NumX==0:
            #left or right wall
            u_coeff = 0
        
        if element < NumX or element > (NumX*NumY - NumX -1):
            #top or bottom wall
            v_coeff = 0
            
        #boundary conditions done, now apply time ders to timestep
        
        #u
        nextmesh[element][0] = (mesh[element][0] + ttd[0]*dt + 0*ttd[4]*(dt**2)/2)*u_coeff
        
        
        #v
        nextmesh[element][1] = (mesh[element][1] + ttd[1]*dt + 0*ttd[5]*(dt**2)/2)*v_coeff
        
        
        #p
        
        nextmesh[element][3] = mesh[element][3] + ttd[2]*dt + 0*ttd[6]*(dt**2)/2
        
        #P
        
        nextmesh[element][4] = mesh[element][4] + ttd[3]*dt
    
    
    mesh=nextmesh[:]
    print("timestep: %i"%timestep)
    #displaymeshnumbers(mesh,NumX,NumY,0)
   #print(mesh[338])
    
    
    
#displaymeshnumbers(mesh,NumX,NumY,4)



#print("displaying derivatives of u:")

for jj in range(0,len(mesh)):
    print(mesh[jj][1])

# nom = 0
# for jj in ders:
    # print("at number %i: %6.1f"%(nom,jj))
    # nom = nom + 1
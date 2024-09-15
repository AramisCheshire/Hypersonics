#a 2D Euler solver for an isentropic liquid box

import math
from meshoperations import displaymeshnumbers, displaymeshsymbols, Elems, create2Dmesh, create2DmeshEmpty, create2DwallEmpty
from methods import Continuity2D, XMomentum2D, YMomentum2D, Continuity2D_secondorder, Balls2theWalls, wallsfnc, corners, governing_2d, interior_fwd, interior_bwd 
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
    walls[5*NumX+i] = "u"
    mesh[5*NumX+i][4] = 99000
    
    walls[6*NumX+i] = "u"
    mesh[6*NumX+i][4] = 99000


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

displaymeshnumbers(mesh,NumX,NumY,0)

ders = create2DmeshEmpty(NumX,NumY)

for timestep in range(250):
    #at each timestep, update the matrix
    
    u_coeff = 1
    v_coeff = 1

    nextmesh = mesh[:]
    predictor = mesh[:]
    corrector = mesh[:]
    for element in range(0,len(mesh)):
        u_coeff = 1
        v_coeff = 1
        
	
	#the following function creates an array called space, which contains the adjacent points to an element and all the spatial derivatives of it

        #first check for corners and walls. apply appropriate space generator. then use space function.
        #for corners and walls, boundary conditions should ignore some of the derivative values.
        
        
        if element == 0 or element == (NumX*NumY -1) or element == (NumX-1) or element == (NumX*NumY - NumX):
            #either of 4 corners
            space = corners(element,mesh,NumX,NumY,dx)
        
        elif ((element < NumX) or (element > (NumX*NumY - NumX - 1)) or (element%NumX == 0) or (element+1)%NumX==0):
            #print("on element %i - entering wall function"%element)            
            space = wallsfnc(element,mesh,NumX,NumY,dx)
            
    
        else:
	    #interior points
            #space = Balls2theWalls(element,mesh,NumX,NumY,dx)
            space = interior_fwd(element,mesh,NumX,NumY,dx)       
        #space has 3 diff ways to be generated but the result will be used in the time-der calculator:
        

	#governing_2d returns 6 temporal derivatives using the elements contained in space
        ttd = governing_2d(space) 
        
	
	
        #ders[element] = ttd[0] -- might be unneeded
        
        
        #now apply the ders in forming the next timestep elements
        
        #but need to apply boundary conditions
        
        if element%NumX == 0 or (element-1)%NumX==0:
            #left or right wall
            u_coeff = 0
        
        if element < NumX or element > (NumX*NumY - NumX -1):
            #top or bottom wall
            v_coeff = 0
            
        #boundary conditions done, now apply time ders to timestep
        
        #u
        predictor[element][0] = (mesh[element][0] + ttd[0]*dt + 0*ttd[4]*(dt**2)/2)*u_coeff
        
        
        #v
        predictor[element][1] = (mesh[element][1] + ttd[1]*dt + 0*ttd[5]*(dt**2)/2)*v_coeff
        
        
        #p
        
        predictor[element][3] = mesh[element][3] + ttd[2]*dt + 0*ttd[6]*(dt**2)/2
        
        #P
        
        predictor[element][4] = mesh[element][4] + ttd[3]*dt
    		
        #now mesh contains the initial values, and predictor the predictor step of maccormack.
        #could create another mesh for the corrector step, and then copy it into mesh.
    
        #need to calculate backwards space from predictor values, then get the temporal derivatives, then average them out
        
        if element == 0 or element == (NumX*NumY -1) or element == (NumX-1) or element == (NumX*NumY - NumX):
            #either of 4 corners
            space = corners(element,predictor,NumX,NumY,dx)
        
        elif element < NumX or element > (NumX*NumY - NumX - 1) or element%NumX == 0 or (element+1)%NumX==0:
            space = wallsfnc(element,predictor,NumX,NumY,dx)
            
    
        else:
	    #interior points
            space = interior_bwd(element,predictor,NumX,NumY,dx)       
        
	#governing_2d returns 6 temporal derivatives using the elements contained in space
        ttd_bwd = governing_2d(space)

        #average out derivatives contained in ttd and in ttd_bwd, then apply to mesh[] 
        
        ttd_avg = []

        for deritem in range(8):
            ttd_avg.append(0.5*ttd[deritem] + 0.5*ttd_bwd[deritem])
            #print("sanity check - on value ttd[%d]\n"%deritem)
	
        if element%NumX == 0 or (element-1)%NumX==0:
            #left or right wall
            u_coeff = 0
        
        if element < NumX or element > (NumX*NumY - NumX -1):
            #top or bottom wall

            v_coeff = 0
            
        #boundary conditions done, now apply time ders to timestep
        
        #u
        nextmesh[element][0] = (mesh[element][0] + ttd_avg[0]*dt + 0*ttd_avg[4]*(dt**2)/2)*u_coeff
        
        
        #v
        nextmesh[element][1] = (mesh[element][1] + ttd_avg[1]*dt + 0*ttd_avg[5]*(dt**2)/2)*v_coeff
        
        
        #p
        
        nextmesh[element][3] = mesh[element][3] + ttd_avg[2]*dt + 0*ttd_avg[6]*(dt**2)/2
        
        #P
        
        nextmesh[element][4] = mesh[element][4] + ttd_avg[3]*dt






    mesh=nextmesh[:]
    print("timestep: %i"%timestep)
   
    
displaymeshnumbers(mesh,NumX,NumY,0)

print("the dimensions were NumX: %i and NumY: %i"%(NumX,NumY))



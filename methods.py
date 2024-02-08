def wall3pt1st(val1,val2,val3,val4,dx):
    ddx =(-11*val1 + 18*val2 - 9*val3 + 2*val4)/(6*dx)
    return ddx

def central2nd(val1,val2,val3,dx):
	d2x2 =(val3 - 2*val2 + val1)/(dx**2)
	return d2x2


def central1st(val1,val3,dx):
    ddx = (val3-val1)/2*dx
    return ddx

def dds(vp1,vm1,dx):
    ddx = (vp1-vm1)/(2*dx)
    return ddx


def dds2(vp1,v0,vm1,dx):
    ddx = (vp1+vm1-2*v0)/(2*(dx**2))
    return ddx
    
    
def ddsm(v11,v10,v01,v00,dx):
    ddx = (v11+v00-v10-v01)/(4*(dx**2))
    return ddx

def ddswall(u3,u2,u1,dx):
    dd2 = 


def corners(e,mesh,NumX,NumY,dx):
    u00 = mesh[e]
    if e==0:
        #bottom left
        u10 = mesh[e+1]
        u20 = mesh[e+2]
        u30 = mesh[e+3]
        u01 = mesh[e+1*NumX]
        u02 = mesh[e+2*NumX]
        u03 = mesh[e+3*NumX]
        
        
    if e==(NumX-1):
        #bottom right
        u10 = mesh[e-1]
        u20 = mesh[e-2]
        u30 = mesh[e-3] 
        u01 = mesh[e+1*NumX]
        u02 = mesh[e+2*NumX]
        u03 = mesh[e+3*NumX]
        
    if e==(NumX*NumY - 1):
        #top right
        u10 = mesh[e-1]
        u20 = mesh[e-2]
        u30 = mesh[e-3]
        u01 = mesh[e-NumX]
        u02= mesh[e-2*NumX]
        u03 = mesh[e-3*NumX]
        
    if e==(NumX*NumY-1-NumX):
        u10 = mesh[e+1]
        u20 = mesh[e+2]
        u30 = mesh[e+3]
        u01 = mesh[e-NumX]
        u02 = mesh[e-2*NumX]
        u03 = mesh[e-3*NumX]
        
    u11,u1m1,um11,um1m1 = 0
    
    
    
    
    #produce u,du/dx,du/dy, du/dx2 , dv/dx2
    
    
    
    
    

def Balls2theWalls(e,mesh,NumX,NumY,dx):
    #4 parameters: u,v,p,P
    #6 space derivatives for each - store in a 24-item array
    #9 mesh points are required - meaning, 36 different values
    #segregate walls and corners
    
    
    #start by generating values
    
    #corners
    
    
    
    #no walls:
    
    u00 = mesh[e]
    u10 = mesh[e+1]
    um10 = mesh[e-1]
    u01 = mesh[e+NumX]
    u0m1 = mesh[e-NumX]
    u11 = mesh[e+NumX+1]
    u1m1 = mesh[e+1-NumX]
    um11 = mesh[e-1+NumX]
    um1m1 = mesh[e-NumX-1]
    
    #now we want to create 24 space derivatives
    
    
    space = []
    #u
    for v in (0,1,3,4):
        space.append(u00[v])
    #d/dx
    for v in (0,1,3,4):
        space.append(dds(u10[0],um10[0],dx))
    #d/dy
    for v in (0,1,3,4):
        space.append(dds(u01[0],u0m1[0],dx)) 
    #d2/dx2
    for v in (0,1,3,4):
        space.append(dds2(u10[v],u00[v],um10[v],dx))
    #d2/dy2
    for v in (0,1,3,4):
        space.append(dds2(u01[v],u00[v],u0m1[v],dx))   
    #d2/dxdy
    for v in (0,1,3,4):
        space.append(ddsm(u11[v],u1m1[v],um11[v],um1m1[v],dx))
    

    

    
    
    
    
    return space
    
    
 




#something for X and something for Y
def ddx(e,mesh,NumX,prop,dx):
    #check for walls here 
    if e%NumX==0:
        #left wall
        u1 = mesh[e][prop]
        u2 = mesh[e+1][prop]
        u3 = mesh[e+2][prop]
        
        dd = (4*u2 - 3*u1 - u3)/(2*dx)
        
    elif (e+1)%(NumX)==0:
        #right wall
        u1 = mesh[e][prop]
        u2 = mesh[e-1][prop]
        u3 = mesh[e-2][prop]
        
        dd = (4*u2 - 3*u1 - u3)/(2*dx)
        
    else:
        up1 = mesh[e+1][prop]
       
        um1 = mesh[e-1][prop]
        
        dd = (up1-um1)/(2*dx)
        
    return dd
    
def ddy(e,mesh,NumX,NumY,prop,dx):
    #check for walls here 
    if e < NumX:
        #bottom
        u1 = mesh[e][prop]
        u2 = mesh[e+NumX][prop]
        u3 = mesh[e+2*NumX][prop]
        
        dd = (4*u2 - 3*u1 - u3)/(2*dx)
        
    elif e > (NumX*NumY - NumX - 1):
        #top
        u1 = mesh[e][prop]
        u2 = mesh[e-1*NumX][prop]
        u3 = mesh[e-2*NumX][prop]
        
        dd = (4*u2 - 3*u1 - u3)/(2*dx)
        
    else:
        up1 = mesh[e+NumX][prop]
       
        um1 = mesh[e-NumX][prop]
        
        dd = (up1-um1)/(2*dx)
        
    return dd


def ddx2(e,mesh,NumX,prop,dx):
    #need to check for walls
    if e%NumX==0:
        #left wall
        u1=mesh[e][prop]
        u2=mesh[e+1][prop]
        u3=mesh[e+2][prop]
        
        dd2 = (u3- 2*u2 +1)/(2*(dx**2))
        
        
    elif (e+1)%NumX==0:
        #right wall
        u1 = mesh[e][prop]
        u2=mesh[e-1][prop]
        u3=mesh[e-2][prop]
        
        dd2 = (u3- 2*u2 +1)/(2*(dx**2)) 
    else:
    
        #no wall:
        u1 = mesh[e+1][prop]
        u0 = mesh[e][prop]
        um1 = mesh[e-1][prop]
        
        dd2 = (u1 + um1 - 2*u0)/(2*(dx**2))
    
    return dd2
    
    
def ddy2(e,mesh,NumX,NumY,prop,dx):
    
    if e < NumX:
        #bottom
        u1=mesh[e][prop]
        u2=mesh[e+NumX][prop]
        u3=mesh[e+2*NumX][prop]
        
        dd2 = (u3- 2*u2 +1)/(2*(dx**2))

    elif e > (NumX*NumY - 1 - NumX):
        #top
        u1=mesh[e][prop]
        u2=mesh[e-NumX][prop]
        u3=mesh[e-2*NumX][prop]
        
        dd2 = (u3- 2*u2 +1)/(2*(dx**2))
        
        
        
    else:
    
        u1 = mesh[e+NumX][prop]
        u0 = mesh[e][prop]
        um1 = mesh[e-NumX][prop]
    
        dd2 = (u1+um1-2*u0)/(2*(dx**2))
    
    return dd2

    
    
def mixdd(e,mesh,NumX,NumY,prop,dx):
    dy=dx
    #for mixed spatial derivatives i.e d2
    
    #start with corners - no derivative possible for them
    
    if e ==0 or e == NumX or e == (NumX*NumY-1) or e==(NumX*NumY-NumX):
        ddm = 0 #corner case
        
   
    elif e%NumX ==0:
        #left wall
        u11 = mesh[e+NumX][prop]
        u1m1 = mesh[e-NumX][prop]
        u21 = mesh[e+NumX+1][prop]
        u2m1 = mesh[e-NumX+1][prop]
        u31 = mesh[e+NumX+2][prop]
        u3m1 = mesh[e-NumX+2][prop]
        
        ddm = (4*u21 - 4*u2m1 - 3*u11 + 3*u1m1 -u31 + u3m1)/(4*dx*dy)
        
        
        
    #need a wall check
    
    elif (e+1)%NumX == 0:
        #right wall
        u11 = mesh[e+NumX][prop]
        u1m1 = mesh[e-NumX][prop]
        u21 = mesh[e+NumX-1][prop]
        u2m1 = mesh[e-NumX-1][prop]
        u31 = mesh[e+NumX-2][prop]
        u3m1 = mesh[e-NumX-2][prop]
        
        ddm = (4*u21 - 4*u2m1 - 3*u11 + 3*u1m1 -u31 + u3m1)/(4*dx*dy)
        
        
    elif e < NumX:
        #bottom
        u11 = mesh[e+1][prop]
        u1m1 = mesh[e-1][prop]
        u21 = mesh[e+NumX+1][prop]
        u2m1 = mesh[e+NumX-1][prop]
        u31 = mesh[e+(2*NumX)+1][prop]
        u3m1 = mesh[e+(2*NumX)-1][prop]
        
        ddm = (4*u21 - 4*u2m1 - 3*u11 + 3*u1m1 -u31 + u3m1)/(4*dx*dy)
        
    elif e > (NumX*NumY-NumX-1):    
        u11 = mesh[e+1][prop]
        u1m1 = mesh[e-1][prop]
        u21 = mesh[e-NumX+1][prop]
        u2m1 = mesh[e-NumX-1][prop]
        u31 = mesh[e-(2*NumX)+1][prop]
        u3m1 = mesh[e-(2*NumX)-1][prop]
        
        ddm = (4*u21 - 4*u2m1 - 3*u11 + 3*u1m1 -u31 + u3m1)/(4*dx*dy)
        
        
        
    

    else:
        ddm = (mesh[e+NumX+1][prop] + mesh[e-NumX-1][prop] -mesh[e+1-NumX][prop] -mesh[e+NumX-1][prop])/(4*dx*dy)
    return ddm
    


def Continuity2D(e,mesh,NumX,NumY,dx):
    term1 = mesh[e][3]*ddx(e,mesh,NumX,0,dx)
    term2 = mesh[e][0]*ddx(e,mesh,NumX,3,dx)
    term3 = mesh[e][3]*ddy(e,mesh,NumX,NumY,1,dx)
    term4 = mesh[e][1]*ddy(e,mesh,NumX,NumY,3,dx)
    ddt = -1*(term1 + term2 + term3 + term4)
    # if e == 338:
        # print("continuity dpdt: %f"%ddt)
    return ddt
    
    
def XMomentum2D(e,mesh,NumX,NumY,dx):
    term1 = mesh[e][0]*ddx(e,mesh,NumX,0,dx)
    term2 = mesh[e][1]*ddy(e,mesh,NumX,NumY,0,dx)
    term3 = ddx(e,mesh,NumX,4,dx)/(mesh[e][3])
    dudt = -1*(term1 + term2 + term3)
    # if e == 338:
        # print("momentum dudt: %f"%dudt)
    return dudt
    
def YMomentum2D(e,mesh,NumX,NumY,dx):
    term1 = mesh[e][0]*ddx(e,mesh,NumX,0,dx)
    term2 = mesh[e][1]*ddy(e,mesh,NumX,NumY,1,dx)
    term3 = ddy(e,mesh,NumX,NumY,4,dx)/mesh[e][3]
    dvdt = -1*(term1 + term2 + term3)
    # if e == 338:
        # print("momentum dvdt: %f"%dvdt)
    return dvdt
    
    

def Continuity2D_secondorder(e,mesh,NumX,NumY,dx):

    u = mesh[e][0]
    v = mesh[e][1]
    p = mesh[e][3]
    P = mesh[e][4]
    pterm = 1/p

    dudx = ddx(e,mesh,NumX,0,dx)
    dvdx = ddx(e,mesh,NumX,1,dx)
    dpdx = ddx(e,mesh,NumX,3,dx)
    dPdx = ddx(e,mesh,NumX,4,dx)
    
    dudy = ddy(e,mesh,NumX,NumY,0,dx)
    dvdy = ddy(e,mesh,NumX,NumY,1,dx)
    dpdy = ddy(e,mesh,NumX,NumY,3,dx)
    dPdy = ddy(e,mesh,NumX,NumY,4,dx)
    
    dpdt = Continuity2D(e,mesh,NumX,NumY,dx)
    dudt = XMomentum2D(e,mesh,NumX,NumY,dx)
    dvdt = YMomentum2D(e,mesh,NumX,NumY,dx)
  
    du2dx = ddx2(e,mesh,NumX,0,dx)
    dv2dx = ddx2(e,mesh,NumX,1,dx)
    dp2dx = ddx2(e,mesh,NumX,3,dx)
    dP2dx = ddx2(e,mesh,NumX,4,dx)
    
    du2dy = ddy2(e,mesh,NumX,NumY,0,dx)
    dv2dy = ddy2(e,mesh,NumX,NumY,1,dx)
    dp2dy = ddy2(e,mesh,NumX,NumY,3,dx)
    dP2dy = ddy2(e,mesh,NumX,NumY,4,dx)
    
    du2dxdy = mixdd(e,mesh,NumX,NumY,0,dx)
    dv2dxdy = mixdd(e,mesh,NumX,NumY,1,dx)
    dp2dxdy = mixdd(e,mesh,NumX,NumY,3,dx)
    dP2dxdy = mixdd(e,mesh,NumX,NumY,4,dx)
    
    
    
    simpleterms = dudx*dpdt + dpdx*dudt + dvdy*dpdt + dpdy*dvdt
    
    du2dxdt = dudx*dudx + u*du2dx + dvdx*dudy + v*du2dxdy + pterm*dP2dx
    dp2dxdt = dpdx*dudx + p*du2dx + dudx*dpdx + u*dp2dx + dpdx*dvdy + p*dv2dxdy + dvdx*dpdy + v*dp2dx
    dv2dydt = dudy*dvdx + u*dv2dxdy + dvdy*dvdy + v*dv2dy + pterm*dP2dy
    dp2dydt = dpdy*dudx + p*du2dxdy + dudy*dpdx + u*dp2dxdy + dpdy*dvdy + p*dv2dy + dvdy*dpdy + v*dp2dy
    
    
    dp2dt = -1*p*du2dxdt +u*dp2dxdt + p*dv2dydt + v*dp2dydt + simpleterms
    
    
    return dp2dt
    
    
    
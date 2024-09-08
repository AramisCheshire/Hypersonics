def wall3pt1st(val1,val2,val3,val4,dx):

    #3-degree approx for 1st order at wall
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

def fwd_diff(vp1,v1,dx):
	ddx = (vp1-v1)/(2*dx)
	return ddx
	
def bck_diff(v1,vm1,dx):
	ddx=(v1-vm1)/(2*dx)
	return ddx

def dds2(vp1,v0,vm1,dx):
    ddx = (vp1+vm1-2*v0)/(2*(dx**2))
    return ddx
    
    
def ddsm(v11,v10,v01,v00,dx):
    ddx = (v11+v00-v10-v01)/(4*(dx**2))
    return ddx

def ddswall(u3,u2,u1,dx):
    dd2 = (4*u2    - u3 - 3*u1)/(2*dx)
    return dd2


def ddswall2(u4, u3,u2,u1,dx):
    dd2 = -1*(u4 - 11*u2 + 4*u3 + 6*u1)/(4*(dx**2))
    return dd2
    
    
def ddsmwalls(u21,u2m1,u11,u1m1,u01,u0m1,dx):
    n1  = 4*(u11-u1m1) -u21 + u2m1 + 3*(u01 - u0m1)
    ddm = n1/(4*(dx**2))
    return ddm

def corners(e,mesh,NumX,NumY,dx):
    u00 = mesh[e][:]
    u01 = [0,0,0,0,0,0,0]
    u02 = [0,0,0,0,0,0,0]
    u03 = [0,0,0,0,0,0,0]
    u10 = [0,0,0,0,0,0,0]
    u20 = [0,0,0,0,0,0,0]
    u30 = [0,0,0,0,0,0,0]
    u0m1 = [0,0,0,0,0,0,0]
    um10 = [0,0,0,0,0,0,0]
    u2m1= [0,0,0,0,0,0,0]
    u21 = [0,0,0,0,0,0,0]
    u11 = [0,0,0,0,0,0,0]
    u1m1 = [0,0,0,0,0,0,0]
    um1m1 = [0,0,0,0,0,0,0]
    um11 = [0,0,0,0,0,0,0]
    
    
    
    if e==0:
        #bottom left
        u10 = mesh[e+1][:]
        u20 = mesh[e+2][:]
        u30 = mesh[e+3][:]
        u01 = mesh[e+1*NumX][:]
        u02 = mesh[e+2*NumX][:]
        u03 = mesh[e+3*NumX][:]
        
        
    if e==(NumX-1):
        #bottom right
        u10 = mesh[e-1][:]
        u20 = mesh[e-2][:]
        u30 = mesh[e-3][:]
        u01 = mesh[e+1*NumX][:]
        u02 = mesh[e+2*NumX][:]
        u03 = mesh[e+3*NumX][:]
        
    if e==(NumX*NumY - 1):
        #top right
        u10 = mesh[e-1][:]
        u20 = mesh[e-2][:]
        u30 = mesh[e-3][:]
        u01 = mesh[e-NumX][:]
        u02= mesh[e-2*NumX][:]
        u03 = mesh[e-3*NumX][:]
        
    if e==(NumX*NumY-NumX):
        #top left
        u10 = mesh[e+1][:]
        u20 = mesh[e+2][:]
        u30 = mesh[e+3][:]
        u01 = mesh[e-NumX][:]
        u02 = mesh[e-2*NumX][:]
        u03 = mesh[e-3*NumX][:]
        
  
    
    
    
    #produce u,du/dx,du/dy, du/dx2 , dv/dx2
    
    
    space = []
    
    for v in (0,1,3,4):
        space.append(u00[v])
    #d/dx
    for v in (0,1,3,4):
        space.append(ddswall(u20[v],u10[v],u00[v],dx))
    #d/dy
    for v in (0,1,3,4):
        space.append(ddswall(u02[v],u01[v],u00[v],dx)) 
    #d2/dx2
    for v in (0,1,3,4):
        space.append(ddswall2(u30[v],u20[v],u10[v],u00[v],dx))
    #d2/dy2
    for v in (0,1,3,4):
        space.append(ddswall2(u03[v],u02[v],u01[v],u00[v],dx))   
    #d2/dxdy
    for v in (0,1,3,4):
        space.append(0)
    
    return space
    
    
def wallsfnc(e,mesh,NumX,NumY,dx): 
    #corners explicitly excluded
    u00 = mesh[e][:]
    u01 = [0,0,0,0,0,0,0]
    u02 = [0,0,0,0,0,0,0]
    u03 = [0,0,0,0,0,0,0]
    u10 = [0,0,0,0,0,0,0]
    u20 = [0,0,0,0,0,0,0]
    u30 = [0,0,0,0,0,0,0]
    u0m1 = [0,0,0,0,0,0,0]
    um10 = [0,0,0,0,0,0,0]
    u2m1= [0,0,0,0,0,0,0]
    u21 = [0,0,0,0,0,0,0]
    u11 = [0,0,0,0,0,0,0]
    u1m1 = [0,0,0,0,0,0,0]
    
    
    if e%NumX == 0:
        #left wall
        u10 = mesh[e+1][:]
        u20 = mesh[e+2][:]
        u30 = mesh[e+3][:]
        u10 = mesh[e+NumX][:]
        um10 = mesh[e-NumX][:]
        
        u21 = mesh[e+NumX+2][:]
        u2m1 = mesh[e-NumX+2][:]
        u11 = mesh[e+NumX+1][:]
        u1m1 = mesh[e-NumX+1][:]
        
        w = "l"
        
        
    if (e+1)%NumX==0:
        #right
        
        u10 = mesh[e-1][:]
        u20 = mesh[e-2][:]
        u30 = mesh[e-3][:]
        u10 = mesh[e+1*NumX][:]
        um10 = mesh[e-1*NumX][:]
        
        u21 = mesh[e+NumX-2][:]
        u2m1 = mesh[e-NumX-2][:]
        u11 = mesh[e+NumX-1][:]
        u1m1 = mesh[e-NumX-1][:]
        
        w = "r"
        
    if e > (NumX*NumY - NumX- 1):
        #top 
        u10 = mesh[e+1][:]
        um10 = mesh[e-1][:]
        
        u10 = mesh[e-NumX][:]
        u20= mesh[e-2*NumX][:]
        u30 = mesh[e-3*NumX][:]
        
        u21 = mesh[e-(2*NumX)+1][:]
        u2m1 = mesh[e-(2*NumX)-1][:]
        u11 = mesh[e-NumX+1][:]
        u1m1 = mesh[e-NumX-1][:]
        
        w = "t"
        
        
        
    if e < NumX:
        #bottom
        u10 = mesh[e+1][:]
        um10 = mesh[e-1 ][:]
        
        u10 = mesh[e+NumX][:]
        u20 = mesh[e+2*NumX][:]
        u30 = mesh[e+3*NumX][:]
        
        
        
        u21 = mesh[e+(2*NumX)+1][:]
        u2m1 = mesh[e+(2*NumX)-1][:]
        u11 = mesh[e+NumX+1][:]
        u1m1 = mesh[e+NumX-1][:]
        
    
        w = "b"
    
    
    #produce u,du/dx,du/dy, du/dx2 , dv/dx2
    
    
    space = []
    
    
    c = 10000
    if w == "l" or "r":
        c = 1
    elif w == "t" or "b":
        c = 0
    
    for v in (0,1,3,4):
        space.append(u00[v])
    #d/dx - for left and right, use wall func, for top/bottom, use normal dds
    for v in (0,1,3,4):
        term = ddswall(u20[v],u10[v],u00[v],dx)*c  + (1-c)*dds(u10[v],um10[v],dx)
        space.append(term)
    #d/dy -  for left and right, use normal dds, for top and bottom use wall dds
    for v in (0,1,3,4):
        term = ddswall(u20[v],u10[v],u00[v],dx)*(1-c)  + c*dds(u10[v],um10[v],dx)
        space.append(term)
    #d2/dx2
    for v in (0,1,3,4):
        space.append(0)#space.append(ddswall2(u30[v],u20[v],u10[v],u00[v],dx))
    #d2/dy2
    for v in (0,1,3,4):
        space.append(0)#space.append(ddswall2(u03[v],u02[v],u01[v],u00[v],dx))   
    #d2/dxdy
    for v in (0,1,3,4):
        space.append(0)#space.append(ddsmwalls(u21[v],u2m1[v],u11[v],u1m1[v],u01[v],u0m1[v],dx))
    
    return space
   

def Balls2theWalls(e,mesh,NumX,NumY,dx):
    #4 parameters: u,v,p,P
    #6 space derivatives for each - store in a 24-item array
    #9 mesh points are required - meaning, 36 different values
    #segregate walls and corners
    
    
    #start by generating values
    
    #corners
    
    
    
    #no walls:
    
    u00 = mesh[e][:]
    u10 = mesh[e+1][:]
    um10 = mesh[e-1][:]
    u01 = mesh[e+NumX][:]
    u0m1 = mesh[e-NumX][:]
    u11 = mesh[e+NumX+1][:]
    u1m1 = mesh[e+1-NumX][:]
    um11 = mesh[e-1+NumX][:]
    um1m1 = mesh[e-NumX-1][:]
    
    #now we want to create 24 space derivatives
    
    
    space = []
    #u
    for v in (0,1,3,4):
        space.append(u00[v])
    #d/dx
    for v in (0,1,3,4):
        space.append(dds(u10[v],um10[v],dx))
    #d/dy
    for v in (0,1,3,4):
        space.append(dds(u01[v],u0m1[v],dx)) 
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
    
    
def governing_2d(s):
    RT = s[3]/s[2]

    #need to return [du/dt, d2u/dt2, dv/dt, d2v/dt2, dp/dt, d2p/dt2, dP/dt, d2P/dt2]
    Q = 4 #four quantities - u,v,p,P
    
    #first order:
    dpdt = -1*(s[2]*s[0+Q] + s[0]*s[2+Q] + s[2]*s[1+2*Q] + s[1]*s[2+2*Q])
    
    dudt = -1*(s[0]*s[0+Q] + s[1]*s[0+2*Q] + (1/s[2])*s[3+Q])
    
    dvdt = -1*(s[0]*s[1+Q] + s[1]*s[1+2*Q] + (1/s[2])*s[3+2*Q])
    
    dPdt = dpdt*RT
    
    
    
    #space mixes:
    
    #---------------------------------------dp/dt *d/dx and d/dy

    
    """
    d2p/dtdx:
    term1: dp/dx * du/dx + p*d2u/dx2 
    term2: du/dx * dp/dx + u * d2p/dx2
    term3: dp/dx * dv/dy + p * d2v/dxdy 
    term4: dv/dx*dp/dy + v*d2p/dxdy
    """
    
    term1 = s[2+Q]*s[0+Q] + s[2]*s[0+3*Q]
    term2 = s[0+Q]*s[2+Q] + s[0]*s[2+3*Q]
    term3 = s[2+Q]*s[1+2*Q] + s[2]*s[1+5*Q]
    term4 = s[1+Q]*s[2+2*Q] + s[1]*s[2+5*Q]
    
    dpdxdt = -1*(term1 + term2 + term3+ term4)
    
    """
    d2p/dtdy:
    term1: dp/dy * du/dx + p*d2u/dxdy 
    term2: du/dy * dp/dx + u * d2p/dxdy
    term3: dp/dy * dv/dy + p * d2v/dy2 
    term4: dv/dy*dp/dy + v*d2p/dy2
    """
    
    term1 = s[2+2*Q]*s[0+Q] + s[2]*s[0+5*Q]
    term2 = s[0+2*Q]*s[2+Q] + s[0]*s[2+5*Q]
    term3 = s[2+2*Q]*s[1+2*Q] + s[2]*s[1+4*Q]
    term4 = s[1+2*Q]*s[2+2*Q] + s[1]*s[2+4*Q]
    
    dpdydt = -1*(term1 + term2 + term3+ term4)  
    
    #---------------------------------------du/dt *d/dx and d/dy

    """
    d2u/dtdx:
    term1: du/dx * du/dx + u*d2u/dx2 
    term2: dv/dx * du/dy + v * d2u/dxdy
    term3: dp/dx * (-p^(-2)) * dP/dx + (1/p) * d2P/dx2 
    """
    
    term1 = s[0+Q]*s[0+Q] + s[0]*s[0+3*Q]
    term2 = s[1+Q]*s[0+2*Q] + s[1]*s[0+5*Q]
    term3 = s[2+Q]*s[3+Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*s[3+3*Q]
    dudxdt = -1*(term1 + term2 + term3)     
    
    
 


    """
    d2u/dtdy:
    term1: du/dy * du/dx + u*d2u/dxdy 
    term2: dv/dy * du/dy + v * d2u/dy2
    term3: dp/dy * (-p^(-2)) * dP/dx + (1/p) * d2P/dxdy    
    """
    
    term1 = s[0+2*Q]*s[0+Q] + s[0]*s[0+5*Q]
    term2 = s[1+2*Q]*s[0+2*Q] + s[1]*s[0+4*Q]
    term3 = s[2+2*Q]*s[3+Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*s[3+5*Q]
    dudydt = -1*(term1 + term2 + term3)  
    
    
    
    #---------------------------------------dv/dt *d/dx and d/dy
    
    """
    d2v/dtdx:
    term1: du/dx * dv/dx + u*d2v/dx2 
    term2: dv/dx * dv/dy + v * d2v/dxdy
    term3: dp/dx * (-p^(-2)) * dP/dy + (1/p) * d2P/dxdy 
    """
    
    term1 = s[0+Q]*s[1+Q] + s[0]*s[1+3*Q]
    term2 = s[1+Q]*s[1+2*Q] + s[1]*s[1+5*Q]
    term3 = s[2+Q]*s[3+2*Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*s[3+5*Q]
    dvdxdt = -1*(term1 + term2 + term3)    
    
    
    
    """
    d2v/dtdy:
    term1: du/dy * dv/dx + u*d2v/dxdy 
    term2: dv/dy * dv/dy + v * d2v/dy2
    term3: dp/dy * (-p^(-2)) * dP/dy + (1/p) * d2P/dy2    
    """
    
    term1 = s[0+2*Q]*s[1+Q] + s[0]*s[1+5*Q]
    term2 = s[1+2*Q]*s[1+2*Q] + s[1]*s[1+4*Q]
    term3 = s[2+2*Q]*s[3+2*Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*s[3+4*Q]
    dvdydt = -1*(term1 + term2 + term3)     
    
    
    
    
    
    #---------------------------------------now I have enough info to calc second order time derivs

   
    """
    d2p/dt2 = 
    term1: dp/dt * du/dx + p* du2/dxdt 
    term2: du/dt * dp/dx + u*d2p/dxdt 
    term3: dp/dt * dv/dy + p*dv2/dydt
    term4: dv/dt * dp/dy + v*d2p/dydt
    """
    
    term1 = dpdt*s[0+Q] + s[2]*dudxdt
    term2 = dudt*s[2+Q] + s[0]*dpdxdt
    term3 = dpdt*s[1+2*Q] + s[2]*dvdydt
    term4 = dvdt*s[2+2*Q] + s[1]*dpdydt
    
    dp2dt2 = term1 + term2 + term3 +term4
    
    
    
    """
    d2u/dt2 = 
    term1: du/dt * du/dx + u* du2/dxdt 
    term2: dv/dt * du/dy + v*d2u/dydt 
    term3: dp/dt * dP/dx *(-p**-2)  + (1/p)*dpdxdt*RT
    
    """
    
    term1 = dudt*s[0+Q] + s[0]*dudxdt
    term2 = dvdt*s[0+2*Q] + s[1]*dudydt
    term3 = dpdt*s[3+Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*dpdxdt*RT
    
    du2dt2 = term1 + term2 + term3 
    
    
    
    
    """
    d2v/dt2 = 
    term1: du/dt * dv/dx + u* dv2/dxdt 
    term2: dv/dt * dv/dy + v*d2v/dydt 
    term3: dp/dt * dP/dy *(-p**-2)  + (1/p)*dpdydt*RT
    
    """
    
    term1 = dudt*s[1+Q] + s[0]*dvdxdt
    term2 = dvdt*s[1+2*Q] + s[1]*dvdydt
    term3 = dpdt*s[3+2*Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*dpdydt*RT
    
    dv2dt2 = term1 + term2 + term3     
    
    
    dP2dt2 = dp2dt2*RT
    
    dudx = s[4]
 #   print("in governing_2d")



   # h = [dudt,s[0],s[4],s[1],s[9],(1/s[2]),s[7]]
    
   # print(h)
    return [dudt,dvdt,dpdt,dPdt,du2dt2,dv2dt2,dp2dt2,dP2dt2] 




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
def governing_2d(s):
    RT = s[3]/s[2]

    #need to return [du/dt, d2u/dt2, dv/dt, d2v/dt2, dp/dt, d2p/dt2, dP/dt, d2P/dt2]
    Q = 4 #four quantities - u,v,p,P
    
    #first order:
    dpdt = -1*(s[2]*s[0+Q] + s[0]*s[2+Q] + s[2]*s[1+2*Q] + s[1]*s[2+2*Q])
    
    dudt = -1*(s[0]*s[0+Q] + s[1]*s[0+2*Q] + (1/s[2])*s[3+Q])
    
    dvdt = -1*(s[0]*s[1+Q] + s[1]*s[1+2*Q] + (1/s[2])*s[3+2*Q])
    
    dPdt = dpdt*RT
    
    
    
    #space mixes:
    
    #---------------------------------------dp/dt *d/dx and d/dy

    
    """
    d2p/dtdx:
    term1: dp/dx * du/dx + p*d2u/dx2 
    term2: du/dx * dp/dx + u * d2p/dx2
    term3: dp/dx * dv/dy + p * d2v/dxdy 
    term4: dv/dx*dp/dy + v*d2p/dxdy
    """
    
    term1 = s[2+Q]*s[0+Q] + s[2]*s[0+3*Q]
    term2 = s[0+Q]*s[2+Q] + s[0]*s[2+3*Q]
    term3 = s[2+Q]*s[1+2*Q] + s[2]*s[1+5*Q]
    term4 = s[1+Q]*s[2+2*Q] + s[1]*s[2+5*Q]
    
    dpdxdt = -1*(term1 + term2 + term3+ term4)
    
    """
    d2p/dtdy:
    term1: dp/dy * du/dx + p*d2u/dxdy 
    term2: du/dy * dp/dx + u * d2p/dxdy
    term3: dp/dy * dv/dy + p * d2v/dy2 
    term4: dv/dy*dp/dy + v*d2p/dy2
    """
    
    term1 = s[2+2*Q]*s[0+Q] + s[2]*s[0+5*Q]
    term2 = s[0+2*Q]*s[2+Q] + s[0]*s[2+5*Q]
    term3 = s[2+2*Q]*s[1+2*Q] + s[2]*s[1+4*Q]
    term4 = s[1+2*Q]*s[2+2*Q] + s[1]*s[2+4*Q]
    
    dpdydt = -1*(term1 + term2 + term3+ term4)  
    
    #---------------------------------------du/dt *d/dx and d/dy

    """
    d2u/dtdx:
    term1: du/dx * du/dx + u*d2u/dx2 
    term2: dv/dx * du/dy + v * d2u/dxdy
    term3: dp/dx * (-p^(-2)) * dP/dx + (1/p) * d2P/dx2 
    """
    
    term1 = s[0+Q]*s[0+Q] + s[0]*s[0+3*Q]
    term2 = s[1+Q]*s[0+2*Q] + s[1]*s[0+5*Q]
    term3 = s[2+Q]*s[3+Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*s[3+3*Q]
    dudxdt = -1*(term1 + term2 + term3)     
    
    
 


    """
    d2u/dtdy:
    term1: du/dy * du/dx + u*d2u/dxdy 
    term2: dv/dy * du/dy + v * d2u/dy2
    term3: dp/dy * (-p^(-2)) * dP/dx + (1/p) * d2P/dxdy    
    """
    
    term1 = s[0+2*Q]*s[0+Q] + s[0]*s[0+5*Q]
    term2 = s[1+2*Q]*s[0+2*Q] + s[1]*s[0+4*Q]
    term3 = s[2+2*Q]*s[3+Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*s[3+5*Q]
    dudydt = -1*(term1 + term2 + term3)  
    
    
    
    #---------------------------------------dv/dt *d/dx and d/dy
    
    """
    d2v/dtdx:
    term1: du/dx * dv/dx + u*d2v/dx2 
    term2: dv/dx * dv/dy + v * d2v/dxdy
    term3: dp/dx * (-p^(-2)) * dP/dy + (1/p) * d2P/dxdy 
    """
    
    term1 = s[0+Q]*s[1+Q] + s[0]*s[1+3*Q]
    term2 = s[1+Q]*s[1+2*Q] + s[1]*s[1+5*Q]
    term3 = s[2+Q]*s[3+2*Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*s[3+5*Q]
    dvdxdt = -1*(term1 + term2 + term3)    
    
    
    
    """
    d2v/dtdy:
    term1: du/dy * dv/dx + u*d2v/dxdy 
    term2: dv/dy * dv/dy + v * d2v/dy2
    term3: dp/dy * (-p^(-2)) * dP/dy + (1/p) * d2P/dy2    
    """
    
    term1 = s[0+2*Q]*s[1+Q] + s[0]*s[1+5*Q]
    term2 = s[1+2*Q]*s[1+2*Q] + s[1]*s[1+4*Q]
    term3 = s[2+2*Q]*s[3+2*Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*s[3+4*Q]
    dvdydt = -1*(term1 + term2 + term3)     
    
    
    
    
    
    #---------------------------------------now I have enough info to calc second order time derivs

   
    """
    d2p/dt2 = 
    term1: dp/dt * du/dx + p* du2/dxdt 
    term2: du/dt * dp/dx + u*d2p/dxdt 
    term3: dp/dt * dv/dy + p*dv2/dydt
    term4: dv/dt * dp/dy + v*d2p/dydt
    """
    
    term1 = dpdt*s[0+Q] + s[2]*dudxdt
    term2 = dudt*s[2+Q] + s[0]*dpdxdt
    term3 = dpdt*s[1+2*Q] + s[2]*dvdydt
    term4 = dvdt*s[2+2*Q] + s[1]*dpdydt
    
    dp2dt2 = term1 + term2 + term3 +term4
    
    
    
    """
    d2u/dt2 = 
    term1: du/dt * du/dx + u* du2/dxdt 
    term2: dv/dt * du/dy + v*d2u/dydt 
    term3: dp/dt * dP/dx *(-p**-2)  + (1/p)*dpdxdt*RT
    
    """
    
    term1 = dudt*s[0+Q] + s[0]*dudxdt
    term2 = dvdt*s[0+2*Q] + s[1]*dudydt
    term3 = dpdt*s[3+Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*dpdxdt*RT
    
    du2dt2 = term1 + term2 + term3 
    
    
    
    
    """
    d2v/dt2 = 
    term1: du/dt * dv/dx + u* dv2/dxdt 
    term2: dv/dt * dv/dy + v*d2v/dydt 
    term3: dp/dt * dP/dy *(-p**-2)  + (1/p)*dpdydt*RT
    
    """
    
    term1 = dudt*s[1+Q] + s[0]*dvdxdt
    term2 = dvdt*s[1+2*Q] + s[1]*dvdydt
    term3 = dpdt*s[3+2*Q]*(-1)*(1/(s[2]**2)) + (1/s[2])*dpdydt*RT
    
    dv2dt2 = term1 + term2 + term3     
    
    
    dP2dt2 = dp2dt2*RT
    
    dudx = s[4]
 #   print("in governing_2d")



   # h = [dudt,s[0],s[4],s[1],s[9],(1/s[2]),s[7]]
    
   # print(h)
    return [dudt,dvdt,dpdt,dPdt,du2dt2,dv2dt2,dp2dt2,dP2dt2] 
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


"""
def maccormack_interior(e,mesh,NumX,NumY,dx):


    #no walls, need to generate space=[u,v,p,P,dudx,dvdx,...etc] 
    #24 elements in totla 

    space = []
    #u (no derivative)
    for v in (0,1,3,4):
        space.append(u00[v])
    #d/dx - fwd difference
    for v in (0,1,3,4):
        space.append(dds(u10[v],u00[v],dx))

    #d/dy - fwd difference 
    for v in (0,1,3,4):
        space.append(dds(u01[vi
    
"""

def firstorder_governing_2D(s):
    RT = s[3]/s[2]
    Q=4

    dpdt = -1*(s[2]*s[0+Q] + s[0]*s[2+Q] + s[2]*s[1+2*Q] + s[1]*s[2+2*Q])
    
    dudt = -1*(s[0]*s[0+Q] + s[1]*s[0+2*Q] + (1/s[2])*s[3+Q])
    
    dvdt = -1*(s[0]*s[1+Q] + s[1]*s[1+2*Q] + (1/s[2])*s[3+2*Q])
    
    dPdt = dpdt*RT
    
    ders=[dpdt,dudt,dvdt,dPdt]
    return ders

def maccormack_interior_predictor(e,mesh,NumX,NumY,dx,dt):

    #need to calculate predicted variables for entire grid using fwd difference

    #assume only interiors
    
    #6 points around element e
    u00 = mesh[e][:]
    u10 = mesh[e+1][:]
    um10 = mesh[e-1][:]
    u01 = mesh[e+NumX][:]
    u0m1 = mesh[e-NumX][:]
    
    
    #use these points to calculate 1st order derivatives
    
    s = []

    #no derivative
    for v in (0,1,3,4):
        s.append(u00[v])

    for v in (0,1,3,4):
        s.append(dds(u10[v],u00[v]))

    #d/dy 
    for v in (0,1,3,4):
        s.append(dds(u01[v],u00[v]))

    #now i have s=[u,v,p,P,ux,vx,px,Px,uy,vy,py,Py] = 12 elements





    # RT from that ideal gas eqn. s[3] = Pressure, s[2] = density p
    RT = s[3]/s[2]
    Q=4 #skip down a row in space, i.e. from [0..3] to [4..7]

    #first order eqns:

    ders = firstorder_governing_2D(s)

    #now i can predict values of next timestep:
    u00t = u00[:]
    u00t[0]= u00[0] + dt*ders[1]
    
    


    return 0


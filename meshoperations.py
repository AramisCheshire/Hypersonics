def displaymeshsymbols(mesh,NumX,NumY):
    ss = ""
    k = 0
    for item in range(0,len(mesh)):
        ss = ss + "%s"%(mesh[item])
        k = k +1
        if k == NumX:
           
            print(ss)
            ss = ""
            k = 0
            
def displaymeshnumbers(mesh,NumX,NumY,property):
    ss = ""
    k = 0
    for item in range(0,len(mesh)):
        ss = ss + "%i"%(mesh[item][property])
        k = k +1
        if k == NumX:
           
            print(ss)
            ss = ""
            k = 0
 
def Elems(x,y,dx):
    import math
    NumX = math.floor(x/dx) + 1
    NumY = math.floor(y/dx) + 1
    
    return [NumX,NumY]
    
def create2Dmesh(NumX,NumY):


    #now, create a multi-D array where the position of the element reveals whether its x or y based
    #every NumX elements = one y value, repeat NumY times

    mesh = []
    for i in range(0,NumX*NumY):
        #prop can be loaded from a settings file or a dictionary variable
        prop = [0,0,0,1.225,100,292,1.4]
        mesh.append(prop)
    
    return mesh

def create2DmeshEmpty(NumX,NumY):


#now, create a multi-D array where the position of the element reveals whether its x or y based
#every NumX elements = one y value, repeat NumY times

    mesh = []
    for i in range(0,NumX*NumY):
        #prop can be loaded from a settings file or a dictionary variable
        mesh.append(0)

    return mesh      
    
    
    
def create2DwallEmpty(NumX,NumY):


#now, create a multi-D array where the position of the element reveals whether its x or y based
#every NumX elements = one y value, repeat NumY times

    mesh = []
    for i in range(0,NumX*NumY):
        #prop can be loaded from a settings file or a dictionary variable
        mesh.append(".")

    return mesh    
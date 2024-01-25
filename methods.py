def wall3pt1st(val1,val2,val3,val4,dx):
    ddx =(-11*val1 + 18*val2 - 9*val3 + 2*val4)/(6*dx)
    return ddx

def central2nd(val1,val2,val3,dx):
	d2x2 =(val3 - 2*val2 + val1)/(dx**2)
	return d2x2


def central1st(val1,val3,dx):
    ddx = (val3-val1)/2*dx
    return ddx

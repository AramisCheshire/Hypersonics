from hyper import oblique
from hyper import oblique_limit
from hyper import ThetaBeta

#velocity vector = [ Vx, Vy, Vz]
vel1 = [3360,0,0]
#props = [V (m/s),a (m/s) ,P (kPa) ,p (kg/m3) ,T (K), y]
flow1 = [vel1,336,100,1.225,300, 1.4]

#ThetaBeta(M1,Bdeg,y):

thetas = []
Betas = []
for i in range(1,180):
		k = i/2
		Betas.append(k)
		theta = ThetaBeta(3,k,1.4)
		thetas.append(theta)

#now need to plot thetas and betas

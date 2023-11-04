#this file is for testing all of the functions in hyper_git
from hyper_git import oblique
from hyper_git import oblique_limit
from hyper_git import ThetaBeta

"""---------------main-------------"""


print("A program to calculate flowfields for hypersonic flows")
print("Start with property change across an oblique shock")
print("starting with default flow properties")

#velocity vector = [ Vx, Vy, Vz]
vel1 = [3360,0,0]
#props = [V (m/s),a (m/s) ,P (kPa) ,p (kg/m3) ,T (K), y]
flow1 = [vel1,336,100,1.225,300, 1.4]


print("original: ")
print(flow1)
print("exact: ")
flow2_ex = oblique(flow1,10)
print(flow2_ex)
print("at limit: ")
flow2_lim = oblique_limit(flow1,10)
print(flow2_lim)


#some math checks - delete later
#flow1 = [vel1,336,100,1.225,300, 1.4]

R1 = flow1[2]*1000/(flow1[3]*flow1[4])

R2 = flow2_ex[2]*1000/(flow2_ex[3]*flow2_ex[4])
print(R1)
print(R2)


R4 = flow2_lim[2]*1000/(flow2_lim[3]*flow2_lim[4])
print(R4)


theta = ThetaBeta(10,10,1.4)
print(theta)
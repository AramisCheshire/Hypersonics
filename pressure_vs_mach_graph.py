import matplotlib.pyplot as plt
from hyper import oblique_limit


vel1 = [2444, 0, 0]
flow1 = [vel1, 323, 132, 1.225, 200, 1.4]
mach_values = []
pressure = []
generated_mach_values = []
tmp = []


x = 0
while x < 40 :
      x = x + 1
      mach_values.append(x)

print('Initial_mach_values: ')
print(mach_values)


for m in mach_values :

    tmp = flow1
    tmp[0][0] = m * tmp[1] # m is vx, tmp[1] is a.
    x = oblique_limit(tmp, 10)
    p2 = x[2]
    pressure.append(p2)
    vx = x[0][0]
    a = x[1]
    mach = vx / a
    generated_mach_values.append(mach)



print('Pressure: ', pressure)
print('mach: ', mach_values)

plt.plot(mach_values, pressure)
plt.xlabel('mach_values')
plt.ylabel('Pressure ')
plt.title('Pressure vs. Mach ')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
from hyper import oblique_limit


vel1 = [2444, 0, 0]
flow1 = [vel1, 323, 132, 1.225, 200, 1.4]
mach_values = [4, 23, 43, 45, 123]
pressure = []
generated_mach_values = []

tmp = []

for m in mach_values :

    tmp = flow1
    tmp[0][0] = m * tmp[1]
    x = oblique_limit(tmp, 10)
    p2 = x[2]
    pressure.append(p2)
    vx = x[0][0]
    a = x[1]
    mach = vx / a
    generated_mach_values.append(mach)



print('Pressure: ', pressure)
print('mach: ', generated_mach_values)

plt.plot(pressure, generated_mach_values)
plt.xlabel('Pressure')
plt.ylabel('Mach ')
plt.title('Pressure vs. Mach ')
plt.grid(True)
plt.show()

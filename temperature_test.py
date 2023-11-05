from flowgen import Mair
from hyper import oblique_limit
from hyper import oblique


beta_values = []
beta_dic = {}
tmp = []

flow1 = Mair(10)
print(flow1)

beta = 0

while beta < 90 :
    beta = beta + 1
    beta_values.append(beta)


beta = 0

for b in beta_values:
    result = oblique_limit(flow1, b)
    t = result[4]
    beta = beta + 1
    print(beta, t)
    beta_dic[beta] = t

print(beta_dic)

highest_temperature = None
lowest_temperature = None

for b,t in beta_dic.items():
    if highest_temperature is None or t > highest_temperature:
        highest_temperature = t
    if lowest_temperature is None or t < lowest_temperature:
        lowest_temperature = t

print('highest_temperature: ', highest_temperature)
print('Lowest_temperature: ', lowest_temperature)

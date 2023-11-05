#functions for generating flow arrays (e.g. flow1)

def Mair(M):
	#this function uses the pressure, temperature, density values of air of the "International Standard Atmosphere" as defined by ICAO https://en.wikipedia.org/wiki/Standard_temperature_and_pressure
	#which is 101.325kPa pressure i.e. atmospheric pressure at sea level, 15C temperature and 1.225kg/m3 density
	#it only takes the user's desired mach value as an input and generates the array
	#note that speed of sound of air depends on its temperature
	#note that the flow array uses temperature in Kelvin not in Celsius. To convert to Kelvin, you simply add +273 to a reading in celsius.
	
	y = 1.401 #Specific heat ratio of dry air - at 15C https://www.engineeringtoolbox.com/specific-heat-ratio-d_602.html
	R = 287.052874 #R-specific of dry air, https://en.wikipedia.org/wiki/Gas_constant
	T = 288.15 #this is 15C + 273.15 kelvin
	a = pow(y*R*T,0.5) #speed of sound formula
	
	P = 101325 #in Pascals, Pa
	p = 1.225 #kg/m3
	
	Vx = M*a
	return [[Vx,0,0],a,P,p,T,y]

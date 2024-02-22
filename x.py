import numpy as np
from PIL import Image

# Parameters

N = 10000  
NumX = 100 
NumY = N // NumX 
threshold_temperature = 30  # 30 and above

# random array for experiment
   
temperatures = np.random.uniform(0, 99, N)  # Random temperatures from 0 to 100

#  matrix (100x100)

temperature_matrix = temperatures.reshape((NumX, NumY))


# Generating blank heatmap 

heatmap_image = Image.new('RGB' , (NumX, NumY), 'white')  


# Mapping temperatures (cold = blue, hot = red)

for x in range(temperature_matrix.shape[0]):
    for y in range(temperature_matrix.shape[1]):
        if temperature_matrix[x, y] < threshold_temperature:
            
            blue = (0, 0, 255)
            heatmap_image.putpixel((x, y), blue)

        
        else:

            red = (255, 0, 0)
            heatmap_image.putpixel((x, y), red)
        

heatmap_image.save('heatmap.bmp', 'BMP')
heatmap_image.show()
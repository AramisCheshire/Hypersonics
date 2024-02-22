#a python script for producing .bmp images of the solver

import sys
sys.path.append("C:\\Users\\David\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages")

#import PIL #pillow- library for creating image files
import PIL

def createimage(mesh,NumX,NumY,prop):
    
    
    


    # Generating blank heatmap 

    heatmap_image = PIL.Image.new('RGB' , (NumX, NumY), 'white')  
    
    
    #go pixel by pixel and write color
    
    for y in range(NumY):
        for x in range(NumX):
            heatmap_image.putpixel((x,y),(0,0,244))
            
            
    heatmap_image.save('heatmap.bmp','BMP')
    
            



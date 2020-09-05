import pyautogui
from PIL import Image,ImageGrab
import time


#Function to press key
def hit(key):
    pyautogui.keyDown(key)
    return

#Function to check for obstacles 
def obstacle(data):
    day=True
    
    #we will check whether its day or night 
    if data[990,252]==138:
        day=False
    
    if day:  
        for i in range(310,340):
            for j in range(470,510):
                if data[i,j] < 100:
                    hit("up")
                    return   
        for i in range(310,340):
            for j in range(380,410):
                if data[i,j] < 50:
                    hit("down")
                    return 
        return 
    
    else:
        for i in range(310,340):
            for j in range(470,510):
                if data[i,j] > 100:
                    hit("up")
                    return 
        for i in range(310,340):
            for j in range(380,410):
                if data[i,j] > 50:
                    hit("down")
                    return 
        return
    
    return



if __name__ == "__main__":
    print("the game will start in 3 seconds move to the game Window")
    time.sleep(3)
    
    while True:
        image=ImageGrab.grab().convert("L")
        data=image.load()
        obstacle(data)
        


        
        #things i used to debug various aspects of this project
        #print(data[1,1])   

        #for i in range(310,340):
            #for j in range(380,410):
               #data[i,j]=0

        #for i in range(290,315):
            #for j in range(400,440):
               #data[i,j] = 100
                    

        #image.show()
        #break

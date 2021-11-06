import time
import dropbox 
import random 
import cv2

start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    #init cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        #read the frames
        ret,frame = videoCaptureObject.read()
        #cv2 imwrite
        img_name= "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot Taken" )
    
    #release camera
    videoCaptureObject.release()

    #close all video might open while this process
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(img_name):
    access_token =""

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)
main()


import cv2 

def take_snapshot():
    #intializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while camera is on
        ret,frame=videoCaptureObject.read()
        print(ret)
        #cv2.imwrite() is used to save an image to any storage device
        cv2.imwrite("./picture.jpg",frame)
        result=False
    #release the camera
    videoCaptureObject.release()
    #close the window that might be open while this process
    cv2.destroyAllWindows()

take_snapshot()
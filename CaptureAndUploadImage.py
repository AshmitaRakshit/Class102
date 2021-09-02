import cv2
import dropbox
import time
import random

start_time=time.time()
print(start_time)

def take_snapshot():
    number=random.randint(0,100)
    #intializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while camera is on
        ret,frame=videoCaptureObject.read()
        print(ret)
        #cv2.imwrite() is used to save an image to any storage device
        img_name="picture"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("Snapshot taken")

    #release the camera
    videoCaptureObject.release()
    #close the window that might be open while this process
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "DKyGxRcwC9QAAAAAAAAAATbMIMLGPPrFl2rJomX3coHCJrJKFcA-sDFSA3CBSTXq"
    file =img_name
    file_from = file
    file_to="/AshmitaPython/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()  

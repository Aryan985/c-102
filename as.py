import cv2
import dropbox
import time
import random
strtime = time.time()
def capture():
    num = random.randint(0,100)
    image = cv2.VideoCapture(0)
    result = True
    while result:
        ret,frame = image.read()
        imgName = "img"+str(num)+".png"
        cv2.imwrite(imgName,frame)
        strtime = time.time()
        result = False
    return imgName
    image.release()
    cv2.destroyAllWindows()
def upload(imgName):
    accessToken = ""
    dbx=dropbox.Dropbox(self.access_token)
    filefrom = imgName
    fileto = "/security/"+imgName
    f = open(filefrom,"rb")
    dbx.files_upload(f.read(),to,mode=dropbox.files.WriteMode.overwrite)
    print("File Uploaded")
def main():
    while(True):
        if((time.time()-strtime)>=5):
            name = capture()
            upload(name)
main()
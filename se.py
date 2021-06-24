import cv2
def capture():
    image = cv2.VideoCapture(0)
    result = True
    while result:
        ret,frame = image.read()
        cv2.imwrite("security.png",frame)
        result = False
    image.release()
    cv2.destroyAllWindows()
capture()
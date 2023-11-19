import cv2
img = cv2.imread("teddy.jpg")
cv2.imshow("Click me", img)
cv2.resizeWindow("Click me",1200,800)
def show_rectandle(event, x, y, flags, params):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+15,y+15),(0,0,0),15)
        cv2.imshow("Click me", img)
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.destroyAllWindows()
cv2.setMouseCallback("Click me",show_rectandle)
cv2.waitKey(0)
cv2.destroyAllWindows()

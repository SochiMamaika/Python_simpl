import cv2
def show_rectandle(event, x, y, flags, params):
    print("in function",k)
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+10,y+10),(0,0,0),10)
        cv2.imshow("Click me", img)
        return 0
    else:
        cv2.imshow("Click me", img)
        return 0
k=0
print("before while",k)
while(True):
    print("in while",k)
    img = cv2.imread("teddy.jpg")
    cv2.imshow("Click me", img)
    cv2.setMouseCallback("Click me",show_rectandle)
    k+=1
    print(k)
    if k>=1:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()

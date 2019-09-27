def select_point(event,x,y,flags,params):
    global point, point_selected
    if event==cv2.EVENT_LBUTTONDOWN:
        point=(x,y)
        point_selected=True
cv2.namedWindow("Video")
cv2.setMouseCallback("Video",select_point)
        
point_selected=False
point=()
old_points=np.array([[]])

capture=cv2.VideoCapture(0)
# creating old frames

r,frame=capture.read()
old_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

while True:
    ret,frame=capture.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    
    
    if point_selected==True:
        cv2.circle(frame, point,4,(255,0,0),2)
        new_point,status, error=cv2.calcOpticalFlowPyrLK(old_gray,gray_frame,old_points,None,**lk_params)
        old_gray=gray_frame.copy()
    cv2.imshow("Video",frame)   
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
capture.release()
        
cv2.destroyAllWindows()
        

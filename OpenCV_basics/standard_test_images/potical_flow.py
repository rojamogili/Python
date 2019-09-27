def select_point(event,x,y,flags,params):
    global point, point_selected,old_points
    if event==cv2.EVENT_LBUTTONDOWN:
        point=(x,y)
        point_selected=True
        old_points=np.array([[x,y]],dtype=np.float32)
cv2.namedWindow("Video")
cv2.setMouseCallback("Video",select_point)
        
point_selected=False
point=()
old_points=np.array([[]])

capture=cv2.VideoCapture(0)
# creating old frames

r,frame=capture.read()
old_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

# lucas kanade params
lk_params=dict(winSize=(10,10),maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.03))

while True:
    ret,frame=capture.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    
    
    if point_selected==True:
        cv2.circle(frame, point,4,(255,0,0),2)
        new_point,status, error=cv2.calcOpticalFlowPyrLK(old_gray,gray_frame,old_points,None,**lk_params)
        old_gray=gray_frame.copy()
        old_points=new_point
        x,y=new_point.ravel()
        
        cv2.circle(frame,(x,y),5,(255,0,0),2)
    cv2.imshow("Video",frame)   
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
capture.release()
        
cv2.destroyAllWindows()
        

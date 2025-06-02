import numpy as np
from PIL import Image
import cv2

yellow = [0, 255, 255]  # BGR format for yellow 
def get_limit(color):
    c = np.uint8([[color]])  # Correctly reshape the input
    hsv_color = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    lower_limit = np.array([hsv_color[0][0][0] - 10, 100, 100], dtype=np.uint8)
    upper_limit = np.array([hsv_color[0][0][0] + 10, 255, 255], dtype=np.uint8)
    return lower_limit, upper_limit

cap=cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit = get_limit(yellow)
    mask= cv2.inRange(hsv_frame, lower_limit, upper_limit)
    mask_= Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
    
cap.release()
cv2.destroyAllWindows()
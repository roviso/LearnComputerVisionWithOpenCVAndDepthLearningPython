import cv2
img = cv2.imread('./DATA/00-puppy.jpg')

cv2.imshow('Puppy', img)
    
while True:

    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()

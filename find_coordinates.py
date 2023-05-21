# Ref: https://www.tutorialspoint.com/opencv-python-how-to-display-the-coordinates-of-points-clicked-on-an-image
import cv2

# define a function to display the coordinates of the points clicked on the image
def click_event(event, x, y, flags, params):
   if event == cv2.EVENT_LBUTTONDOWN:
      print(f'({x},{y})')

      img_shape = img.shape
      txt_x = x
      txt_y = y

      if (x + 50 >= img_shape[1]):
        txt_x = txt_x - 80
        txt_y = txt_y + 10

      # put coordinates as text on the image
      cv2.putText(img, f'({x},{y})',(txt_x,txt_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
      
      # draw point on the image
      cv2.circle(img, (x,y), 3, (0,255,255), -1)
 
# read the input image
img = cv2.imread('images/book1.jpg')

# create a window
cv2.namedWindow('Point Coordinates')

# bind the callback function to window
cv2.setMouseCallback('Point Coordinates', click_event)

# display the image
while True:
   cv2.imshow('Point Coordinates',img)
   k = cv2.waitKey(1) & 0xFF
   if k == 27:
      break
   
cv2.imwrite('images/book1_coord.jpg', img)
cv2.destroyAllWindows()
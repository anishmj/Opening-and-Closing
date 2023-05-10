# Opening-and-Closing

## Aim
To implement Opening and Closing using Python and OpenCV.

## Software Required
1. Anaconda - Python 3.7
2. OpenCV
## Algorithm:
### Step 1:
Import the necessary packages.

### Step 2:
Create the Text using cv2.putText.

### Step 3:
Create the structuring element.

### Step 4:
Use Opening operation.

### Step 5:
Use Closing Operation.

### Step 6:
Print the output and end the program.
 
## Program:
~~~
DEVELOPED BY : ANISH M J
REGISTER NO : 212221230005
~~~


``` Python
# Import the necessary packages
import cv2
import numpy as np


# Create the Text using cv2.putText
img = np.zeros((100,400),dtype = 'uint8')
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img,'ANISH M J',(5,70),font,2,(255,0,255),5,cv2.LINE_AA)


# Create the structuring element

kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))

# Use Opening operation
image_open=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow("open",image_open)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Use Closing Operation

image_close=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow("close",image_close)
cv2.waitKey(0)
cv2.destroyAllWindows()



```
## Output:

### Display the input Image
![p](input.png)

### Display the result of Opening
![p](open.png)

### Display the result of Closing
![p](close.png)

## Result
Thus the Opening and Closing operation is used in the image using python and OpenCV.
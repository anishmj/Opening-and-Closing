#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


img = np.zeros((100,400),dtype = 'uint8')
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img,'ANISH M J',(5,70),font,2,(255,0,255),5,cv2.LINE_AA)


# In[3]:


kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))


# In[7]:


cv2.imshow("input",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


image_open=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow("open",image_open)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


image_close=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow("close",image_close)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





import cv2
import numpy as np 
from Q2_Chapter_1_1 import generate_number


generated_number = generate_number()

def adjust_image_colors_opencv(image_path, generated_number):
    img = cv2.imread(image_path)

    img = cv2.add(img, np.array([generated_number]).astype('uint8'))
    
    return img

image_path = 'Q2_chapter1.jpg'
adjusted_img = adjust_image_colors_opencv(image_path, generated_number)
cv2.imwrite('Q2_chapter1out.jpg', adjusted_img)

red_sum = np.sum(adjusted_img[:, :, 2]) 

print("Sum of red channel pixel values:", red_sum)

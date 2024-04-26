import cv2
import numpy as np 
from Q2_Chapter_1_1 import generate_number


generated_number = generate_number()

def adjust_image_colors_opencv(image_path, generated_number):
    # Load the image
    img = cv2.imread(image_path)
    
    # Ensure that adding the number won't result in values exceeding 255
    img = cv2.add(img, np.array([generated_number]).astype('uint8'))
    
    return img

# Path to your image
image_path = 'Q2_chapter1.jpg'

# Adjust the image colors
adjusted_img = adjust_image_colors_opencv(image_path, generated_number)

# To save the adjusted image to a file
cv2.imwrite('Q2_chapter1out.jpg', adjusted_img)

# Calculate the sum of red channel values
red_sum = np.sum(adjusted_img[:, :, 2])  # Index 2 corresponds to the red channel

print("Sum of red channel pixel values:", red_sum)

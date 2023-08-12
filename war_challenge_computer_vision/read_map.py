import cv2
import pytesseract

from coordinates import coordinates

image = cv2.imread('images/TelaDoJogo.png')

# Convert BGR to RGB (OpenCV loads images in BGR format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

for territory in coordinates.keys():
    top_left = coordinates[territory]["coord1"]
    bottom_right = coordinates[territory]["coord2"]
    c1, c2 = coordinates[territory]["color"]
    print(c1, c2)
    color = list(image[c2, c1].astype('int32'))

    print(color)

    x1, y1 = top_left
    x2, y2 = bottom_right
    
    slice_image = image[y1: y2, x1 : x2]

    troops_in_territory = pytesseract.image_to_string(slice_image)
    print(f'There is {troops_in_territory} in {territory}')
    print(image.shape)
    cv2.rectangle(img=image, pt1=top_left, pt2=bottom_right, color=color, thickness=1)

# Display the image
cv2.imshow('Square', slice_image)
cv2.imshow('Square', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
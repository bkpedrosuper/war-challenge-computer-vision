import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageOps

from war_challenge_computer_vision.coordinates import coordinates

image = Image.open("images/TelaDoJogo.png")


def otsu_threshold(image, threshold):
    # Convert the PIL image to a NumPy array
    image_array = np.array(image)
    # opencv_image = cv2.cvtColor(image_array, cv2.GRAY)
    ret1, thresh = cv2.threshold(
        image_array, threshold, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    return Image.fromarray(cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB))


# Convert BGR to RGB (OpenCV loads images in BGR format)
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

for territory in coordinates.keys():
    top_left = coordinates[territory]["coord1"]
    bottom_right = coordinates[territory]["coord2"]
    c1, c2 = coordinates[territory]["color"]
    color = list(image.getpixel((c1, c2)))

    print(color)

    x1, y1 = top_left
    x2, y2 = bottom_right

    slice_image = image.crop((x1, y1, x2, y2))
    gray_image = slice_image.convert("L")
    threshold = 140
    threshold_image = otsu_threshold(gray_image, threshold)
    image_contrast = ImageOps.autocontrast(
        gray_image.point(lambda gray_pixel: 255 - gray_pixel)
    ).resize((500, 500), resample=Image.BOX)

    high_resolution_threshold_image = threshold_image.resize(
        (500, 500), resample=Image.BOX
    )

    # pil_image = Image.fromarray(cv2.cvtColor(slice_image, cv2.COLOR_BGR2GRAY))
    # pil_image = Image.open("images/definicao-de-texto.png")

    troops_in_territory = pytesseract.image_to_string(
        high_resolution_threshold_image, lang="eng", config="--psm 6 outputbase digits"
    )

    print(f"There is {str(troops_in_territory).strip()} in {territory}")
    # print(image.size)

    # Display the image
    # cv2.imwrite('images/Square_slice.png', slice_image)
    high_resolution_threshold_image.save(f"images/{territory}_slice_threshold.png")
    image_contrast.save(f"images/{territory}_contrast.png")
    slice_image.save(f"images/{territory}_slice.png")
    # cv2.imwrite('images/Square_rect.png', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

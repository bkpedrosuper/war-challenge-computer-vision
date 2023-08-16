import numpy as np
from PIL import Image, ImageOps
from PIL.Image import Image as ImagePIL
from skimage.filters import rank
from skimage.morphology import binary_dilation, binary_erosion, disk


# https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html
class Preprocessor:
    def __init__(self, image: ImagePIL):
        self.image = image
        self.processed_image = self.image

    def invert_image(self):
        self.processed_image = ImageOps.invert(image=self.processed_image)
        return self

    def filter_mean(self, kernel_size=15):
        footprint = disk(kernel_size)
        filtered_image = rank.mean_percentile(
            image=np.array(self.processed_image), footprint=footprint
        )
        self.processed_image = Image.fromarray(filtered_image)
        return self

    def threshold(self, threshold=170):
        self.processed_image = self.processed_image.point(
            lambda gray_point: 255 if gray_point > threshold else 0
        )
        return self

    def erode_image(self, qtd_erosion=14):
        binary_image = self.processed_image.convert("1")
        eroded_image = binary_erosion(np.array(binary_image))
        for _ in range(qtd_erosion - 1):
            eroded_image = binary_erosion(eroded_image)
        self.processed_image = Image.fromarray(eroded_image.astype(np.uint8) * 255)
        return self

    def dilate_image(self, qtd_dilation=5):
        binary_image = self.processed_image.convert("1")
        eroded_image = binary_dilation(np.array(binary_image))
        for _ in range(qtd_dilation - 1):
            eroded_image = binary_dilation(eroded_image)
        self.processed_image = Image.fromarray(eroded_image.astype(np.uint8) * 255)
        return self

    def convert_to_gray(self):
        self.processed_image = self.processed_image.convert("L")
        return self

    def resize(self, size: tuple[int, int] = (500, 500)):
        self.processed_image = self.processed_image.resize(
            size, resample=Image.Resampling.BICUBIC
        )
        return self

    def build(self):
        return self.processed_image

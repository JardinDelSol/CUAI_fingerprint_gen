import cv2
import glob
import numpy as np

# from PIL import Image
import os

base_dir = "./cropped/images"


def main():
    for img in glob.glob(base_dir + "/*.jpg"):
        image = cv2.imread(img)
        name = img.split("\\")[-1]
        print(name)
        for rate in [0, 10, 20, 30, 40]:
            # continue
            bright = np.ones(image.shape, dtype="uint8") * rate
            brighter = cv2.add(image, bright)
            darker = cv2.subtract(image, bright)
            cv2.imwrite("./Dataset/bright_changed/" + str(rate) + "b_" + name, brighter)
            cv2.imwrite("./Dataset/bright_changed/" + str(rate) + "d_" + name, darker)


if __name__ == "__main__":
    main()

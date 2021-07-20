from genericpath import isdir
import re
import cv2
import sys
import os


def main():
    base_dir = sys.argv[1]
    if not os.path.isdir(base_dir):
        print("no such directory: {}".format(base_dir))
        return
    label_dir = base_dir.replace("images", "labels")
    save_dir = sys.argv[2]
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)
    save_img_dir = save_dir + "/images"
    save_label_dir = save_dir + "/labels"
    if not os.path.isdir(save_img_dir):
        os.mkdir(save_img_dir)

    img_list = os.listdir(base_dir)
    count = 0
    for img in img_list:
        img_dir = os.path.join(base_dir, img)
        label = os.path.join(label_dir, img.replace("jpg", "txt"))
        if not os.path.isfile(label):
            continue
        file = open(label)
        lines = file.readlines()
        image = cv2.imread(img_dir)
        sp = image.shape
        width = sp[1]
        height = sp[0]
        print(img_dir)
        print(lines)
        for line in lines:
            cls, x, y, w, h = line.split()
            print(x, y, w, h)
            x, y, w, h = [float(i) for i in [x, y, w, h]]
            x = int(width * x)
            y = int(height * y)
            w = int(width * w)
            h = int(height * h)
            print(x, y, w, h)
            croped = image[
                y - int(h / 2) : y + int(h / 2), x - int(w / 2) : x + int(w / 2)
            ]
            new_dir = os.path.join(save_img_dir, str(count) + ".jpg")
            print(new_dir)
            croped = cv2.resize(croped, (526, 526), cv2.INTER_NEAREST)
            try:
                cv2.imwrite(new_dir, croped)
            except:
                print(image.shape)
                print(image)
            count += 1


if __name__ == "__main__":
    main()

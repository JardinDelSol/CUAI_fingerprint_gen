import albumentations as AL
from albumentations.augmentations import transforms
import cv2
import glob
import tensorflow as tf

HF = AL.Compose([AL.HorizontalFlip(p=1)])
VF = AL.Compose([AL.VerticalFlip(p=1)])
ColorJitter = AL.Compose(
    [AL.augmentations.transforms.ColorJitter(always_apply=True, p=1)]
)

base_dir = "./bright_changed"


def main():
    for img in glob.glob(base_dir + "/*.jpg"):
        image = cv2.imread(img)
        name = img.split("/")[-1]
        print(name)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        H_TF = HF(image=image)
        V_TF = VF(image=image)
        H_img = H_TF["image"]
        V_img = V_TF["image"]

        H_name = "H_" + name
        V_name = "V_" + name
        for i in range(5):
            H_temp = cv2.cvtColor(ColorJitter(image=H_img)["image"], cv2.COLOR_RGB2BGR)
            V_temp = cv2.cvtColor(ColorJitter(image=V_img)["image"], cv2.COLOR_RGB2BGR)
            # V_temp = ColorJitter(image=V_img)["image"]

            cv2.imwrite("./dataset/" + str(i) + H_name, H_temp)
            cv2.imwrite("./dataset/" + str(i) + V_name, V_temp)

        H_img = cv2.cvtColor(H_TF["image"], cv2.COLOR_RGB2BGR)
        V_img = cv2.cvtColor(V_TF["image"], cv2.COLOR_RGB2BGR)
        cv2.imwrite("./dataset/" + H_name, H_img)
        cv2.imwrite("./dataset/" + V_name, V_img)


if __name__ == "__main__":
    main()

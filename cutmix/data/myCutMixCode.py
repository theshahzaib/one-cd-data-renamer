import cv2
import numpy as np
import torch
from torch.utils.data import Dataset
import os

class TrainData(Dataset):
    def __init__(self, train_idxs, low, high):
        super().__init__()
        self.train_idxs = train_idxs
        self.low = low
        self.high = high

    def __len__(self):
        return len(self.train_idxs)

    def __getitem__(self, idx):
        _idx = self.train_idxs[idx]

        fn = all_files[_idx]

        img = cv2.imread(fn, cv2.IMREAD_COLOR)
        img2 = cv2.imread(fn.replace('_pre_disaster', '_post_disaster'), cv2.IMREAD_COLOR)
        msk0 = cv2.imread(fn.replace('/images/', '/masks/'), cv2.IMREAD_UNCHANGED)
        lbl_msk1 = cv2.imread(fn.replace('/images/', '/masks/').replace('_pre_disaster', '_post_disaster'), cv2.IMREAD_UNCHANGED)

        # Randomly select another image from the dataset
        rand_idx = np.random.randint(self.low, self.high)
        rand_fn = all_files[rand_idx]
        rand_img = cv2.imread(rand_fn, cv2.IMREAD_COLOR)
        rand_img2 = cv2.imread(rand_fn.replace('_pre_disaster', '_post_disaster'), cv2.IMREAD_COLOR)
        rand_msk0 = cv2.imread(rand_fn.replace('/images/', '/masks/'), cv2.IMREAD_UNCHANGED)
        rand_lbl_msk1 = cv2.imread(rand_fn.replace('/images/', '/masks/').replace('_pre_disaster', '_post_disaster'), cv2.IMREAD_UNCHANGED)

        # Randomly select a patch from the second image
        lam = np.random.beta(1, 1)
        bbx1, bby1, bbx2, bby2 = rand_bbox((rand_img.shape[1], rand_img.shape[0]), lam)
        # Paste the selected patch onto the first image
        img[bbx1:bbx2, bby1:bby2, :] = rand_img[bbx1:bbx2, bby1:bby2, :]
        img2[bbx1:bbx2, bby1:bby2, :] = rand_img2[bbx1:bbx2, bby1:bby2, :]
        msk0[bbx1:bbx2, bby1:bby2] = rand_msk0[bbx1:bbx2, bby1:bby2]
        lbl_msk1[bbx1:bbx2, bby1:bby2] = rand_lbl_msk1[bbx1:bbx2, bby1:bby2]

        # Your remaining augmentation steps...

        # Convert to PyTorch tensors and return the sample
        img = preprocess_inputs(np.concatenate([img, img2], axis=2))
        img = torch.from_numpy(img.transpose((2, 0, 1))).float()
        msk = torch.from_numpy(msk.transpose((2, 0, 1))).long()

        sample = {'img': img, 'msk': msk, 'lbl_msk': lbl_msk, 'fn': fn}
        return sample

def rand_bbox(size, lam):
    W, H = size
    cut_rat = np.sqrt(1. - lam)
    cut_w = np.int64(W * cut_rat)
    cut_h = np.int64(H * cut_rat)

    # uniform
    cx = np.random.randint(W)
    cy = np.random.randint(H)

    bbx1 = np.clip(cx - cut_w // 2, 0, W)
    bby1 = np.clip(cy - cut_h // 2, 0, H)
    bbx2 = np.clip(cx + cut_w // 2, 0, W)
    bby2 = np.clip(cy + cut_h // 2, 0, H)

    return bbx1, bby1, bbx2, bby2

def preprocess_inputs(inputs):
    # Your preprocessing steps...
    return inputs

# def main(image1, image2):
#     # Load images
#     img = cv2.imread(image1, cv2.IMREAD_COLOR)
#     img2 = cv2.imread(image2, cv2.IMREAD_COLOR)

#     # Randomly select a patch from the second image
#     lam = np.random.beta(1, 1)
#     bbx1, bby1, bbx2, bby2 = rand_bbox((img2.shape[1], img2.shape[0]), lam)
#     # Paste the selected patch onto the first image
#     img[bbx1:bbx2, bby1:bby2, :] = img2[bbx1:bbx2, bby1:bby2, :]

#     # Perform any remaining augmentation steps or processing here...

#     # Return the modified image
#     return img

# # Example usage
# image1_path = "img1.jpg"
# image2_path = "img2.jpg"
# cutmix_image = main(image1_path, image2_path)
# cv2.imwrite("cutmix_image.jpg", cutmix_image)




def main(pre_image_path, post_image_path, pre_label_path, post_label_path):
    # Load pre-images and labels
    pre_img = cv2.imread(pre_image_path, cv2.IMREAD_COLOR)
    pre_label = cv2.imread(pre_label_path, cv2.IMREAD_UNCHANGED)
    
    # Load post-images and labels
    post_img = cv2.imread(post_image_path, cv2.IMREAD_COLOR)
    post_label = cv2.imread(post_label_path, cv2.IMREAD_UNCHANGED)

    # Randomly select a patch from the post-image
    lam = np.random.beta(1, 1)
    bbx1, bby1, bbx2, bby2 = rand_bbox((post_img.shape[1], post_img.shape[0]), lam)

    # Paste the selected patch onto the pre-image and update the pre-label
    pre_img[bbx1:bbx2, bby1:bby2, :] = post_img[bbx1:bbx2, bby1:bby2, :]
    pre_label[bbx1:bbx2, bby1:bby2] = post_label[bbx1:bbx2, bby1:bby2]

    # Randomly select a patch from the pre-image
    lam = np.random.beta(1, 1)
    bbx1, bby1, bbx2, bby2 = rand_bbox((pre_img.shape[1], pre_img.shape[0]), lam)

    # Paste the selected patch onto the post-image and update the post-label
    post_img[bbx1:bbx2, bby1:bby2, :] = pre_img[bbx1:bbx2, bby1:bby2, :]
    post_label[bbx1:bbx2, bby1:bby2] = pre_label[bbx1:bbx2, bby1:bby2]

    # Return the modified pre-image, post-image, pre-label, and post-label
    return pre_img, post_img, pre_label, post_label

# Example usage
pre_image_path = "sample/image/bolari_1802_patch_1_1_png_rf_81647124bd8c565e704f14428d42e0fc_pre.png"
post_image_path = "train/images/bolari_1606_patch_1_1_png_rf_323fda8b57ee23fa5746397e601de276_post.png"
pre_label_path = "train/images/bolari_1606_patch_1_1_png_rf_323fda8b57ee23fa5746397e601de276_pre.png"
post_label_path = "train/images/bolari_1606_patch_1_1_png_rf_323fda8b57ee23fa5746397e601de276_post.png"
cutmix_pre_img, cutmix_post_img, cutmix_pre_label, cutmix_post_label = main(pre_image_path, post_image_path, pre_label_path, post_label_path)

# Save or use the cutmix_pre_img, cutmix_post_img, cutmix_pre_label, and cutmix_post_label as needed
def save_cutmix_images_and_labels(cutmix_pre_img, cutmix_post_img, cutmix_pre_label, cutmix_post_label, save_dir):
    # Save cutmix pre-image
    cutmix_pre_image_path = os.path.join(save_dir, "cutmix_pre_image.jpg")
    cv2.imwrite(cutmix_pre_image_path, cutmix_pre_img)

    # Save cutmix post-image
    cutmix_post_image_path = os.path.join(save_dir, "cutmix_post_image.jpg")
    cv2.imwrite(cutmix_post_image_path, cutmix_post_img)

    # Save cutmix pre-label
    cutmix_pre_label_path = os.path.join(save_dir, "cutmix_pre_label.png")
    cv2.imwrite(cutmix_pre_label_path, cutmix_pre_label)

    # Save cutmix post-label
    cutmix_post_label_path = os.path.join(save_dir, "cutmix_post_label.png")
    cv2.imwrite(cutmix_post_label_path, cutmix_post_label)

    print("Cutmix images and labels saved successfully.")

# Example usage
save_dir = "cutmix_output"
os.makedirs(save_dir, exist_ok=True)
save_cutmix_images_and_labels(cutmix_pre_img, cutmix_post_img, cutmix_pre_label, cutmix_post_label, save_dir)

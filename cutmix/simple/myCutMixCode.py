import cv2
import numpy as np
import torch
from torch.utils.data import Dataset

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

def main(image1, image2):
    # Load images
    img = cv2.imread(image1, cv2.IMREAD_COLOR)
    img2 = cv2.imread(image2, cv2.IMREAD_COLOR)

    # Randomly select a patch from the second image
    lam = np.random.beta(1, 1)
    bbx1, bby1, bbx2, bby2 = rand_bbox((img2.shape[1], img2.shape[0]), lam)
    # Paste the selected patch onto the first image
    img[bbx1:bbx2, bby1:bby2, :] = img2[bbx1:bbx2, bby1:bby2, :]

    # Perform any remaining augmentation steps or processing here...

    # Return the modified image
    return img

# Example usage
image1_path = "img1.jpg"
image2_path = "img2.jpg"
cutmix_image = main(image1_path, image2_path)
cv2.imwrite("cutmix_image.jpg", cutmix_image)

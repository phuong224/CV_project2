import cv2
from src.code.Mask import get_mask



src_path = 'src/image/'
dst_path = 'src/dest/'
res_path = 'result/'


def edit(src, dst, mask, center):
    return cv2.seamlessClone(src, dst, mask, center, cv2.NORMAL_CLONE)


def main():
    for i in range(1, 4):
        

        src = cv2.imread(src_path + f"img{i}.jpg")
        dst = cv2.imread(dst_path + f"bg{i}.jpg")

        mask = get_mask(src_path + f"img{i}.jpg")

        center_x = dst.shape[1] // 2 
        center_y = dst.shape[0] // 2 
        center = (center_x, center_y)

        editted_img = edit(src , dst, mask, center)

        cv2.imwrite(res_path + f"img{i}.jpg", editted_img)

   

main()
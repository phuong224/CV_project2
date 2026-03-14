import cv2

src = cv2.imread("Image/black-house-spider_src-1.jpg")

h, w = src.shape[:2]

target_size = 612

scale = min(target_size / w, target_size / h)

new_w = int(w * scale)
new_h = int(h * scale)

resized = cv2.resize(src, (new_w, new_h), interpolation=cv2.INTER_AREA)

cv2.imwrite("resized_source_black-house-spider_src-1.jpg", resized)
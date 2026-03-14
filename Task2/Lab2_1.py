import cv2
import numpy as np

# Đọc ảnh
src = cv2.imread("Image/resized_source.jpg")
dst = cv2.imread("Image/bg_sky.jpg")

# Đọc mask dưới dạng grayscale
mask = cv2.imread("Image/mask.png", cv2.IMREAD_GRAYSCALE)

# Kiểm tra nếu kích thước mask khác source → resize
if mask.shape[:2] != src.shape[:2]:
    mask = cv2.resize(mask, (src.shape[1], src.shape[0]))

# Đảm bảo mask là nhị phân (0 hoặc 255)
_, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

# Vị trí đặt object trên background
center_dst = (306, 306)

# Poisson blending
output = cv2.seamlessClone(src, dst, mask, center_dst, cv2.NORMAL_CLONE)

# Hiển thị
cv2.imshow("Source", src)
cv2.imshow("Mask", mask)
cv2.imshow("Result", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu ảnh
cv2.imwrite("Result/Task1.jpg", output)
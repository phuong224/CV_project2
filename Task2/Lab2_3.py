import cv2
import numpy as np

# Đọc ảnh
poster = cv2.imread("Image/faker.jpg")
background = cv2.imread("Image/bg1.jpg")

h_bg, w_bg = background.shape[:2]
h_p, w_p = poster.shape[:2]

# 4 điểm ảnh nguồn
pts_src = np.float32([
    [0, 0],
    [w_p, 0],
    [w_p, h_p],
    [0, h_p]
])

# 4 điểm mặt phẳng đích (chỉnh theo ảnh của bạn)
pts_dst = np.float32([
    [1213, 830],
    [1941, 1092],
    [1885, 2538],
    [1068, 2445]
])

# Tính homography
H = cv2.getPerspectiveTransform(pts_src, pts_dst)

# Warp poster
warped = cv2.warpPerspective(poster, H, (w_bg, h_bg))

# Tạo mask
mask = np.zeros((h_bg, w_bg), dtype=np.uint8)
cv2.fillPoly(mask, [pts_dst.astype(int)], 255)

mask_inv = cv2.bitwise_not(mask)

# Xóa vùng dán trên background
bg_cut = cv2.bitwise_and(background, background, mask=mask_inv)

# Lấy phần poster đã warp
poster_cut = cv2.bitwise_and(warped, warped, mask=mask)

# Ghép lại
result = cv2.add(bg_cut, poster_cut)

#Scale để hiển thị full trên màn hình 1920x1080
screen_w = 1920
screen_h = 1080

h_res, w_res = result.shape[:2]

scale = min(screen_w / w_res, screen_h / h_res)

if scale < 1:
    new_w = int(w_res * scale)
    new_h = int(h_res * scale)
    result_display = cv2.resize(result, (new_w, new_h), interpolation=cv2.INTER_AREA)
else:
    result_display = result.copy()

cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.imshow("Result", result_display)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Result/Task3.jpg", result)
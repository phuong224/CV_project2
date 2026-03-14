import cv2
import numpy as np
import tkinter as tk

# ===== Lấy kích thước màn hình =====
root = tk.Tk()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.destroy()

# ===== Đọc ảnh gốc =====
img_original = cv2.imread("Image/faker.jpg")

# ===== Resize để fit màn hình =====
def resize_to_fit_screen(img, max_w, max_h):
    h, w = img.shape[:2]
    scale = min(max_w / w, max_h / h)

    if scale >= 1:
        return img.copy(), 1.0

    new_w = int(w * scale)
    new_h = int(h * scale)

    resized = cv2.resize(img, (new_w, new_h))
    return resized, scale

img_display, scale = resize_to_fit_screen(img_original, screen_w, screen_h)
clone = img_display.copy()

points = []

# ===== Mouse callback =====
def get_coordinates(event, x, y, flags, param):
    global clone, points

    if event == cv2.EVENT_LBUTTONDOWN:

        # Convert tọa độ hiển thị → tọa độ ảnh gốc
        orig_x = int(x / scale)
        orig_y = int(y / scale)

        print(f"Display: ({x},{y})  --> Original: ({orig_x},{orig_y})")

        points.append([orig_x, orig_y])

        # Vẽ trên ảnh hiển thị
        cv2.circle(clone, (x, y), 5, (0,0,255), -1)
        text = f"{orig_x},{orig_y}"
        cv2.putText(clone, text, (x+10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0,255,0), 1)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", clone)
cv2.setMouseCallback("Image", get_coordinates)

while True:
    cv2.imshow("Image", clone)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

print("4 điểm gốc:", points)
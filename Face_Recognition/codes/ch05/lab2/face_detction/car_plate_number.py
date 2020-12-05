import cv2
import time

# 1、讀取影象，並把影象轉換為灰度影象並顯示 
img = cv2.imread("tesla_car.jpg") # 讀取圖片 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉換了灰度化 
cv2.imshow('gray', img_gray) # 顯示圖片 
cv2.waitKey(0) 
# 2、將灰度影象二值化，設定閾值是100 
img_thre = img_gray 
cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV, img_thre) 
cv2.imshow('threshold', img_thre) 
cv2.waitKey(0) 
# 3、儲存黑白圖片 
cv2.imwrite('thre_res.png', img_thre) 
# 4、分割字元 
white = [] # 記錄每一列的白色畫素總和 
black = [] # ..........黑色....... 
height = img_thre.shape[0] 
width = img_thre.shape[1] 
white_max = 0 
black_max = 0 
# 計算每一列的黑白色畫素總和 
for i in range(width): 
    s = 0 # 這一列白色總數 
    t = 0 # 這一列黑色總數 
for j in range(height): 
    if img_thre[j][i] == 255: 
        s  = 1 
    if img_thre[j][i] == 0: 
        t  = 1 
    white_max = max(white_max, s) 
    black_max = max(black_max, t) 
    white.append(s) 
    black.append(t) 
    print(s) 
    print(t) 
    arg = False # False表示白底黑字；True表示黑底白字 
    if black_max > white_max: 
        arg = True 
# 分割影象 
def find_end(start_): 
    end_ = start_1 
    for m in range(start_1, width-1): 
        if (black[m] if arg else white[m]) > (0.95 * black_max if arg else 0.95 * white_max): # 0.95這個引數請多調整，對應下面的0.05 
            end_ = m 
            break 
        return end_ 
        n = 1 
        start = 1 
        end = 2 
        while n < width-2: 
            n  = 1 
        if (white[n] if arg else black[n]) > (0.05 * white_max if arg else 0.05 * black_max): 
# 上面這些判斷用來辨別是白底黑字還是黑底白字 
# 0.05這個引數請多調整，對應上面的0.95 
            start = n 
            end = find_end(start) 
            n = end 
        if end-start > 5: 
            cj = img_thre[1:height, start:end]

cv2.imshow('caijian', cj) 
cv2.waitKey(0) 




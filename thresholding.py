from numba import njit
import numpy as np

@njit
def integral_im(img):
    # Calculates the integral image, so that smaller parts of the image can be added up in linear time.
    int_img = np.zeros_like(img)
    for i in range(np.shape(img)[0]):
        isum = 0
        for j in range(np.shape(img)[1]):
            isum += img[i,j]
            if i==0:
                int_img[i,j] = isum
            else:
                int_img[i,j] = isum + int_img[i-1,j]

    return int_img

@njit
def bradleyroth(img, int_img, s, t):
    # Uses a moving sxs window of pixels and calculates the total sum in each window. Then the pixel is assigned a value based on the threshold t and the average value of the pixels around it.
    thresh_img = np.zeros_like(img)
    l = np.shape(img)[0]
    w = np.shape(img)[1]
    for i in range(l):
        for j in range(w):
            x1 = i - s//2
            x2 = i + s//2
            y1 = j - s//2
            y2 = j + s//2
            area = (x2 - x1)*(y2 - y1)
            psum = int_img[x2%l, y2%w] - int_img[x2%l, (y1-1)%w] - int_img[(x1-1)%l, y2%w] + int_img[(x1-1)%l, (y1-1)%w]
            threshold = psum/area * (100-t)/100
            if img[i,j] <= threshold:
                thresh_img[i,j] = 0
            else:
                thresh_img[i,j] = img[i,j]
    return thresh_img


#Functions to help in cropping the image after thresholding
#Calculates horizontal and vertical averages

@njit
def avg_horizontal(image_dat):
    havg = np.zeros(0)
    for i in range(np.shape(image_dat)[1]):
        temp = np.zeros(0)
        for j in range(np.shape(image_dat)[0]):
            temp = np.append(temp,image_dat[j][i])
        havg = np.append(havg,np.mean(temp))
    return havg
@njit
def avg_vertical(image_dat):
    vavg = np.zeros(0)
    for i in range(np.shape(image_dat)[0]):
        temp = np.zeros(0)
        for j in range(np.shape(image_dat)[1]):
            temp = np.append(temp,image_dat[i][j])
        vavg = np.append(vavg,np.mean(temp))
    return vavg

#Function to calculate center of an arc/circle given 3 points on the arc

@njit
def arc_centr(p1,p2,p3):
    #unpack points into x and y
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    #Find slopes and intercepts of two lines passing through the input points
    m1 = (y2-y1)/(x2-x1)
    m2 = (y3-y1)/(x3-x1)
    c1 = (-m1*x1) + y1
    c2 = (-m2*x1) + y1

    #Find mid-point
    xmid1 = (x2+x1)//2
    ymid1 = (y2+y1)//2
    xmid2 = (x3+x1)//2
    ymid2 = (y3+y1)//2

    #Find slopes and intercepts of perpendicular bisectors to above lines
    perp_m1 = -1/m1
    perp_m2 = -1/m2
    perp_c1 = (-perp_m1*xmid1) + ymid1
    perp_c2 = (-perp_m2*xmid2) + ymid2

    #Find intersection x and y
    xcent = (perp_c2-perp_c1)/(perp_m1-perp_m2)
    ycent = (perp_m1*xcent) + perp_c1
    centr = [np.floor(xcent),np.floor(ycent)]
    return centr



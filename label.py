import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
data_path = '/home/lijun/Research/Code/depth_pretrain/res/'
img_names = os.listdir('../res/')
img_names = [i[:-4] for i in img_names if i.endswith('npy')]
for im_name in img_names:

    points = np.load('../res/'+im_name + '.npy')
    num = points.shape[0]
    im = cv2.imread(data_path + im_name + '_img.png')

    for id in range(num):
        im_cur = im.copy()
        cv2.circle(im_cur, center=(points[id, 0], points[id, 1]), radius=8, color=(0, 0, 255), thickness=-1)
        cv2.imwrite('focal_point/'+im_name + '_img_%d.png'%id, im_cur)

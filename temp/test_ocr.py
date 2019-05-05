# -*- coding: utf-8 -*
# 通过猫的位置确定屏幕，进行透视变换，然后截取物量和FC/AC标志
# 训练kNN进行OCR，得出谱面难度等级及是否FC/AC

import numpy as np
import cv2 as cv

def ocr_test():
    #**************** 特征匹配，确定该图是魔剂猫的结算图 ****************#

    MIN_MATCH_COUNT = 150
    img1 = cv.imread('_image\\catSE2.jpg',0)                # queryImage
    img2c = cv.imread('_test\\catMN1.jpg',1)                  # trainImage
    # img2c = cv.imread('_image\\catF1.jpg')

    height,width = img2c.shape[:2]
    # print(height, width)
    if max(height, width) > 1000:
        f = min(1000/height, 1000/width)
        img2c = cv.resize(img2c,None,fx=f, fy=f, interpolation = cv.INTER_CUBIC)
    img2 = cv.cvtColor(img2c, cv.COLOR_BGR2GRAY)

    # Initiate SIFT detector
    sift = cv.xfeatures2d.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1,des2,k=2)
    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)

    #**************** 透视变换，截取屏幕 ****************#

    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
        M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        h, w = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv.perspectiveTransform(pts,M)
        M1 = cv.getPerspectiveTransform(dst, pts)

    #**************** 对物量进行OCR ****************#

        img10 = cv.warpPerspective(img2, M1, (pts[2][0][0], pts[2][0][1]))
        # img10c = cv.warpPerspective(img2c, M1, (pts[2][0][0], pts[2][0][1]))

        imgAmount = img10[195:215, 255:295]
        imgAmount = cv.adaptiveThreshold(imgAmount, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 55, 12)

        imgFCAC = img10[336:356, 78:258]
        imgFCAC = cv.adaptiveThreshold(imgFCAC, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 55, 12)

        # cv.imshow('Amount', imgAmount)
        # cv.imshow('FCAC', imgFCAC)

        # print(i)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

        cv.imwrite('imgAmount.jpg', imgAmount)
        cv.imwrite('imgFCAC.jpg', imgFCAC)

        x = np.array(imgAmount)
        test = x[:, :].reshape(-1, 800).astype(np.float32)

        with np.load('amount_data.npz') as data:
            train = data['train']
            train_labels = data['train_labels']

        knn = cv.ml.KNearest_create()
        knn.train(train, cv.ml.ROW_SAMPLE, train_labels)
        amount_ret,amount_result,amount_neighbours,amount_dist = knn.findNearest(test,k=5)

        print("Amount_result:  {}".format(amount_result))
        print("Amount_neighbours:  {}".format(amount_neighbours))
        print("Amount_distance:  {}".format(amount_dist))

    #**************** 对FC/AC标志进行OCR ****************#

        x = np.array(imgFCAC)
        test = x[:, :].reshape(-1, 3600).astype(np.float32)

        with np.load('FCAC_data.npz') as data:
            train = data['train']
            train_labels = data['train_labels']

        knn = cv.ml.KNearest_create()
        knn.train(train, cv.ml.ROW_SAMPLE, train_labels)
        FCAC_ret,FCAC_result,FCAC_neighbours,FCAC_dist = knn.findNearest(test,k=5)

        print("FCAC_result:  {}".format(FCAC_result))
        print("FCAC_neighbours:  {}".format(FCAC_neighbours))
        print("FCAC_distance:  {}".format(FCAC_dist))

    #**************** OCR结果输出到文件 ****************#

        amount_Out = int(amount_result[0][0])
        FCAC_Out = int(FCAC_result[0][0])

        if amount_dist[0][0] >= 7000000:
            amount_Out = 0
        if FCAC_dist[0][0] >= 70000000:
            FCAC_Out = 0

        return amount_Out, FCAC_Out

        # print(amount_Out, FCAC_Out)
        # print(amount_dist[0][0], FCAC_dist[0][0])

a, b = ocr_test()
print(a, b)

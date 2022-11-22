##################################################################################################

본 과제물은 20173709 소프트웨어학부 나원후가 작성하였음을 밝힙니다.

프로그램 실행은 main.ipynb에서 수행합니다.

프로그램의 시퀀스는 다음과 같습니다.


##################################################################################################


1. import

import cv2
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np
from src import correlation, normalize_subtraction, three_channel_correlation, show_output, normalize_pixel, normalize_reverse, normalize_0to1, convolution_patch, no_normalization

2. 사용할 이미지 정의
image_original1 = cv2.imread('data/image01.jpg')
image1 = image_original1[:,:,::-1] # BGR -> RGB
patch1_1 = cv2.imread('data/patch1.jpg')
patch1_1 = patch1_1[:,:,::-1] # BGR -> RGB

3. 이미지 전처리 연산
normalized_image1_s = normalize_subtraction(image1)
normalized_patch1_1_s = normalize_subtraction(patch1_1)
conv_normalized_patch1_1_s = convolution_patch(normalized_patch1_1_s)
conv_output1_1_s = three_channel_correlation(normalized_image1_s, conv_normalized_patch1_1_s)
conv_output1_1_s = normalize_0to1(conv_output1_1_s)

4. 결과 출력
show_output(patch1_1, image_original1, conv_output1_1_s, 0.99)

이후 수행되는 모든 코드는 앞선 코드의 반복이며,
각각은 이미지에 수행하는 전처리가 다릅니다.


##################################################################################################


main.ipynb에서 참조하는 외부 모듈은 src 디렉토리 내부에 있는
correlation.py, normalize.py, show_output.py입니다.

correlation을 구하는 평균 시간은 m1 mac pro 10 core cpu 10 core gpu 기준 35초 입니다.

디바이스 환경에 따라 실행 시간이 상이할 수 있습니다.

tests 디렉토리에서는 구현한 함수의 기능을 테스트하는 모듈들이 있습니다.


##################################################################################################


본 과제물에서 활용한 이미지는 data 디렉토리에 있습니다.

모든 이미지 결과는 result 디렉토리에 있습니다.

각 이미지 결과들의 이름은 f"{정규화함수이름}_{패치숫자}"로 구성되었습니다.

Convolution을 적용한 결과의 경우의 이름은 f"convolution_{정규화함수이름}_{패치숫자}"로 구성되었습니다.

##################################################################################################

모든 코드는 비공개 git으로 로그가 남겨져 있습니다.

##################################################################################################
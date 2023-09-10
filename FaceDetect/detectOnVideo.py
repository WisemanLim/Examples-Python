# -*- coding:utf-8 -*-
# !/usr/bin/python
import cv2
import numpy as np

# 사용할 동영상 파일 경로
video_path = './청년의날 스케치 영상.mp4'

# 동영상에서 얼굴을 감지하기 위한 딥러닝 모델 목록
model_paths = [
    'deploy.prototxt.txt',  # 프로토타입 정의 파일
    'res10_300x300_ssd_iter_140000.caffemodel'  # 사전 학습된 가중치 파일
]

# 모델을 로드합니다.
net = cv2.dnn.readNetFromCaffe(model_paths[0], model_paths[1])

# 동영상 캡처 객체 생성
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 동영상 프레임 크기 변경 (선택사항)
    frame = cv2.resize(frame, (640, 480))

    # 프레임 전처리
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104, 177, 123))

    # 전처리된 프레임을 모델에 입력
    net.setInput(blob)
    detections = net.forward()

    # 감지된 얼굴 주위에 경계 상자 그리기
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # 신뢰도 임계값
            box = detections[0, 0, i, 3:7] * np.array([640, 480, 640, 480])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # 화면에 프레임 표시
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 해제 및 OpenCV 윈도우 닫기
cap.release()
cv2.destroyAllWindows()
# -*- coding:utf-8 -*-
# !/usr/bin/python
import os
import time
import numpy as np
import cv2

# OpenCV에서 얼굴 감지기를 초기화합니다.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 웹캠을 엽니다. 웹캠 인덱스는 보통 0 또는 1입니다.
cap = cv2.VideoCapture(0)

# 이미지 저장 경로
output_dir = './detected_faces'
os.makedirs(output_dir, exist_ok=True)

# 이미지 저장 후 경과한 시간 초기화
last_save_time = 0

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 프레임이 제대로 읽어졌는지 확인
    if not ret:
        break

    # 그레이스케일로 변환 (얼굴 감지기는 그레이스케일 이미지를 사용합니다)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 감지
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # 감지된 얼굴 주위에 경계 상자 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 이미지 저장 조건 설정 (3초마다 한 번씩 저장)
        current_time = time.time()
        if ((current_time - last_save_time) >= 3):
            # 감지된 얼굴 이미지 저장
            face_image = frame[y:y + h, x:x + w]
            face_filename = os.path.join(output_dir, f'face_{len(os.listdir(output_dir))}.jpg')
            cv2.imwrite(face_filename, face_image)
            last_save_time = current_time

    # 화면에 프레임 표시
    cv2.imshow('Face Detection', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 해제 및 OpenCV 윈도우 닫기
cap.release()
cv2.destroyAllWindows()
import cv2
import face_recognition
import os
from moviepy.editor import VideoFileClip
import numpy as np

def extract_frames(video_path, interval=600):
    frames = []
    clip = VideoFileClip(video_path)
    duration = clip.duration
    
    for t in np.arange(0, duration, interval):
        frame = clip.get_frame(t)
        frames.append(frame)
    
    clip.close()
    return frames

def detect_person(frames, target_image_path, tolerance=0.6):
    target_image = face_recognition.load_image_file(target_image_path)
    target_encoding = face_recognition.face_encodings(target_image)
    
    if not target_encoding:
        raise ValueError("ターゲット画像から顔を検出できませんでした。")
    
    target_encoding = target_encoding[0]
    appearances = []

    for i, frame in enumerate(frames):
        rgb_frame = frame[:, :, ::-1]  # BGR to RGB
        small_frame = cv2.resize(rgb_frame, (0, 0), fx=0.25, fy=0.25)
        try:
            face_locations = face_recognition.face_locations(small_frame)
            # small_frameを使用して顔エンコーディングを行う
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            continue

        for face_encoding in face_encodings:
            match = face_recognition.compare_faces([target_encoding], face_encoding, tolerance=tolerance)[0]
            if match:
                appearances.append(i * 10)  # フレーム番号を秒数に変換
                break

    return appearances

def main():
    video_path = r"C:\hoge.mp4"
    target_image_path = r"C:\fuga.jpg"
    
    print("フレームを抽出中...")
    frames = extract_frames(video_path, interval=10)  # 間隔を10秒に設定
    
    print("顔認識を実行中...")
    appearances = detect_person(frames, target_image_path, tolerance=0.5)
    
    if appearances:
        print(f"対象の人物が以下の時間に出演しています（秒）: {appearances}")
    else:
        print("対象の人物は動画内で検出されませんでした。")

if __name__ == "__main__":
    main()
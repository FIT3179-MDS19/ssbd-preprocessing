"""
The purpose of this program is to extract key-frames from a video by utilising low-motion technique.
The input of this program is the videos directory.
The output of this program is the extracted frame videos under videos_extracted folder.
"""

import cv2
import numpy as np

def extract_frame(video):
    cap = cv2.VideoCapture(rf'videos\{video}')
    ori_fps = int(cap.get(cv2.CAP_PROP_FPS))

    keyframes = []

    prev_frame = None


    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_frame is not None:
            # Calculate optical flow using Farneback method
            flow = cv2.calcOpticalFlowFarneback(prev_frame, frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

            # Calculate motion magnitude
            motion_magnitude = np.sqrt(flow[..., 0] ** 2 + flow[..., 1] ** 2)

            # Check if the mean motion magnitude is below the threshold
            if np.mean(motion_magnitude) < 1.4296789216364987:
                keyframes.append(frame)

        prev_frame = frame_gray.copy()

    print("BEFORE:", cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()

    # Get the width and height of the keyframes
    height, width, _ = keyframes[0].shape

    # Define the output video writer
    output_video_path = f'videos_extracted/{video}_extracted.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use other codecs as well
    out = cv2.VideoWriter(output_video_path, fourcc, ori_fps, (width, height))

    # Write keyframes to the output video
    for keyframe in keyframes:
        out.write(keyframe)

    print("AFTER:", len(keyframes))
    out.release()

    return len(keyframes) / ori_fps

import os

dir_path = './videos'

videos = os.listdir(dir_path)

durations = []
for video in videos:
    print(video)
    d = extract_frame(video)
    durations.append(d)
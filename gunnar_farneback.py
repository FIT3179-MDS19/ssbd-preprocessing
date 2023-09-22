"""
The purpose of this program is to calculate the mean and standard deviation of each Gunnar Farneback optical flow.
The input of this program is the videos directory generated from `extract_va.py'
The output of this program is a txt file `magnitude_videos.txt`
"""

import cv2
import numpy as np
import os

def calculate_magnitude(video):
    # Initialize video capture
    cap = cv2.VideoCapture(rf'videos\{video}')

    # Create a list to store optical flow magnitudes
    magnitudes = []

    # Read the first frame
    ret, frame = cap.read()

    # Convert the first frame to grayscale
    prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the current frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Calculate optical flow
        flow = cv2.calcOpticalFlowFarneback(prev_frame, gray_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        
        # Calculate the magnitude of optical flow vectors
        magnitude = np.sqrt(flow[..., 0] ** 2 + flow[..., 1] ** 2)
        
        # Calculate the average magnitude for this frame
        avg_magnitude = np.mean(magnitude)
        
        # Store the average magnitude in the list
        magnitudes.append(avg_magnitude)
        
        # Draw optical flow vectors on the frame
        step = 20  # Controls the spacing between arrows
        for y in range(0, frame.shape[0], step):
            for x in range(0, frame.shape[1], step):
                dx, dy = flow[y, x]
                cv2.arrowedLine(frame, (x, y), (int(x + dx), int(y + dy)), (0, 255, 0), 2)
        
        # Update the previous frame
        prev_frame = gray_frame.copy()
        
        # Display the magnitude on the frame
        # cv2.putText(frame, f'Avg Magnitude: {avg_magnitude:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # cv2.imshow('Optical Flow', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Analyze the distribution of magnitudes (you can use any metric here)
    mean_magnitude = np.mean(magnitudes)
    stddev_magnitude = np.std(magnitudes)

    print(f"Mean Magnitude: {mean_magnitude:.2f}")
    print(f"Standard Deviation of Magnitude: {stddev_magnitude:.2f}")

    return mean_magnitude, stddev_magnitude


dir_path = './videos'

videos = os.listdir(dir_path)

with open('magnitude_videos.txt', 'a') as file:
    for video in videos:
        print(video)
        mean, std = calculate_magnitude(video)
        # Append the data to the file
        file.write(f'{video}, {mean}, {std}\n')
# SSBD dataset Preprocessing

Please pre-installed these libraries before proceeding to the next step; cv2, pytube, numpy, scipy, xml, os, json, 

In this module, you will be parsing XML dataset to a pre-formatted JSON files, extract videos and audios, then using Gunnar Farnback optical flow to extract key-frames.

Due to large size of videos and audios data, please download all the videos and audios by performing the steps below.

1. Parse SSBD dataset into JSON format `python XML_JSON.py`.
2. Extract and download videos and audios from parsed JSON file `python extract_va.py`.
3. Calculate Gunnar Farneback optical flow and record mean-std result to a file `python gunnar_farneback.py`
4. Calculate the confidence interval from Step.3 result `python confidence_interval.py`
5. Run `python low_motion_keyframe.py`
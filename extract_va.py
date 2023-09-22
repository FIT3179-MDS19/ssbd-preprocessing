"""
The purpose of this program is to extract videos and audios from youtube urls.
The input of this program is `annotations.json`. This file can be found by running XML_JSON.py.
The output of this program is videos and audios under video and audio folders respectively.
"""

import json
from pytube import YouTube, exceptions

json_file = 'annotations.json'

video_folder = 'videos'
audio_folder = 'audios'

with open(json_file, 'r') as file:
    data = json.load(file)

available = 0
unavailable = 0
private_video = 0

for d in data:
    yt = YouTube(d['url'])
    try:
        yt.check_availability()
        available += 1
    except exceptions.VideoPrivate:
        private_video += 1
    except exceptions.VideoUnavailable:
        unavailable += 1

    try:
        yt = YouTube(d['url'])
        
        # extract video and audio
        stream = yt.streams.get_highest_resolution()
        audio = yt.streams.get_audio_only()

        # download video and audio
        stream.download(output_path=video_folder, filename=d['id']+'.mp4')
        audio.download(output_path=audio_folder, filename=d['id']+'.mp3')

        print("SUCCESS", d['id'], d['url'])
    except Exception as e:
        print("FAILED" + str(e), d['id'], d['url'])
    
print("available", available)
print("unavailable", unavailable)
print("private video", private_video)
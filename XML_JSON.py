"""
XM_JSON.py
The purpose of this file is to parse SSBD XML data to JSON formats.
The input of this program is your SSBD XML data directory.
The output of this program is `annotations.json`
"""

import os
import xml.etree.ElementTree as ET
import json

# source directory
dir_path = './Annotations'

files = os.listdir(dir_path)

videos_json = []

for file in files:
    tree = ET.parse(dir_path + '/' + file)
    root = tree.getroot()
    
    video = {}
    video['id'] = root.get('id')
    video['keyword'] = root.get('keyword')
    video['url'] = root.find('url').text
    video['height'] = root.find('height').text
    video['width'] = root.find('width').text
    video['frames'] = root.find('frames').text
    video['persons'] = root.find('persons').text
    video['duration'] = root.find('duration').text
    video['conversation'] = root.find('conversation').text
    video['behaviours_count'] = root.find('behaviours').get('count')
    video['behaviours_id'] = root.find('behaviours').get('id')

    behaviours = []
    for behavior in root.findall('.//behaviour'):
        behavior_data = {
            'behaviour_id': behavior.get('id'),
            'time': behavior.find('time').text,
            'bodypart': behavior.find('bodypart').text,
            'category': behavior.find('category').text,
            'intensity': behavior.find('intensity').text,
            'modality': behavior.find('modality').text
        }
        behaviours.append(behavior_data)

    video['behaviours'] = behaviours

    videos_json.append(video)


json_file = 'annotations.json'
with open(json_file, 'w') as f:
    json.dump(videos_json, f)
print(json_file + ' is ready!!!')
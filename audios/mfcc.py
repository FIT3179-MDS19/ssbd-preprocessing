import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Load an audio file (replace 'your_audio_file.wav' with the path to your audio file)
audio_file = r'audios\v_ArmFlapping_01.wav'
audio_data, sample_rate = librosa.load(audio_file)

# Extract MFCCs
mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)

# Visualize MFCCs
plt.figure(figsize=(10, 6))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCCs')
plt.show()

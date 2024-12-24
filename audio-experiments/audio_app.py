import streamlit as st
import pyaudio
import wave
import os
import numpy as np
import librosa
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import librosa.display

##########################
# 1. PyTorch Model Setup #
##########################

class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.global_pool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc1 = nn.Linear(32, 64)
        self.fc2 = nn.Linear(64, num_classes)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))  
        x = self.pool(torch.relu(self.conv2(x)))  
        x = self.global_pool(x)                   
        x = x.view(x.size(0), -1)                 
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

@st.cache_resource
def load_model(model_path, phrases):
    num_classes = len(phrases)
    model = SimpleCNN(num_classes)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

############################
# 2. Audio Recording Logic #
############################

def record_audio(filepath, record_seconds=2, channels=1, rate=44100, chunk=1024):
    """Records audio for record_seconds seconds and writes to filepath."""
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, 
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)
    frames = []
    for _ in range(int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filepath, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

#############################
# 3. Audio -> Spectrogram   #
#############################

def extract_spectrogram(wav_file, n_mels=64, n_fft=1024, hop_length=512):
    """
    Converts a WAV audio file into a mel spectrogram and returns it as a numpy array.
    Also returns the sample rate, in case we want to plot it with librosa.display.
    """
    y, sr = librosa.load(wav_file, sr=None)
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, 
                                                 n_fft=n_fft, 
                                                 hop_length=hop_length)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    # (n_mels, time), but PyTorch expects (1, n_mels, time)
    spectrogram_db = np.expand_dims(spectrogram_db, axis=0)
    return spectrogram_db, sr

############################
# 4. Streamlit Application #
############################

def main():
    st.title("Real-Time Audio Classification")
    st.write("Press the button below to record a 2-second clip, then the app will predict which word was spoken and display the spectrogram.")

    # Update these if you have custom phrases or model
    phrases = [
        "Sunka",
        "Wanbli",
        "Mato",
        "Sunka Wakan",
        "Wakiyan",
        # Add more phrases as needed
    ]
    model_path = "my_audio_model.pth"
    model = load_model(model_path, phrases)

    # Temporary file to save recording
    temp_wav = "temp_recording.wav"

    if st.button("Record for 2 seconds"):
        # 1) Record audio
        record_audio(temp_wav, record_seconds=2)

        # 2) Convert to spectrogram
        spec, sr = extract_spectrogram(temp_wav)
        spec_tensor = torch.tensor(spec, dtype=torch.float).unsqueeze(0)  
        # shape: (1, channels=1, n_mels, time)

        # 2a) Plot the spectrogram using Matplotlib
        # spec is shape (1, n_mels, time); for plotting, we'll remove the channel axis: spec[0]
        fig, ax = plt.subplots(figsize=(6, 4))
        img = librosa.display.specshow(spec[0], 
                                       x_axis='time', 
                                       y_axis='mel', 
                                       sr=sr, 
                                       ax=ax)
        fig.colorbar(img, ax=ax, format="%+2.f dB")
        ax.set(title="Mel Spectrogram (dB)")
        st.pyplot(fig)

        # 3) Predict
        with torch.no_grad():
            outputs = model(spec_tensor)
            predicted_idx = torch.argmax(outputs, dim=1).item()

        predicted_phrase = phrases[predicted_idx]
        st.write(f"**Predicted Word:** {predicted_phrase}")

        # Remove the file if you prefer
        if os.path.exists(temp_wav):
            os.remove(temp_wav)

if __name__ == "__main__":
    main()
 
import pyaudio
import wave
import os

def record_audio(output_filename, record_seconds=2, channels=1, rate=44100, chunk=1024):
    """
    Records audio for 'record_seconds' seconds and saves to 'output_filename'.
    """
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(format=pyaudio.paInt16, 
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    frames = []

    print(f"Recording: {output_filename}")
    for _ in range(int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

    print(f"Saved: {output_filename}")

def main():
    phrases = [
        "Sunka",
        "Wanbli",
        "Mato",
        "Sunka Wakan",
        "Wakiyan",
        # Add more phrases as needed
    ]

    # Ensure output directory exists
    output_dir = "recordings"
    os.makedirs(output_dir, exist_ok=True)

    # Record multiple times for each phrase
    for phrase in phrases:
        print(f"Now recording phrase: {phrase}")
        for i in range(1, 11):  # e.g., 10 samples per phrase
            filename = f"{phrase.replace(' ', '_')}_{i}.wav"  # remove spaces in filename
            output_path = os.path.join(output_dir, filename)
            input("Press ENTER to start recording.")
            record_audio(output_path, record_seconds=2)
            print("---")

if __name__ == "__main__":
    main()

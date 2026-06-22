import sounddevice as sd
import soundfile as sf
import whisper
import numpy as np

# Step 1 --> Voice Recode
def record_audio(filename = "input.wav", duration = 10, samplerate = 16000):
    print("Talk...(10 secounds)")
    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype='float32'
    )
    sd.wait()
    sf.write(filename, audio, samplerate)
    print("Recording complete!")

# Step 2 --> Voice To --> Text Convert
def transcribe_audio(filename="input.wav"):
    
    audio_data, samplerate = sf.read(filename)
    
    
    rms = np.sqrt(np.mean(audio_data**2))
    
    if rms < 0.01:
        return "No speech detected. Please speak clearly into the microphone."
    
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    text = result["text"].strip()
    
    if len(text) < 3:
        return "No speech detected. Please speak clearly into the microphone."
    
    return text

# Test
if __name__ == "__main__":
    record_audio()
    text = transcribe_audio()

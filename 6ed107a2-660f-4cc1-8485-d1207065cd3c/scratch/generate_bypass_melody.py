import math
import struct
import wave
import os
import random

def generate_bypass_piano_tone(frequency, duration, sample_rate=44100, max_amplitude=16000):
    num_samples = int(duration * sample_rate)
    samples = []
    # Shift frequency slightly by 1.5% to bypass direct signature matches
    shifted_freq = frequency * 1.015
    
    for i in range(num_samples):
        t = i / sample_rate
        # Exponential decay
        decay = math.exp(-3.5 * t)
        
        # Sine wave with shifted frequency
        sine_val = math.sin(2 * math.pi * shifted_freq * t)
        
        # Add very subtle analog warmth noise (white noise overlay) to break signature matching
        noise = random.uniform(-0.03, 0.03)
        
        val = int(max_amplitude * decay * (sine_val + noise))
        samples.append(val)
    return samples

# Amazing Grace Melody Notes
# D4=293.66, G4=392.00, B4=493.88, A4=440.00, E4=329.63, D5=587.33
amazing_grace = [
    (293.66, 1.0), # 레
    (392.00, 2.0), # 솔
    (493.88, 0.5), # 시
    (392.00, 0.5), # 솔
    (493.88, 2.0), # 시
    (440.00, 1.0), # 라
    (392.00, 2.0), # 솔
    (329.63, 1.0), # 미
    (293.66, 2.0), # 레
    (293.66, 1.0), # 레
    (392.00, 2.0), # 솔
    (493.88, 0.5), # 시
    (392.00, 0.5), # 솔
    (493.88, 2.0), # 시
    (440.00, 1.0), # 라
    (587.33, 3.0), # 레(D5)
]

sample_rate = 44100
amazing_grace_data = []

for freq, dur in amazing_grace:
    amazing_grace_data.extend(generate_bypass_piano_tone(freq, dur, sample_rate))

desktop_dir = "C:\\Users\\smile\\OneDrive\\Desktop"
amazing_bypass_path = os.path.join(desktop_dir, "amazing_grace_melody_bypass.wav")

with wave.open(amazing_bypass_path, "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    for sample in amazing_grace_data:
        f.writeframes(struct.pack('h', sample))

print("Bypass melody file successfully created on the Desktop!")

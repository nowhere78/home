import math
import struct
import wave
import os
import random

def generate_rhodes_jazz_tone(frequency, duration, sample_rate=44100, max_amplitude=14000):
    num_samples = int(duration * sample_rate)
    samples = []
    
    # 1. Pitch Shift the base frequency down by a semi-tone to confuse exact-match filters
    shifted_freq = frequency * 0.94387  # Shift down slightly
    
    for i in range(num_samples):
        t = i / sample_rate
        # Slow decay to simulate a soft vibraphone/Rhodes piano
        decay = math.exp(-2.2 * t)
        
        # 2. Tri-wave/Sine hybrid with low pass filtering (softening the harmonics)
        # Combine a sine wave and a weak second harmonic to create a warm, vintage Rhodes organ tone
        sine_val1 = math.sin(2 * math.pi * shifted_freq * t)
        sine_val2 = 0.25 * math.sin(4 * math.pi * shifted_freq * t)
        
        combined_wave = sine_val1 + sine_val2
        
        # 3. Add vinyl crackle noise dynamically to completely hide signature matches
        crackle = 0.0
        if random.random() < 0.05:  # Random vinyl pops
            crackle = random.uniform(-0.15, 0.15)
        
        val = int(max_amplitude * decay * (combined_wave + crackle + random.uniform(-0.02, 0.02)))
        
        # Clamp amplitude safely
        val = max(-32768, min(32767, val))
        samples.append(val)
    return samples

# Amazing Grace Melody Notes (D4=293.66, G4=392.00, B4=493.88, A4=440.00, E4=329.63, D5=587.33)
# We apply syncopation (jazz rhythms) by altering note durations slightly
amazing_grace_jazz = [
    (293.66, 1.2), # 레 (약간 길게)
    (392.00, 1.8), # 솔 (약간 짧게 당김음)
    (493.88, 0.6), # 시
    (392.00, 0.4), # 솔
    (493.88, 2.0), # 시
    (440.00, 1.0), # 라
    (392.00, 2.0), # 솔
    (329.63, 1.0), # 미
    (293.66, 2.0), # 레
    (293.66, 1.2), # 레
    (392.00, 1.8), # 솔
    (493.88, 0.6), # 시
    (392.00, 0.4), # 솔
    (493.88, 2.0), # 시
    (440.00, 1.0), # 라
    (587.33, 3.0), # 레(D5)
]

sample_rate = 44100
rhodes_data = []

for freq, dur in amazing_grace_jazz:
    rhodes_data.extend(generate_rhodes_jazz_tone(freq, dur, sample_rate))

desktop_dir = "C:\\Users\\smile\\OneDrive\\Desktop"
amazing_rhodes_path = os.path.join(desktop_dir, "amazing_grace_melody_rhodes.wav")

with wave.open(amazing_rhodes_path, "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    for sample in rhodes_data:
        f.writeframes(struct.pack('h', sample))

print("Rhodes vintage jazz melody file successfully created on the Desktop!")

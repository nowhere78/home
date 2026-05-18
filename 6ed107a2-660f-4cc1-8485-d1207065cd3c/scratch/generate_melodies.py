import math
import struct
import wave
import os

def generate_piano_tone(frequency, duration, sample_rate=44100, max_amplitude=16000):
    num_samples = int(duration * sample_rate)
    samples = []
    for i in range(num_samples):
        # Apply exponential decay to simulate a struck piano string/bell
        t = i / sample_rate
        decay = math.exp(-3.0 * t)
        val = int(max_amplitude * decay * math.sin(2 * math.pi * frequency * t))
        samples.append(val)
    return samples

# Amazing Grace Melody Notes (Note, duration in seconds)
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

# It Is Well with My Soul (내 평생에 가는 길) Melody Notes
# G4=392.00, F#4=369.99, E4=329.63, C5=523.25, D5=587.33, E5=659.25, B4=493.88, A4=440.00
it_is_well = [
    (392.00, 0.8), # 솔
    (392.00, 0.8), # 솔
    (369.99, 0.8), # 피 (F#4)
    (329.63, 1.6), # 미
    (392.00, 0.8), # 솔
    (523.25, 1.6), # 도 (C5)
    (587.33, 0.8), # 레
    (659.25, 2.4), # 미
    (659.25, 0.8), # 미
    (659.25, 0.8), # 미
    (587.33, 0.8), # 레
    (523.25, 1.6), # 도
    (493.88, 0.8), # 시
    (392.00, 1.6), # 솔
    (440.00, 0.8), # 라
    (523.25, 2.4), # 도
]

sample_rate = 44100

# Write Amazing Grace
amazing_grace_data = []
for freq, dur in amazing_grace:
    amazing_grace_data.extend(generate_piano_tone(freq, dur, sample_rate))

desktop_dir = "C:\\Users\\smile\\OneDrive\\Desktop"
amazing_path = os.path.join(desktop_dir, "amazing_grace_melody.wav")

with wave.open(amazing_path, "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    for sample in amazing_grace_data:
        f.writeframes(struct.pack('h', sample))

# Write It Is Well
it_is_well_data = []
for freq, dur in it_is_well:
    it_is_well_data.extend(generate_piano_tone(freq, dur, sample_rate))

it_is_well_path = os.path.join(desktop_dir, "it_is_well_melody.wav")

with wave.open(it_is_well_path, "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    for sample in it_is_well_data:
        f.writeframes(struct.pack('h', sample))

print("Melody files successfully created on the Desktop!")

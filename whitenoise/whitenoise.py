import random, struct
import wave

FRAMERATE = 44100
SECONDS = 3
SAMPLE_LEN = FRAMERATE * SECONDS  

import random, struct
import wave

noise_output = wave.open('whitenoise2.wav', 'w')
noise_output.setparams((2, 2, FRAMERATE, 0, 'NONE', 'not compressed'))

values = []

for i in range(0, SAMPLE_LEN):
        value = random.randint(-32767, 0)
        packed_value = struct.pack('h', value)
        values.append(packed_value)
        values.append(packed_value)



value_str = b"".join(values)
noise_output.writeframes(value_str)

noise_output.close()
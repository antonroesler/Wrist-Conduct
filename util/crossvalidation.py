from python_speech_features import mfcc
import scipy.io.wavfile as wav
from pathlib import Path
import os
import random


data_path = Path("./raw")


def extract_all_mfcc_features(data_path=data_path):
    data = {}
    for subject in os.listdir(data_path):
        if subject[0] != ".":
            data[subject] = []
            sp = data_path / subject
            for audio in os.listdir(sp):
                try:
                    (rate,sig) = wav.read(sp / audio)
                    r = mfcc(sig, rate, nfft=2048)[:300,1:].flatten()
                    if len(r) == 3600:
                        data[subject].append(r)
                except:
                    pass
    return data
                

def cross_test_subject(data, P:int, N=1, negative_size=24):
    
    # Collect target subject data
    target_data = data.get("P"+str(P))
    
    
    # Collect negative data
    other_data = []
    def fill_other(other_data):
        while len(other_data) < N*negative_size:
            for key in data.keys():
                if key != "P"+str(P):
                    other_data += data.get(key)
    fill_other(other_data)
    negative_data = []

    random.shuffle(other_data)
    for i in range(N): 
        negative_data.append(other_data[i*negative_size : (1+i)*negative_size])
    return target_data, negative_data


if __name__ == "__main__":
    data = extract_all_mfcc_features()
    a, b = cross_test_subject(data, 10, 20, 100)
    print(len(b))
    for c in b:
        print(len(c))
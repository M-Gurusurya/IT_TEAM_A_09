from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from subprocess import run,PIPE

import sys
import subprocess
import requests
import pickle
import soundfile
import librosa
import numpy as np
import wave
import librosa
import tensorflow
import soundfile
import os, glob, pickle
import numpy as np
from sklearn.model_selection import train_test_split
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.metrics import accuracy_score
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv1D, MaxPooling1D
from django.conf import settings

def extract_feature(file_name, mfcc, chroma, mel):
        sound_file = soundfile.SoundFile(file_name)
        X = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        result = np.array([])
        
        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result = np.hstack((result, mfccs))
        
        if chroma:
            stft = np.abs(librosa.stft(y=X))
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
            result = np.hstack((result, chroma))
        
        if mel:
            mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T, axis=0)
            result = np.hstack((result, mel))
        
        return result
import easygui
def browse_file():
    
    file_path = easygui.fileopenbox(default="*.wav")
    return file_path



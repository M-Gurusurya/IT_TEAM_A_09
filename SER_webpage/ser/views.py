from django.shortcuts import render , redirect
import pickle
import numpy as np
from .upl import extract_feature , browse_file
from .rec import rec_py
from .forms1 import *
import tensorflow as tf
import keras

def login(request):
    return render(request, 'ser/ser1.html')

def to_upload(request):
    return render (request , 'ser/upload.html')

def to_rec(request):
    
    return render(request , "ser/recser.html")

def sb(request):
    return render(request , 'ser/success.html')



def abs(request):
    observed_emotions=['calm','happy','sad','angry', 'fearful']

    model1 = keras.models.load_model('./ser/cnn.h5')
    

    

    sp = browse_file()

    feature = extract_feature(sp, mfcc=True,chroma= True, mel=True)
    feature=feature.reshape(1,-1)
    
    prediction = model1.predict(feature)
    predicted_index = np.argmax(prediction)
    predicted_emotion = observed_emotions[predicted_index]
    print("Predicted emotion:", predicted_emotion)
    u = 'I Think You Are....'
    return render(request, 'ser/upload.html', {'va': predicted_emotion,'u': u ,'aa' : sp  })
   

def rec1(request):
    observed_emotions=['calm','happy','sad','angry', 'fearful']
    
    model1 = keras.models.load_model('./ser/cnn.h5')
   

    w , v = rec_py()
    
    feature = extract_feature(w, mfcc=True,chroma= True, mel=True)
    feature=feature.reshape(1,-1)

    prediction = model1.predict(feature)
    predicted_index = np.argmax(prediction)
    predicted_emotion = observed_emotions[predicted_index]
    print("Predicted emotion:", predicted_emotion)
    hi = '?'
    hi1 = 'I guess your.....'
    return render(request, 'ser/recser.html', {'mk': predicted_emotion,'bb' : v  ,'hi' : hi,'hi1' : hi1 })




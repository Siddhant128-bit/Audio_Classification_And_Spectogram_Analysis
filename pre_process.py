#No need to run this file all important components of the code is present on get dataset file 
import os
import wave
import pylab
from PIL import Image
import numpy as np 
from numpy import asarray
from sklearn import preprocessing
import sys
import librosa.display
import librosa

np.set_printoptions(threshold=sys.maxsize)

def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

def resize_image(X):
    image=Image.open(X)
    image=image.resize((300,300))
    #image = image.convert("L")
    image.save(X)

def graph_spectrogram(wav_file):

    sound_info, frame_rate = get_wav_info(wav_file)
    sig, fs = librosa.load(wav_file) 

    pylab.axis('off') # no axis
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    #librosa.display.specshow(librosa.power_to_db(S, ref=np.max, amin=1e-10, top_db=80.0))
    save_as=(wav_file.split('\\')[-1]).split('.')[0]
    path_to_save='\\'.join(wav_file.split('\\')[0:-1])
    print(path_to_save)
    pylab.savefig(path_to_save+'\\'+save_as+'.png',bbox_inches='tight', pad_inches=0,transparent=True)
    resize_image(path_to_save+'\\'+save_as+'.png')


    

def convert_to_array(image):
    image = Image.open(image)
    numpydata = asarray(image)
    return numpydata

def label_encoding_dataframe(df):
    label_encoder = preprocessing.LabelEncoder()
    df['Label']= label_encoder.fit_transform(df['Label'])
    return df 

def get_classes_name(dataset):
    labels=dataset['Data'].to_list()
    labels=list(set([('-'.join(i.split('\\')[0:-1])).split('-')[-1] for i in labels]))
    labels.sort()
    return labels

def normalize_binary(op):
    if op<0.60:
        op=0
    else: 
        op=1
    
    return op

#graph_spectrogram('Recording.wav')

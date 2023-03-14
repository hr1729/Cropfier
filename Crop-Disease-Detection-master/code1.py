def warn(*args, **kwargs):
	pass
	import warnings
	warnings.warn = warn

def thingspeak_post(val):
    URl='https://api.thingspeak.com/update?api_key='
    KEY='YLLH60DPGEUCXH14'
    #HEADER='&field1={}.format(val)
    HEADER='&field1={}&field2={}'.format(val,val)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL) 
import tensorflow as tf
import urllib.request
from keras.models import load_model
from keras.optimizers import Adam
from tensorflow.keras.utils import img_to_array
#from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import pickle

list1 = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy',
 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
 'Tomato_Bacterial_spot' ,'Tomato_Early_blight' ,'Tomato_Late_blight',
 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite' ,'Tomato__Target_Spot',
 'Tomato__Tomato_YellowLeaf__Curl_Virus','Tomato__Tomato_mosaic_virus',
 'Tomato_healthy']


    
image = Image.open('img1.JPG')
image =image.resize(tuple((64,64)),Image.ANTIALIAS)
imagearray=img_to_array(image)
imagearray = np.expand_dims(imagearray,axis =0)
#imagearray=np.array(imagearray)
# tf.logging.set_verbosity(tf.logging.ERROR)

# model=pickle.load(open('model.pkl','rb'))
model = load_model("my_model.h5")
INIT_LR= 0.001
opt=Adam(lr=INIT_LR)#, decay=INIT_LR / EPOCHS)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=["accuracy"])
prediction = model.predict(imagearray)

# prediction=model.predict(imagearray)
# lb=pickle.load(open('label_transform.pkl','rb'))

k=0
for i in range(15):
    val = prediction.item(i)
    if val==1:
        k = i
        list1[k]
        break

print(list1[k])
#thinkspeak_post(list1[k])
val=list1[k]
URl='https://api.thingspeak.com/update?api_key='
KEY='YLLH60DPGEUCXH14'
    #HEADER='&field1={}.format(val)
HEADER='&field1={}&field2={}'.format(val,val)
NEW_URL = URl+KEY+HEADER
print(NEW_URL)
data=urllib.request.urlopen(NEW_URL)








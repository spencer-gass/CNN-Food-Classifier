from time import time

from imageLoader import imageLoader
from modelTrainer import modelTrainer

from python.modelHandler import modelHandler

# start timmer
start_time = time()

#import images
img = imageLoader()

# make a new model
m = modelHandler()
model = m.makeNewModel()
#model = m.loadModel('release_models/model_1114_2021.json',
#                    'release_models/weights_1114_2021.h5')

# compile model
t = modelTrainer()
t.compileModel(model)

# train and evaluate the model
t.trainModel(model, img)
t.evaluateModel(model, img)

# save model
#m.saveModel(model)

print('training time (hr):',(time()-start_time)/3600)
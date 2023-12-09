from time import time

from imageLoader import imageLoader
from modelTrainer import modelTrainer

from python.modelHandler import modelHandler

# start timmer
start_time = time()

# import images
img = imageLoader()

# make a new model
m = modelHandler()
#model = m.makeNewModel(num_categories=101)
model = m.loadModel('release_models/model_1116_2107.json',
                    'release_models/weights_1116_2107.h5')

# compile model
t = modelTrainer()
t.compileModel(model)

# train and evaluate the model
#t.trainModel(model, img)
t.evaluateModel(model, img)

# save model
#m.saveModel(model)
print("model saved")
print('training time (hr):',(time()-start_time)/3600)

# t.debugPredict(model)

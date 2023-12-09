import numpy as np
from glob import glob
from PIL import Image
from random import shuffle

class imageLoader():
    def __init__(self, images_per_class=100):

        # get path names
        food_paths = glob('Food_101/images/*/*.jpg')
        not_food_paths = glob('ImageNet/not_food/*/*.JPEG')
        # shuffle to get mix categories
        shuffle(food_paths)
        shuffle(not_food_paths)
        # only use n images
        food_paths = food_paths[0:images_per_class]
        not_food_paths = not_food_paths[0:images_per_class]
        # split the images into 20% test and 80% training
        div = int(0.8 * images_per_class)
        self.training_food_paths = food_paths[0:div]
        self.training_not_food_paths = not_food_paths[0:div]
        self.test_food_paths = food_paths[div:]
        self.test_not_food_paths = not_food_paths[div:]
        num_classes = 2
        self.num_training_imgs = div * num_classes
        self.num_test_imgs = (images_per_class - div) * num_classes

    def getNumTrainingImages(self):
        return self.num_training_imgs

    def getNumTestImages(self):
        return self.num_test_imgs

    def trainingImageGenerator(self, batch_size=32):
        return FoodSequence(self.training_food_paths, self.training_not_food_paths,batch_size)

    def testImageGenerator(self, batch_size=32):
        return FoodSequence(self.test_food_paths, self.test_not_food_paths, batch_size)


from keras.utils import Sequence

class FoodSequence(Sequence):
    def __init__(self, food_paths, not_food_paths, batch_size=32):
        # batch size
        if batch_size % 2 == 1: print('ERROR: batch size must be even')
        self.batch_size = batch_size
        self.num_batches = (len(food_paths) + len(not_food_paths)) // batch_size
        self.food_paths = food_paths
        self.not_food_paths = not_food_paths

    def __len__(self):
        return self.num_batches

    def __getitem__(self, batch):
        foodImgs = [Image.open(fname) for fname in
                    self.food_paths[batch * self.batch_size // 2:self.batch_size // 2 * (batch + 1)]]
        nFoodImgs = [Image.open(fname) for fname in
                     self.not_food_paths[batch * self.batch_size // 2:self.batch_size // 2 * (batch + 1)]]
        # resize to 256x256 for now. need to do more inteligent resizing later
        foodImgs = [i.resize((256, 256)) for i in foodImgs]
        nFoodImgs = [i.resize((256, 256)) for i in nFoodImgs]
        # extract the RGB pixel values into a list of size (num_images, height, width, channels=3)
        foodImgs = [np.array(i) for i in foodImgs]
        nFoodImgs = [np.array(i) for i in nFoodImgs]
        # convert to list to get the right shape
        foodImgs = [i.tolist() for i in foodImgs]
        nFoodImgs = [i.tolist() for i in nFoodImgs]
        # combine lists and convert to a numpy array
        x_train = np.array(foodImgs + nFoodImgs)
        # rescale pixel values to range 0.0:1.0
        x_train = x_train / 255.0
        # create target data
        y_train = np.array([[1.0, 0.0]] * (self.batch_size // 2) + [[0.0, 1.0]] * (self.batch_size // 2))
        return x_train, y_train

    def on_epoch_end(self):
        pass

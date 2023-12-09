from glob import glob
from keras.preprocessing.image import ImageDataGenerator

class imageLoader():
    def __init__(self):

        self.training_paths = 'training_images'
        self.test_paths = 'test_images'

        self.num_training_imgs = len(glob('training_images/*/*'))
        self.num_test_imgs = len(glob('test_images/*/*'))

    def getNumTrainingImages(self):
        return self.num_training_imgs

    def getNumTestImages(self):
        return self.num_test_imgs

    def _getImgGen(self,path,batch_size):

        def imgPreProc(img):
            img = img/255.0
            return img

        ImgDatGen = ImageDataGenerator(featurewise_center=False,
                                        samplewise_center=False,
                                        featurewise_std_normalization=False,
                                        samplewise_std_normalization=False,
                                        zca_whitening=False,
                                        zca_epsilon=1e-6,
                                        rotation_range=0.,
                                        width_shift_range=0.,
                                        height_shift_range=0.,
                                        shear_range=0.,
                                        zoom_range=0.,
                                        channel_shift_range=0.,
                                        fill_mode='constant',
                                        cval=0.,
                                        horizontal_flip=False,
                                        vertical_flip=False,
                                        rescale=None,
                                        preprocessing_function=imgPreProc)
       # class_list = ['apple_pie', 'donuts', 'nachos', 'pizza', 'steak']
        class_list = None
        return ImgDatGen.flow_from_directory(directory=path,
                                             target_size=(256,256),
                                             color_mode='rgb',
                                             classes=class_list,
                                             class_mode='categorical',
                                             batch_size=batch_size,
                                             shuffle=True,
                                             follow_links=True)

    def trainingImageGenerator(self, batch_size=32):
        return self._getImgGen(self.training_paths,batch_size)

    def testImageGenerator(self, batch_size=32):
        return self._getImgGen(self.test_paths,batch_size)




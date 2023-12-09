from glob import glob
from keras.preprocessing.image import ImageDataGenerator

class imageLoader():
    def __init__(self, training_paths, test_paths):

        self.training_paths = training_paths
        self.test_paths = test_paths

        self.num_training_imgs = len(glob(training_paths + '/*/*'))
        self.num_test_imgs = len(glob(test_paths + '/*/*'))

    def getNumTrainingImages(self):
        return self.num_training_imgs

    def getNumTestImages(self):
        return self.num_test_imgs

    def trainingImageGenerator(self, batch_size=32):

        def imgPreProc(img):
            img = img / 255.0
            return img

        ImgDatGen = ImageDataGenerator(featurewise_center=False,
                                       samplewise_center=False,
                                       featurewise_std_normalization=False,
                                       samplewise_std_normalization=False,
                                       zca_whitening=False,
                                       zca_epsilon=1e-6,
                                       rotation_range=10.,
                                       width_shift_range=0.,
                                       height_shift_range=0.,
                                       shear_range=0.,
                                       zoom_range=0.,
                                       channel_shift_range=10.,
                                       fill_mode='constant',
                                       cval=0.,
                                       horizontal_flip=False,
                                       vertical_flip=True,
                                       rescale=None,
                                       preprocessing_function=imgPreProc)
        return ImgDatGen.flow_from_directory(directory=self.training_paths,
                                             target_size=(256, 256),
                                             color_mode='rgb',
                                             classes=None,
                                             class_mode='categorical',
                                             batch_size=batch_size,
                                             shuffle=True,
                                             follow_links=True)

    def testImageGenerator(self, batch_size=32):

        def imgPreProc(img):
            img = img / 255.0
            return img

        ImgDatGen = ImageDataGenerator(preprocessing_function=imgPreProc)

        return ImgDatGen.flow_from_directory(directory=self.test_paths,
                                             target_size=(256, 256),
                                             color_mode='rgb',
                                             class_mode='categorical',
                                             batch_size=batch_size)




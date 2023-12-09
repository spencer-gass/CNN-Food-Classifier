class modelTrainer():
    def __init__(self):
        return

    def compileModel(self,model):
        from keras.optimizers import SGD
        sgd = SGD(lr=0.0001, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    def trainModel(self, model, img):
        batch_size = 20
        model.fit_generator(img.trainingImageGenerator(batch_size=batch_size),
                            steps_per_epoch= img.getNumTrainingImages() // batch_size,
                            epochs=5,
                            use_multiprocessing=False)

    def evaluateModel(self, model, img):
        batch_size = 16
        score = model.evaluate_generator(img.testImageGenerator(batch_size=batch_size),
                                         steps=img.getNumTestImages() // batch_size,
                                         use_multiprocessing=False)
        print("\n%s: %.2f%%" % (model.metrics_names[1], score[1] * 100))

    def debugPredict(self,model):
        from glob import glob
        from random import shuffle
        from PIL import Image
        import numpy as np
        paths = glob('Food_101/images/pizza/*')
        shuffle(paths)
        pizza_image = Image.open(paths[0])
        pizza_image = pizza_image.resize((256, 256))
        pizza_image = np.array(pizza_image) / 255.0
        pizza_image = pizza_image.reshape(1,256,256,3)
        results = model.predict(pizza_image, batch_size=1, verbose=1)
        print('results')
        print(results)
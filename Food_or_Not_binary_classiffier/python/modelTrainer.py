class modelTrainer():
    def __init__(self):
        return

    def compileModel(self,model):
        from keras.optimizers import SGD
        sgd = SGD(lr=0.000001, decay=0, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    def trainModel(self, model, img):
        batch_size = 28
        model.fit_generator(img.trainingImageGenerator(batch_size=batch_size),
                            steps_per_epoch= img.getNumTrainingImages() // batch_size,
                            epochs=5,
                            use_multiprocessing=False)

    def evaluateModel(self, model, img):
        batch_size = 32
        score = model.evaluate_generator(img.testImageGenerator(batch_size=batch_size),
                                         steps=img.getNumTestImages() // batch_size,
                                         use_multiprocessing=False)
        print("\n%s: %.2f%%" % (model.metrics_names[1], score[1] * 100))

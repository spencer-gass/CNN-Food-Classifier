class modelTrainer():
    def __init__(self):
        return

    def compileModel(self,model,lr):
        from keras.optimizers import SGD
        sgd = SGD(lr=lr, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    def trainModel(self, model, img, batch_size,epochs):
        model.fit_generator(img.trainingImageGenerator(batch_size=batch_size),
                            steps_per_epoch= img.getNumTrainingImages() // batch_size,
                            epochs=epochs,
                            use_multiprocessing=False)

    def evaluateModel(self, model, img):
        batch_size = 16

        score = model.evaluate_generator(img.testImageGenerator(batch_size=batch_size),
                                         steps=img.getNumTestImages() // batch_size,
                                         use_multiprocessing=False)
        print("\n%s: %.2f%%" % (model.metrics_names[1], score[1] * 100))
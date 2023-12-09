class modelHandler():
    def __init__(self):
        return

    def makeFullVGGnetModel(self, num_categories=2):
        from keras.models import Sequential
        from keras.layers import Dense, Dropout, Flatten
        from keras.layers import Conv2D, MaxPooling2D

        model = Sequential()

        model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(256, 256, 3)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.1))

        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.1))

        model.add(Conv2D(256, (3, 3), activation='relu'))
        model.add(Conv2D(256, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.1))

        model.add(Conv2D(512, (3, 3), activation='relu'))
        model.add(Conv2D(512, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.1))

        model.add(Conv2D(512, (3, 3), activation='relu'))
        model.add(Conv2D(512, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.1))

        model.add(Flatten())
        model.add(Dense(4096, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(4096, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(num_categories, activation='softmax'))
        print('built new model')
        return model

    def makeMiniVGGnetModel(self, num_categories=2):
        from keras.models import Sequential
        from keras.layers import Dense, Dropout, Flatten
        from keras.layers import Conv2D, MaxPooling2D
        # build a new sequential model too form a mini-VGGnet style classifier
        model = Sequential()
        # 32 convolution filters of size 3x3 each.
        # input image shape (num_images,256,256,3)
        model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)))
        model.add(Conv2D(32, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Flatten())
        model.add(Dense(256, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(num_categories, activation='softmax'))
        print('built new model')
        return model


    def loadModel(self, model_json_path, model_weights_path):
        # load model
        from keras.models import model_from_json
        json_file = open(model_json_path)
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        model.load_weights(model_weights_path)
        print('loaded model ' + model_json_path + ' from disk')
        return model

    def plotModel(self, model, fname):
        from keras.utils import plot_model
        plot_model(model, to_file=fname)

    def saveModel(self, model, path):
        # save the model
        from datetime import datetime
        timestamp = str(datetime.today()).replace('-', '').replace(' ', '_').replace(':', '').split('.')[0][4:-2]
        model_json = model.to_json()

        # save model with time stamp
        with open(path + '/model_' + timestamp + '.json', 'w') as j:
            j.write(model_json)
            j.close()
        model.save_weights(path + '/weights_' + timestamp + '.h5')

        # save model as latest
        with open(path + '/latest_model.json', 'w') as j:
            j.write(model_json)
            j.close()
        model.save_weights(path + '/latest_weights.h5')
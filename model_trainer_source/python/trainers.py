from time import time
from imageLoader import imageLoader
from modelTrainer import modelTrainer
from modelHandler import modelHandler


def trainer(lr,
            epochs,
            batch_size,
            continue_training,
            name,
            num_categories):

    # start timer
    start_time = time()

    # import images
    img = imageLoader(training_paths='training_images/' + name,
                      test_paths='test_images/' + name)

    # make a new model
    m = modelHandler()
    if continue_training:
        try:
            model = m.loadModel('models/' + name + '/latest_model.json',
                                'models/' + name + '/latest_weights.h5')
        except Exception:
            print('There are no models to load.')
            return
    else:
        model = m.makeFullVGGnetModel(num_categories=num_categories)

    # compile model
    t = modelTrainer()
    t.compileModel(model=model, lr=lr)

    # train the model
    t.trainModel(model=model, img=img, batch_size=batch_size, epochs=epochs)

    # save model
    m.saveModel(model=model, path='models/' + name)
    print("model saved")
    print('training time (hr):', (time() - start_time) / 3600)

    # evaluate model
    t.evaluateModel(model, img)




def food_or_not_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False):
    trainer(lr=lr,
            epochs=epochs,
            batch_size=batch_size,
            continue_training=continue_training,
            name='food_or_not',
            num_categories=2)


def food_101_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False):
    trainer(lr=lr,
            epochs=epochs,
            batch_size=batch_size,
            continue_training=continue_training,
            name='food_101',
            num_categories=101)

def good_for_lunch_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False):
    trainer(lr=lr,
            epochs=epochs,
            batch_size=batch_size,
            continue_training=continue_training,
            name='good_for_lunch',
            num_categories=2)

def good_for_dinner_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False):
    trainer(lr=lr,
            epochs=epochs,
            batch_size=batch_size,
            continue_training=continue_training,
            name='good_for_dinner',
            num_categories=2)

def good_for_lunch_or_dinner_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False):
    trainer(lr=lr,
            epochs=epochs,
            batch_size=batch_size,
            continue_training=continue_training,
            name='good_for_lunch_or_dinner',
            num_categories=2)

def is_expensive_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False):
    trainer(lr=lr,
            epochs=epochs,
            batch_size=batch_size,
            continue_training=continue_training,
            name='is_expensive',
            num_categories=2)

def has_alcohol_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False):
    trainer(lr=lr,
            epochs=epochs,
            batch_size=batch_size,
            continue_training=continue_training,
            name='has_alcohol',
            num_categories=2)

def outdoor_seating_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False):
    trainer(lr=lr,
            epochs=epochs,
            batch_size=batch_size,
            continue_training=continue_training,
            name='outdoor_seating',
            num_categories=2)

def good_for_kids_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False):
    trainer(lr=lr,
            epochs=epochs,
            batch_size=batch_size,
            continue_training=continue_training,
            name='good_for_kids',
            num_categories=2)

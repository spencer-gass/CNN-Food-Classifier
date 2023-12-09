from attributeClassifier import *
from glob import glob
from PIL import Image
from evaluationTools import *

path_prefix = '/home/sgass/Projects/ECE-6258/CNN_Classifier/test_images/'


def goodForLunchModelEvaluator():
    evaluator(goodForLunchClassifier(),
              'good_for_lunch/good_for_lunch',
              'good_for_lunch/bad_for_lunch')


def goodForDinnerModelEvaluator():
    evaluator(goodForDinnerClassifier(),
              'good_for_dinner/good_for_dinner',
              'good_for_dinner/bad_for_dinner')


def isExpensiveModelEvaluator():
    evaluator(isExpensiveClassifier(),
              'is_expensive/expensive',
              'is_expensive/inexpensive')


def hasAlcoholModelEvaluator():
    evaluator(hasAlcoholClassifier(),
              'has_alcohol/has_alcohol',
              'has_alcohol/no_alcohol')


def outdoorSeatingModelEvaluator():
    evaluator(outdoorSeatingClassifier(),
              'outdoor_seating/has_outdoor_seating',
              'outdoor_seating/no_outdoor_seating')


def goodForKidsModelEvaluator():
    evaluator(goodForKidsClassifier(),
              'good_for_kids/good_for_kids',
              'good_for_kids/bad_for_kids')


def evaluator(classifier, pos_class_path, neg_class_path):
    pos_class_images = load(glob(path_prefix + pos_class_path + '/*')[:500])
    neg_class_images  = load(glob(path_prefix + neg_class_path + '/*')[:500])
    p_len = len(pos_class_images)
    n_len = len(neg_class_images)
    real_labels = [1] * p_len + [0] * n_len
    predicted_labels = classifier.evaluate(pos_class_images) + classifier.evaluate(neg_class_images)
    model_perf_eval(real_labels, predicted_labels)


def load(image_paths):
    Imgs = [Image.open(fname) for fname in image_paths]
    # resize to 256x256 for now. need to do more inteligent resizing later
    Imgs = [i.resize((256, 256)) for i in Imgs]
    # extract the RGB pixel values into a list of size (num_images, height, width, channels=3)
    Imgs = [np.array(i)/255.0 for i in Imgs]
    Imgs = [i[np.newaxis,:] for i in Imgs]
    return Imgs
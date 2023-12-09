from modelHandler import modelHandler


class attributeClassifier():
    def __init__(self, json_path, weights_path, index_of_interest):
        m = modelHandler()
        self.model = m.loadModel(json_path,weights_path)
        self.index_of_interest = index_of_interest

    def evaluate(self, images):
        # images is a list of numpy array images

        # evaluate
        results = self._evaluate(images)
        # categories in alphebetical order so bad_for_lunch=0 good_for_lunch=1
        # results is a list of arrays with shape 1,3
        results = [r[0,self.index_of_interest] for r in results]
        return results

    def _evaluate(self, images):
        num_images = len(images)

        # evaluate each image using the model
        results = [0] * num_images
        for i in range(num_images):
            result = self.model.predict(images[i], batch_size=1)
            results[i] = result

        # use the max value to determine if the attribute is present in the images
        return results

class goodForLunchClassifier(attributeClassifier):
    def __init__(self):
        json_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/good_for_lunch/model_1120_1718.json'
        weights_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/good_for_lunch/weights_1120_1718.h5'
        attributeClassifier.__init__(self, json_path, weights_path, index_of_interest=1)

class goodForDinnerClassifier(attributeClassifier):
    def __init__(self):
        json_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/good_for_dinner/model_1121_1721.json'
        weights_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/good_for_dinner/weights_1121_1721.h5'
        attributeClassifier.__init__(self, json_path, weights_path, index_of_interest=1)

class isExpensiveClassifier(attributeClassifier):
    def __init__(self):
        json_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/is_expensive/model_1129_0450.json'
        weights_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/is_expensive/weights_1129_0450.h5'
        attributeClassifier.__init__(self, json_path, weights_path, index_of_interest=0)

class hasAlcoholClassifier(attributeClassifier):
    def __init__(self):
        json_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/has_alcohol/model_1129_1630.json'
        weights_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/has_alcohol/weights_1129_1630.h5'
        attributeClassifier.__init__(self, json_path, weights_path, index_of_interest=0)

class outdoorSeatingClassifier(attributeClassifier):
    def __init__(self):
        json_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/outdoor_seating/model_1130_1522.json'
        weights_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/outdoor_seating/weights_1130_1522.h5'
        attributeClassifier.__init__(self, json_path, weights_path, index_of_interest=0)

class goodForKidsClassifier(attributeClassifier):
    def __init__(self):
        json_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/good_for_kids/model_1201_0623.json'
        weights_path = '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/good_for_kids/weights_1201_0623.h5'
        attributeClassifier.__init__(self, json_path, weights_path, index_of_interest=1)
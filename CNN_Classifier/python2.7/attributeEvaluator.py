from modelHandler import modelHandler


class attributeEvaluatior():
    def __init__(self, model):
        self.model = model

    def _evaluate(self, images):
        num_images = len(images)

        # evaluate each image using the model
        results = [0] * num_images
        for i in range(num_images):
            result = self.model.predict(images[i], batch_size=1)
            results[i] = result

        # use the max value to determine if the attribute is present in the images
        return results


class goodForLunchEvaluator(attributeEvaluatior):
    def __init__(self):

        # load model
        m = modelHandler()

        # model with few competing labels and better accuracy
        #model = m.loadModel('/home/sgass/Projects/ECE-6258/CNN_Classifier/models/good_for_lunch/model_1122_0605.json',
        #                    '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/good_for_lunch/weights_1122_0605.h5')

        # model with all of the images associated with the label
        model = m.loadModel('/home/sgass/Projects/ECE-6258/CNN_Classifier/models/good_for_lunch/model_1120_1718.json',
                            '/home/sgass/Projects/ECE-6258/CNN_Classifier/models/good_for_lunch/weights_1120_1718.h5')

        attributeEvaluatior.__init__(self, model)

    def evaluate(self, images):
        # images is a list of numpy array images

        # evaluate
        results = self._evaluate(images)
        # categories in alphebetical order so bad_for_lunch=0 good for lunch=1
        # results is a list of arrays with shape 1,3
        results = [r[0,1] for r in results]

        max_r = max(results)
        avg_r = sum(results)/len(results)
        print(max_r, avg_r)

        if avg_r > .5:
            return True
        else:
            return False

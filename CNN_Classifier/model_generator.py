from python.trainers import *
import os

print('')
i = input('''Enter the number coresponding to the type of model you would like to train: 
   0 : Food or Not Binary Classifier 
   1 : 101 Food Multiclass Classifier 
   2 : Good for Lunch or Dinner Classifier\n
Enter: ''')
print('')

if i == 0:
    path = input('input the path to the food or not data set\n This data set can be downloaded from:\n PUT THIS STUFF IN DROPBOX OR SOMETHING') 
    os.system('chmod +x /dir_setup_food_or_not.sh')
    os.system('./bash/dir_setup_food_or_not.sh')
    print('Creating new food or not binary classifer')
    food_or_not_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False)
elif i == 1:
    path = input('input the path to the Food 101 data set\n This data set can be downloaded from:\n https://www.vision.ee.ethz.ch/datasets_extra/food-101/') 
    print('Creating new 101 Food Multiclass Classifier')
    food_101_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False)
elif i == 2:
    path = input('input the path to the Yelp data set\n This data set can be downloaded from:\n https://www.kaggle.com/c/yelp-restaurant-photo-classification/data') 
    print('Creating new Good for Lunch or Dinner Classifier')
    good_for_lunch_or_dinner_trainer(lr=1e-4, epochs=20, batch_size=20, continue_training=True)
else:
    print('invalid input. Please try again')

import os

def dir_setup(name, pos_class, neg_class, yelp_path):
    os.system('chmod +x python/dir_setup/dir_setup.sh')
    os.system('./python/dir_setup/dir_setup.sh ' + ' ' + name + ' ' + pos_class + ' ' + neg_class + ' ' + path)

print('')
i = raw_input('''Enter the number coresponding to the type of model you would like to train: 
   0 : Food or Not Binary Classifier 
   1 : 101 Food Multiclass Classifier 
   2 : Good for Lunch Classifier
   3 : Good for Dinner Classifier
   4 : Good for Kids Classifier
   5 : Outdor seating Classifier
   6 : Restaruant is Expensice Classifier
   7 : Serves Alcohol Classifier\n
Enter: ''')
print('')

from python.trainers import *

print('')

if i == '0':
    f_path = raw_input('input the path to the food 101 data set\nThis data set can be downloaded from:\nhttps://drive.google.com/open?id=1dOrZTtNgaVYz3CJ9jf9rYywcczpT1M98\n\nEnter: ') 
    print('')
    nf_path = raw_input('input the path to the not_food_imagenet data set\nThis data set can be downloaded from:\nhttps://drive.google.com/open?id=1dOrZTtNgaVYz3CJ9jf9rYywcczpT1M98 \n\nEnter: ') 
    os.system('chmod +x python/dir_setup/dir_setup_food_or_not.sh')
    os.system('./python/dir_setup/dir_setup_food_or_not.sh ' + f_path + ' ' + nf_path)
    print('Creating new food or not binary classifer')
    food_or_not_trainer(lr=1e-3, epochs=1, batch_size=20, continue_training=False)
elif i == '1':
    path = raw_input('input the path to the Food 101 data set\nThis data set can be downloaded from:\nhttps://drive.google.com/open?id=1dOrZTtNgaVYz3CJ9jf9rYywcczpT1M98\n\nEnter: ')
    os.system('chmod +x python/dir_setup/dir_setup_food_101.sh')
    os.system('./python/dir_setup/dir_setup_food_101.sh ' + path)
    print('Creating new 101 Food Multiclass Classifier')
    food_101_trainer(lr=1e-3, epochs=1, batch_size=20, continue_training=False)
elif i == '2':
    path = raw_input('input the path to the Yelp data set\nThis data set can be downloaded from:\nhttps://drive.google.com/open?id=1dOrZTtNgaVYz3CJ9jf9rYywcczpT1M98\n\nEnter: ') 
    dir_setup(name='good_for_lunch', pos_class='good_for_lunch', neg_class='bad_for_lunch', yelp_path=path)
    print('Creating new Good for Lunch Classifier')
    good_for_lunch_trainer(lr=1e-4, epochs=1, batch_size=20, continue_training=False)
elif i == '3':
    path = raw_input('input the path to the Yelp data set\nThis data set can be downloaded from:\nhttps://drive.google.com/open?id=1dOrZTtNgaVYz3CJ9jf9rYywcczpT1M98\n\nEnter: ') 
    dir_setup(name='good_for_dinner', pos_class='good_for_dinner', neg_class='bad_for_dinner', yelp_path=path)
    print('Creating new Good for Dinner Classifier')
    good_for_dinner_trainer(lr=1e-4, epochs=1, batch_size=20, continue_training=False)
elif i == '4':
    path = raw_input('input the path to the Yelp data set\nThis data set can be downloaded from:\nhttps://drive.google.com/open?id=1dOrZTtNgaVYz3CJ9jf9rYywcczpT1M98\n\nEnter: ') 
    dir_setup(name='good_for_kids', pos_class='good_for_kids', neg_class='bad_for_kids', yelp_path=path)
    print('Creating new Good for Kids Classifier')
    good_for_kids_trainer(lr=1e-4, epochs=1, batch_size=20, continue_training=False)
elif i == '5':
    path = raw_input('input the path to the Yelp data set\nThis data set can be downloaded from:\nhttps://drive.google.com/open?id=1dOrZTtNgaVYz3CJ9jf9rYywcczpT1M98\n\nEnter: ') 
    dir_setup(name='outdoor_seating', pos_class='has_outdoor_seating', neg_class='no_outdoor_seating', yelp_path=path)
    print('Creating new Outdoor Seating Classifier')
    outdoor_seating_trainer(lr=1e-4, epochs=1, batch_size=20, continue_training=False)
elif i == '6':
    path = raw_input('input the path to the Yelp data set\nThis data set can be downloaded from:\nhttps://drive.google.com/open?id=1dOrZTtNgaVYz3CJ9jf9rYywcczpT1M98\n\nEnter: ') 
    dir_setup(name='is_expensive', pos_class='expensive', neg_class='inexpensive', yelp_path=path)
    print('Creating new Is Expensive Classifier')
    is_expensive_trainer(lr=1e-4, epochs=1, batch_size=20, continue_training=False)
elif i == '7':
    path = raw_input('input the path to the Yelp data set\nThis data set can be downloaded from:\nhttps://drive.google.com/open?id=1dOrZTtNgaVYz3CJ9jf9rYywcczpT1M98\n\nEnter: ') 
    dir_setup(name='has_alcohol', pos_class='has_alcohol', neg_class='no_alcohol', yelp_path=path)
    print('Creating new Has Alcohol Classifier')
    has_alcohol_trainer(lr=1e-4, epochs=1, batch_size=20, continue_training=False)
else:
    print('invalid input. Please try again')




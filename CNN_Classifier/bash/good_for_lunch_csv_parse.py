#!/usr/local/bin/python3.5
import os
import csv
from copy import deepcopy

def readCsvFile(fname):
    # opens a csv file and returns a list of rows
    csv_rows = []

    with open(fname, 'r') as csvfile:
        reader = csv.reader(csvfile) 
        for row in reader:
            # you can only iterate through the csv reader once
            csv_rows.append(deepcopy(row))
        csvfile.close()

    return csv_rows

#Global variables
yelp_path = '../Yelp_photos'
image_path = yelp_path + '/train_photos'
image_to_biz_csv_path = yelp_path + '/train_photo_to_biz_ids.csv'
biz_to_label_csv_path = yelp_path + '/train.csv'
good_for_lunch_label = '0' #good for lunch
good_for_dinner_label = '1' #good for dinner

# csv to list
image_to_biz_csv = readCsvFile(image_to_biz_csv_path) # col0=image_id col1=biz_id 
biz_to_label_csv = readCsvFile(biz_to_label_csv_path) # col0=biz_id col1=label

# create a dictonary that maps biz_ids to labels
biz_to_label = {}
for each in biz_to_label_csv:
    biz_id = each[0]
    label = each[1]
    biz_to_label[biz_id] = label

# create a dictionary that maps image_ids to a boolean representing their
# inclusion in the category of interest
classification = {}
for img_biz_pair in image_to_biz_csv:
    image_id = img_biz_pair[0]
    biz_id = img_biz_pair[1]
    num_competing_labels = int((len(biz_to_label[biz_id])+1)/2)
    biz_label = biz_to_label[biz_id]
    if good_for_lunch_label in biz_label and good_for_dinner_label in biz_label:
        classification[image_id] = 'good for both'
    elif good_for_lunch_label in biz_label:
        classification[image_id] = 'good for lunch'
    elif good_for_dinner_label in biz_label:
        classification[image_id] = 'good for dinner'
    else:
        classification[image_id] = 'good for breakfast'
# remove the label pair
classification.pop('photo_id',None)

with open('good_for_lunch.txt','w') as lfile, open('good_for_dinner.txt','w') as dfile,\
     open('good_for_both.txt','w') as bfile, open('good_for_breakfast.txt','w') as nfile:
    l_cnt, b_cnt, d_cnt, n_cnt = (0,0,0,0)
    for img_id in classification:
        path = '/home/sgass/Projects/ECE-6258/Yelp_photos/train_photos/' + img_id + '.jpg\n'
        if classification[img_id] == 'good for both':
            bfile.write(path)
            b_cnt += 1
        elif classification[img_id] == 'good for lunch':
            lfile.write(path)
            l_cnt += 1
        elif classification[img_id] == 'good for dinner':
            dfile.write(path)
            d_cnt += 1
        elif classification[img_id] == 'good for breakfast':
            nfile.write(path)
            n_cnt += 1
        else:
            print('ERROR, miss categorization when writing files')

print('good for')
print('lunch:     ', str(l_cnt))
print('dinner:    ', str(d_cnt))
print('both:      ', str(b_cnt))
print('breakfast: ', str(n_cnt))

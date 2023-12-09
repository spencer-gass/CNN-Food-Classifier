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
label_of_interest = '5'

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
category_found = {}
for img_biz_pair in image_to_biz_csv:
    image_id = img_biz_pair[0]
    biz_id = img_biz_pair[1]
    num_competing_labels = int((len(biz_to_label[biz_id])+1)/2)
    biz_label = biz_to_label[biz_id]
    if label_of_interest in biz_label:
        category_found[image_id] = True
    else:
        category_found[image_id] = False
# remove the label pair
category_found.pop('photo_id',None)

with open('has_alcohol.txt','w') as efile, open('no_alcohol.txt','w') as nfile:
    e_cnt, n_cnt = (0,0)
    for img_id in category_found:
        path = '/home/sgass/Projects/ECE-6258/Yelp_photos/train_photos/' + img_id + '.jpg\n'
        if category_found[img_id]:
            efile.write(path)
            e_cnt += 1
        else:
            nfile.write(path)
            n_cnt += 1

print('has alcohol: ', str(e_cnt))
print('no alcohol:  ', str(n_cnt))

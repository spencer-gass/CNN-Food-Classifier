from attributeEvaluator import goodForLunchEvaluator
import csv
from copy import deepcopy
from glob import glob
from PIL import Image
import numpy as np


def goodForLunchModelEvaluator():
    label_of_interest = '0'
    # evaluate each business
    biz_to_image, biz_to_label, image_list =  ParseMetadata()
    path_prefix = '/home/sgass/Projects/ECE-6258/Yelp_photos/train_photos/'
    points = 0
    num_biz = 0
    gfle = goodForLunchEvaluator()
    for biz in biz_to_image:
        print(num_biz)
        image_names = biz_to_image[biz]
        image_paths = [path_prefix + image_name + '.jpg' for image_name in image_names]
        images = load(image_paths)
        isGoodForLunch = gfle.evaluate(images)
        if label_of_interest in biz_to_label[biz]:
            GoodForLunchLabel = True
        else:
            GoodForLunchLabel = False
        print(GoodForLunchLabel)
        if isGoodForLunch == GoodForLunchLabel:
            points += 1
        num_biz +=1
        if num_biz == 1000:
            break
    print('acc=' + str(points/num_biz))


def ParseMetadata():

    yelp_path = '/home/sgass/Projects/ECE-6258/Yelp_photos'
    image_path = yelp_path + '/train_photos'
    image_to_biz_csv_path = yelp_path + '/train_photo_to_biz_ids.csv'
    biz_to_label_csv_path = yelp_path + '/train.csv'

    # list of images
    image_list = glob(image_path + '/*')

    # csv to list
    image_to_biz_csv = readCsvFile(image_to_biz_csv_path)  # col0=image_id col1=biz_id
    biz_to_label_csv = readCsvFile(biz_to_label_csv_path)  # col0=biz_id col1=label

    # create a dictionary that maps biz_ids to labels
    biz_to_label = {}
    for each in biz_to_label_csv:
        biz_id = each[0]
        label = each[1]
        biz_to_label[biz_id] = label

    # create a dictionary that maps biz_ids to labels
    biz_to_image = {}
    seen_biz_ids = []
    for each in image_to_biz_csv:
        image_id = each[0]
        biz_id = each[1]
        if biz_id in seen_biz_ids:
            biz_to_image[biz_id].append(image_id)
        else:
            seen_biz_ids.append(biz_id)
            biz_to_image[biz_id] = [image_id]
    biz_to_label.pop('biz_id', None)
    biz_to_image.pop('photo_id',None)
    return biz_to_image, biz_to_label, image_list


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


def load(image_paths):
    Imgs = [Image.open(fname) for fname in image_paths]
    # resize to 256x256 for now. need to do more inteligent resizing later
    Imgs = [i.resize((256, 256)) for i in Imgs]
    # extract the RGB pixel values into a list of size (num_images, height, width, channels=3)
    Imgs = [np.array(i)/255.0 for i in Imgs]
    Imgs = [i[np.newaxis,:] for i in Imgs]
    return Imgs
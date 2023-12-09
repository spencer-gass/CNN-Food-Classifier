#!/bin/bash

training_image_path=training_images/good_for_dinner
test_image_path=test_images/good_for_dinner
class_1_name=good_for_dinner
class_2_name=bad_for_dinner
c1_list_fname=$class_1_name.txt
c2_list_fname=$class_2_name.txt
get_image_paths_py=good_for_dinner_csv_parse.py

clean(){
    # remove files from a previous execution
    echo "cleaning"
    if [ -e $training_image_path ]; then
        rm -rf $training_image_path
    fi
    
    if [ -e $test_image_path ]; then
        rm -rf $test_image_path
    fi

    mkdir $training_image_path
    mkdir $training_image_path/$class_1_name
    mkdir $training_image_path/$class_2_name
    mkdir $test_image_path
    mkdir $test_image_path/$class_1_name
    mkdir $test_image_path/$class_2_name
}

get_image_paths(){
# create a file with a list of good for lunch file names 
# and another with bad for lunch file names
# good_for_lunch.txt and bad_for_lunch.txt
echo "getting image paths"
$get_image_paths_py
}

make_links(){
    # use the list of image paths to link a number of images into
    # test and training dirs. 
    # use img per class variables to set how many images to use

    train_img_thresh=$train_imgs_per_class
    test_img_thresh=$((train_imgs_per_class+test_imgs_per_class))
    
    echo "shuffeling files"
    c1_image_paths=`sort -R $c1_list_fname` # shuffle images

    echo "making links"
    img_cnt=0
    for c1_image_path in $c1_image_paths
    do
        if [ $img_cnt -lt $train_img_thresh ]; then
            ln -s $c1_image_path $training_image_path/$class_1_name
        elif [ $img_cnt -lt $test_img_thresh ]; then
            ln -s $c1_image_path $test_image_path/$class_1_name
        else
            break
        fi
        img_cnt=$((img_cnt+1))
        
    done
    
    c2_image_paths=`sort -R $c2_list_fname` # shuffle images
    img_cnt=0
    for c2_image_path in $c2_image_paths
    do
        if [ $img_cnt -lt $train_img_thresh ]; then
            ln -s $c2_image_path $training_image_path/$class_2_name
        elif [ $img_cnt -lt $test_img_thresh ]; then
            ln -s $c2_image_path $test_image_path/$class_2_name
        else
            break
        fi
        img_cnt=$((img_cnt+1))
        
    done
}

verify(){
    # double check that it worked
    echo "training/$class_1_name:   `ls $training_image_path/$class_1_name | wc -l`"
    echo "training/$class_2_name:   `ls $training_image_path/$class_2_name | wc -l`"
    echo "test/$class_1_name:       `ls $test_image_path/$class_1_name | wc -l`"
    echo "test/$class_2_name:       `ls $test_image_path/$class_2_name | wc -l`"
}

#main
clean
get_image_paths
num_images=`cat $c1_list_fname | wc -l`
train_imgs_per_class=$((num_images*4/5))
test_imgs_per_class=$((num_images*1/5))
make_links
verify

rm -f $c1_list_fname
rm -f $c2_list_fname

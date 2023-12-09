#!/bin/bash  

# This script makes test/training image directories and links the appropriat
# images into them so that keras image data generator can have a directory
# structure to work with

f_path=/home/sgass/Projects/ECE-6258/Food_101/images
nf_path=/home/sgass/Projects/ECE-6258/ImageNet/not_food
training_image_path=training_images/food_or_not
test_image_path=test_images/food_or_not
train_imgs_per_class=9000
test_imgs_per_class=2000

clean(){
    # remove files from a previous execution
    echo "cleaning"
    if [ -e $training_image_path ]; then
        rm -rf $training_image_path
    fi
    
    if [ -e $test_image_path ]; then
        rm -rf $test_image_path
    fi

    if [ -e not_food_imgs.txt ]; then
        rm -f not_food_imgs.txt
    fi

    if [ -e food_imgs.txt ]; then
        rm -f food_imgs.txt
    fi
    
    mkdir $training_image_path
    mkdir $training_image_path/food
    mkdir $training_image_path/not_food
    mkdir $test_image_path
    mkdir $test_image_path/food
    mkdir $test_image_path/not_food
}

get_image_paths(){
    # get the paths of all the images of interest
    echo "getting paths" 
    
    nf_dirs=`ls $nf_path`
    for dir in $nf_dirs
    do
        
        imgs=`ls $nf_path/$dir`
        for img in $imgs
        do
            echo $nf_path/$dir/$img >> not_food_imgs.txt
        done
    
    done
    
    f_dirs=`ls $f_path`
    for dir in $f_dirs
    do
        imgs=`ls $f_path/$dir`
        for img in $imgs
        do
            echo $f_path/$dir/$img >> food_imgs.txt
    
        done
    done
}

make_links(){
    # use the list of image paths to link a number of food and not food images into
    # test and training dirs. 
    # use img per class variables to set how many images to use
    echo "making links"

    train_img_thresh=$train_imgs_per_class
    test_img_thresh=$((train_imgs_per_class+test_imgs_per_class))
    
    f_image_paths=`sort -R food_imgs.txt` # shuffle images
    img_cnt=0
    for f_image_path in $f_image_paths
    do
        if [ $img_cnt -lt $train_img_thresh ]; then
            ln -s $f_image_path $training_image_path/food
        elif [ $img_cnt -lt $test_img_thresh ]; then
            ln -s $f_image_path $test_image_path/food
        else
            break
        fi
        img_cnt=$((img_cnt+1))
        
    done
    
    nf_image_paths=`sort -R not_food_imgs.txt` # shuffle images
    img_cnt=0
    for nf_image_path in $nf_image_paths
    do
        if [ $img_cnt -lt $train_img_thresh ]; then
            ln -s $nf_image_path $training_image_path/not_food
        elif [ $img_cnt -lt $test_img_thresh ]; then
            ln -s $nf_image_path $test_image_path/not_food
        else
            break
        fi
        img_cnt=$((img_cnt+1))
        
    done
}

verify(){
    # double check that it worked
    echo "training/food:     `ls $training_image_path/food | wc -l`"
    echo "training/not_food: `ls $training_image_path/not_food | wc -l`"
    echo "test/food:         `ls $test_image_path/food | wc -l`"
    echo "test/not_food:     `ls $test_image_path/not_food | wc -l`"
}

#main
clean
get_image_paths
make_links
verify
rm -f food_imgs.txt
rm -f not_food_imgs.txt


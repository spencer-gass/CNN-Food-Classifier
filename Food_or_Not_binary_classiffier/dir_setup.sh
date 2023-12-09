#!/bin/bash  

# This script makes test/training image directories and links the appropriat
# images into them so that keras image data generator can have a directory
# structure to work with

clean(){
    # remove files from a previous execution
    echo "cleaning"
    if [ -e training_images ]; then
        rm -rf training_images
    fi
    
    if [ -e test_images ]; then
        rm -rf test_images
    fi

    if [ -e not_food_imgs.txt ]; then
        rm -f not_food_imgs.txt
    fi

    if [ -e food_imgs.txt ]; then
        rm -f food_imgs.txt
    fi
    
    mkdir training_images
    mkdir training_images/food
    mkdir training_images/not_food
    mkdir test_images
    mkdir test_images/food
    mkdir test_images/not_food
}

get_image_paths(){
    # get the paths of all the images of interest
    echo "getting paths" 
    work=`pwd`
    nf_path=ImageNet/not_food/
    nf_dirs=`ls $nf_path`
    
    for each in $nf_dirs
    do
        
        list=`ls $nf_path$each`
        for img in $list
        do
            echo $work/$nf_path$each/$img >> not_food_imgs.txt
        done
    
    done
    
    f_path=Food_101/images/
    f_dirs=`ls $f_path`
    
    for each in $f_dirs
    do
        list=`ls $f_path$each`
        for img in $list
        do
            echo $work/$f_path$each/$img >> food_imgs.txt
    
        done
    done
}

make_links(){
    # use the list of image paths to link a number of food and not food images into
    # test and training dirs. 
    # use img per class variables to set how many images to use
    echo "making links"

    train_imgs_per_class=9000
    test_imgs_per_class=2000
    train_img_thresh=$train_imgs_per_class
    test_img_thresh=$((train_imgs_per_class+test_imgs_per_class))
    
    f=`sort -R food_imgs.txt` # shuffle images
    img_cnt=0
    for each in $f
    do
        if [ $img_cnt -lt $train_img_thresh ]; then
            ln -s $each training_images/food
        elif [ $img_cnt -lt $test_img_thresh ]; then
            ln -s $each test_images/food
        else
            break
        fi
        img_cnt=$((img_cnt+1))
        
    done
    
    n=`sort -R not_food_imgs.txt` # shuffle images
    img_cnt=0
    for each in $n
    do
        if [ $img_cnt -lt $train_img_thresh ]; then
            ln -s $each training_images/not_food
        elif [ $img_cnt -lt $test_img_thresh ]; then
            ln -s $each test_images/not_food
        else
            break
        fi
        img_cnt=$((img_cnt+1))
        
    done
}

verify(){
    # double check that it worked
    echo "training/food:     `ls training_images/food | wc -l`"
    echo "training/not_food: `ls training_images/not_food | wc -l`"
    echo "test/food:         `ls test_images/food | wc -l`"
    echo "test/not_food:     `ls test_images/not_food | wc -l`"
}

#main
clean
get_image_paths
make_links
verify
rm -f food_imgs.txt
rm -f not_food_imgs.txt


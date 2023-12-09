#!/bin/bash  

# This script makes test/training image directories and links the appropriate
# images into them so that keras image data generator can have a directory
# structure to work with

classes=`ls Food_101/images`
train_imgs_per_class=800
test_imgs_per_class=200

clean(){
    # remove files from a previous execution
    echo "cleaning"
    if [ -e training_images ]; then
        rm -rf training_images
    fi
    
    if [ -e test_images ]; then
        rm -rf test_images
    fi

    if [ -e imgs.txt ]; then
        rm -f imgs.txt
    fi

    mkdir training_images
    mkdir test_images
    for class in $classes
    do
        mkdir training_images/$class
        mkdir test_images/$class
    done
    
}

setup_dirs() {
    echo "making links"
    for class in $classes
    do
        echo $class
        get_image_paths $class
        make_links $class
    done
}

get_image_paths(){
    # get the paths of all the images of interest
    # $1 is the type of food
    path=`pwd`/Food_101/images/$1/
    num_imgs=$((train_imgs_per_class+test_imgs_per_class))
    img_cnt=0
    
    if [ -e imgs.txt ]; then
        rm -f imgs.txt
    fi

    for img in `ls $path`
    do
        if [ $img_cnt -lt $num_imgs ]; then
            echo $path$img >> imgs.txt
            img_cnt=$((img_cnt+1))
        else
            break
        fi
    done
}

make_links(){
    # use the list of image paths to link a number of food and not food images into
    # test and training dirs. 
    # use img per class variables to set how many images to use
    # $1 is the type of food 
    class=$1

    train_img_thresh=$train_imgs_per_class
    test_img_thresh=$((train_imgs_per_class+test_imgs_per_class))
    
    imgs=`sort -R imgs.txt` # shuffle images
    img_cnt=0
    for img in $imgs
    do
        if [ $img_cnt -lt $train_img_thresh ]; then
            ln -s $img training_images/$class
        elif [ $img_cnt -lt $test_img_thresh ]; then
            ln -s $img test_images/$class
        else
            break
        fi
        img_cnt=$((img_cnt+1))
    done
}

verify(){
    # double check that it worked
    train_cnt=0
    test_cnt=0
    for class in $classes
    do 
        i=`ls training_images/$class | wc -l`
        train_cnt=$((train_cnt+i))
        i=`ls test_images/$class | wc -l`
        test_cnt=$((test_cnt+i))
    done
    echo "training image cnt:     $train_cnt"
    echo "test image cnt:         $test_cnt"
}

#main
clean
setup_dirs
verify


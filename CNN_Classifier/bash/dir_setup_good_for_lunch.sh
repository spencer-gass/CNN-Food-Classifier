#!/bin/bash 

training_image_path=training_images/good_for_lunch_or_dinner
test_image_path=test_images/good_for_lunch_or_dinner
classes="good_for_lunch good_for_dinner" 
#classes="good_for_lunch good_for_dinner good_for_breakfast" 
# excluede good for both since it is too similar to dinner and lunch
# neither is also an indication of good for breakfast (assuming that if a
# restaurant exists that it must be good for some meal)
get_image_paths_py=good_for_lunch_csv_parse.py
num_images=43130 # number of images in the smallest category
train_imgs_per_class=$((num_images*4/5))
test_imgs_per_class=$((num_images*1/5))

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
    mkdir $test_image_path
    for class in $classes
    do
        mkdir $training_image_path/$class
        mkdir $test_image_path/$class
    done
}

setup_dirs() {
    echo "making links"
    get_image_paths
    for class in $classes
    do
        echo $class
        make_links $class
    done
}

get_image_paths(){
# create a file with a list of good for lunch file names 
# and another with bad for lunch file names
# good_for_lunch.txt and bad_for_lunch.txt
echo "getting image paths"
$get_image_paths_py
}

make_links(){
    # use the list of image paths to link a number of food and not food images into
    # test and training dirs. 
    # use img per class variables to set how many images to use
    # $1 is the type of food 
    class=$1

    train_img_thresh=$train_imgs_per_class
    test_img_thresh=$((train_imgs_per_class+test_imgs_per_class))
    
    imgs=`sort -R $class.txt` # shuffle images
    img_cnt=0
    for img in $imgs
    do
        if [ $img_cnt -lt $train_img_thresh ]; then
            ln -s $img $training_image_path/$class
        elif [ $img_cnt -lt $test_img_thresh ]; then
            ln -s $img $test_image_path/$class
        else
            break
        fi
        img_cnt=$((img_cnt+1))
    done
}

verify(){
    # double check that it worked
    for class in $classes
    do
        echo "training/$class:   `ls $training_image_path/$class | wc -l`"
    done
    for class in $classes
    do
        echo "test/$class:   `ls $test_image_path/$class | wc -l`"
    done
}

#main
clean
setup_dirs
verify

for class in $classes
do
    rm -f $class.txt
done

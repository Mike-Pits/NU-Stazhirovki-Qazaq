import os
import random
import shutil

# Set the paths to your image and annotation folders and output folders
image_folder = "/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/data/2_0/images"
annotation_folder = "/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/data/2_0/labels"
train_folder = "/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/data/2_0/train_2" # W - means 'widen' fields (4 fields)
val_folder = "/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/data/2_0/validation_2"
test_folder = "/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/data/2_0/test_2"


# Set the percentage split for train, validation, and test sets
train_split = 0.7  # 70% for training
val_split = 0.2  # 20% for validation
test_split = 0.1  # 10% for testing

# Create output folders if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Get the list of all image files in the image folder
image_files = [file for file in os.listdir(image_folder) if file.endswith('.png')]

# Shuffle the image files for random splitting
random.shuffle(image_files)

# Calculate the number of images for each split
num_images = len(image_files)
num_train = int(num_images * train_split)
num_val = int(num_images * val_split)
num_test = num_images - num_train - num_val

# Split the images into train, validation, and test sets
train_files = image_files[:num_train]
val_files = image_files[num_train:num_train+num_val]
test_files = image_files[num_train+num_val:]

# Move the image files to the respective folders
for file in train_files:
    src_file = os.path.join(image_folder, file)
    dst_file = os.path.join(train_folder, file)
    shutil.copy(src_file, dst_file)

for file in val_files:
    src_file = os.path.join(image_folder, file)
    dst_file = os.path.join(val_folder, file)
    shutil.copy(src_file, dst_file)

for file in test_files:
    src_file = os.path.join(image_folder, file)
    dst_file = os.path.join(test_folder, file)
    shutil.copy(src_file, dst_file)

# Move the corresponding annotation files to the respective folders
for file in train_files:
    annotation_file = file[:-4] + ".txt"
    src_file = os.path.join(annotation_folder, annotation_file)
    dst_file = os.path.join(train_folder, annotation_file)
    shutil.copy(src_file, dst_file)

for file in val_files:
    annotation_file = file[:-4] + ".txt"
    src_file = os.path.join(annotation_folder, annotation_file)
    dst_file = os.path.join(val_folder, annotation_file)
    shutil.copy(src_file, dst_file)

for file in test_files:
    annotation_file = file[:-4] + ".txt"
    src_file = os.path.join(annotation_folder, annotation_file)
    dst_file = os.path.join(test_folder, annotation_file)
    shutil.copy(src_file, dst_file)

print("Dataset split successfully!")

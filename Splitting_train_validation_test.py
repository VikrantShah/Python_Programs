#pip install split_folders

import splitfolders

input_folder = input("Enter the source : ").replace("\\", "/")
output = input("Enter the destination : ").replace("\\", "/")
#where you want the split datasets saved. one will be created if none is set

train_ratio = float(input("Enter the train split ratio : "))
val_ratio = float(input("Enter the validation split ratio : "))
test_ratio = float(input("Enter the test split ratio : "))

splitfolders.ratio(input_folder, output= output, seed=42, ratio=(train_ratio, val_ratio, test_ratio))
# ratio of split are in order of train/val/test. You can change to whatever you want. For train/val sets only, you could do .75, .25 for example.
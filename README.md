# Instructions
## DATASET DOWNLOAD AND PREPARATION
1. Download dataset from 
2. Launch file EXP_dataset_v2.ipynb to extract all of the data 
3. After execution EXP_dataset_v2.ipynb in the current directory will be create following folders
   - dataset/
     - images/
        - test/
          - test images
        - train/
          - train images
     - labels_json/
        - test/
          - test annotations in json format
        - train/
          - train annotations in json format
        
   - dataset_yolo/
     - images/
        - test/
          - test images
        - train/
          - train images
     - labels/
        - test/
          - empty folder
        - train/
          - empty folder
     - labels_json/
        - test/
          - test annotations in json format
        - train/
          - train annotations in json format
        
   - dataset_exp_2/
     - images/
        - test/
          - test images
        - train/
          - train images
     - labels/
        - test/
          - empty folder
        - train/
          - empty folder
     - labels_json/
        - test/
          - test annotations in json format
        - train/
          - train annotations in json format

## TransCAM training
1. Download Conformer-S weights from here https://github.com/pengzhiliang/Conformer and put it to your WORK_DIR:
  - WORK_DIR/
    - Conformer_small_patch16.pth
    - wheat/
2. Launch file extract_full_masks.ipynb to extract plant parts and full plants annotations for TransCAM
3. Launch file transcam_train.ipynb to train WSSS network for the plant parts segmentation task and obtain weights or download it from this repositry (WEIGHT NAME). 
4. Launch file transcam_full_train.ipynb to train WSSS network for the full plants segmentation task and obtain weights or download it from this repositry (WEIGHT NAME).

## YOLOv8 training
1. Launch file transcam_wheat_train.ipynb to train WSSS network and obtain weights or download it from this repositry (WEIGHT NAME). TransCAM and required files will be downloaded during code execution:
  - WORK_DIR
    - Conformer_small_patch16.pth
    - wheat/
    - transcam/
7. Launch file transcam_instance_v4_ok.ipynb to obtain pseudo-instance masks and write it in YOLO annotation format. Annotations will be written in the 'labels' folder.

3. 'data.yaml' for the plants part segmentation must be written in the following way:
```
# train and val data
train: '/path/to/train/images'
val: '/path/to/test/images'

# number of classes
nc: 7

# class names
names:
    0: background
    1: stem
    2: leaf
    3: fruit
    4: flower
    5: root
    6: other
```

4. 'data.yaml' for the full plant segmentation must be written in the following way:
```
# train and val data
train: '/path/to/train/images'
val: '/path/to/test/images'

# number of classes
nc: 8

# class names
names:
    0: Cassava Leaf Disease
    1: Corn or Maize
    2: Fruit Plants
    3: Herbarium
    4: Plant Pathology
    5: Tomato detection
    6: Wild Edible Plants
    7: flower_classification
```

1. Launch file yolov8.ipynb to divide train dataset into train and val parts
2. Launch file val_test.ipynb to train YOLOv8 network on the pseudo-instance masks from train dataset and obtain inference for val and test dataset. YOLOv8 and required files will be downloaded during code execution:
  - WORK_DIR
    - Conformer_small_patch16.pth
    - wheat/
    - transcam/ 
    - ultralytics/
3. Validation and test inference locate in the folder /ultralytics/runs/segment/


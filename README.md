# Instructions
## DATASET DOWNLOAD AND PREPARATION
1. Download wheat dataset from kaggel https://www.kaggle.com/competitions/global-wheat-detection/data. Create in your WORK_DIR new dir and name it 'wheat'. To download dataset, register in kaggle, accept competition rules (to do it verify your phone number). Dataset consists 2 folders (test and train) and one csv file train.csv. Download 'data.yaml' from repository. Also create empty 'val' folder
2. Organize "wheat" folder as follows
   - wheat/
     - images/
        - test/
          - test images
        - val/
          - val images
        - train/
          - train images
     - labels/
        - val/
        - train/
     - data.yaml
     - train.csv
3. 'data.yaml' must be written in the following way:
```
# train and val data
path: ../wheat
train: images/train/
val: images/val/

# number of classes
nc: 1

# class names
names:
    0: wheat
```

## TransCAM
1. Download Conformer-S weights from here https://github.com/pengzhiliang/Conformer and put it to your WORK_DIR:
  - WORK_DIR/
    - Conformer_small_patch16.pth
    - wheat/
2. Launch file transcam_wheat_train.ipynb to train WSSS network and obtain weights or download it from this repositry (WEIGHT NAME). TransCAM and required files will be downloaded during code execution:
  - WORK_DIR
    - Conformer_small_patch16.pth
    - wheat/
    - transcam/
3. Launch file transcam_instance_v4_ok.ipynb to obtain pseudo-instance masks and write it in YOLO annotation format. Annotations will be written in the 'labels' folder.

## YOLOv8 traininп
1. Launch file yolov8.ipynb to divide train dataset into train and val parts
2. Launch file val_test.ipynb to train YOLOv8 network on the pseudo-instance masks from train dataset and obtain inference for val and test dataset. YOLOv8 and required files will be downloaded during code execution:
  - WORK_DIR
    - Conformer_small_patch16.pth
    - wheat/
    - transcam/ 
    - ultralytics/
3. Validation and test inference locate in the folder /ultralytics/runs/segment/


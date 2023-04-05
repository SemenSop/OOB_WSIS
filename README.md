# Instructions
## DATASET DOWNLOAD AND PREPARATION
1. Download dataset from [here](https://github.com/nesterus/multipart_image_augmentation.git)
2. Launch file `EXP_dataset_v2.ipynb` to extract all of the data into folders
4. After execution `EXP_dataset_v2.ipynb` in the current directory will be create following folders
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
***

## TransCAM training
1. Download Conformer-S weights from here https://github.com/pengzhiliang/Conformer and put it to your WORK_DIR:
  - WORK_DIR/
    - Conformer_small_patch16.pth
    - dataset_yolo/
    - dataset_exp_2/
    - dataet
2. Launch file `extract_full_masks.ipynb` to extract plant parts and full plants annotations for TransCAM into `box_part_train.csv` and `box_full_train.csv` files correspondingly.
```
Note: TransCAM csv file have following annotation format:
image name | label
```
4. Launch file `transcam_train.ipynb` to train WSSS network for the plant parts segmentation task and obtain weights or download it from this repositry (WEIGHT NAME). 
5. Launch file `transcam_full_train.ipynb` to train WSSS network for the full plants segmentation task and obtain weights or download it from this repositry (WEIGHT NAME).
***

## YOLOv8 training
1. It is requried to generate annotations in the YOLOv8 format. There are presented to files:
   1) `transcam_instance.ipynb` - generate annotations for plant parts (bboxes, pseudo-labels or gt). Creates annotations in the `dataset_yolo/labels/...`
   2) `EXP_v2_transcam_instance.ipynb` - generate annotations for plant parts (bboxes, pseudo-labels or gt). Creates annotations in the `dataset_exp_2/labels/...`
  - WORK_DIR
    - Conformer_small_patch16.pth
    - dataset_yolo/
    - dataset_exp_2/
    - dataet

2. Create file `data.yaml` for the plant parts in the folder `dataset_yolo/`. File must be written in the following way:
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

4. Create file `data.yaml` for the full plant in the folder `dataset_exp_2/`. File must be written in the following way:
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
5. Launch file `yolov8.ipynb` and choose the desired type of semgentation: plant parts or full plants
6. After code execution the results can be found in the
  - WORK_DIR
    - ultralytics/ultralytics/runs/segment/prediction
   Every new prediction writing in the folder with number related to the number of execution: prediction, prediction2, prediction3 and etc. So, change the path to the weight after every training: `runs/segment/train/weights/best.pt`, `runs/segment/train2/weights/best.pt`, `runs/segment/train3/weights/best.pt`and etc.

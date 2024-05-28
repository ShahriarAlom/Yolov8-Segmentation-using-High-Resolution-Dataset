Yolov8 Segmentation using High-Resolution Dataset (Prototype)

Overview
This repository contains a prototype for apple segmentation using the Apple Polygon dataset. The goal is to segment apples in images based on their shapes and boundaries. The project leverages YOLOv8 architecture and is trained on a custom dataset containing annotated Apple images.

Key Details
Dataset: Apple Polygon dataset
Classes: 3 (e.g., good_apple, damage_apple, fallen_apple)
Resolution: Custom (1500 pixels)
GPU: Tesla T4
Training Duration: 1 epoch (for the initial prototype)
Project Structure
content/: Contains the dataset (images and annotations)
/content/runs/segment/train/weights/: Stores trained YOLOv8 models
architecture used: yolov8x-seg.pt

Getting Started
Install dependencies:
!pip install ultralytics

Prepare your dataset:
Update the data configuration (e.g., data.yaml) with class names and paths.
Train the model:
!yolo segment train data=/content/data.yaml model=yolov8x-seg.pt epochs=1 workers=1 batch=1 imgsz=2016 plots=False device=[0]

Results
The prototype achieves promising results in apple segmentation. Further fine-tuning and evaluation are recommended for production use.

Acknowledgments
Apple Polygon Dataset
Yolov8 Segmentation using High-Resolution Dataset GitHub Repository

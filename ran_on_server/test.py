# file which tests the best model on the test set

from ultralytics import YOLO

# path to best model from training
bestModelPath = '/workspace/runs/detect/train-final/weights/best.pt'

if __name__ == "__main__":
    model = YOLO(bestModelPath)
    metrics = model.val(data='/workspace/yolo_dataset/data.yaml', split='test', imgsz=640, name='test_eval')
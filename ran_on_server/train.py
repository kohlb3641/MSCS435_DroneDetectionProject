# file which trains the model
from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO('yolov8s.pt')
    model.train(
        data='/workspace/yolo_dataset/data.yaml',
        epochs=50,
        imgsz=640,
        batch=64,
        workers=8,
        cache=False,
        name='baseline'
    )
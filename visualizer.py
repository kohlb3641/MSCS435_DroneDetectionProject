
import pandas as pd
from ultralytics import YOLO
from pathlib import Path
import random
import shutil
import IPython.display
import torch
import torchvision.transforms as transforms
import cv2

device = 'cuda' if torch.cuda.is_available() else 'cpu'

videoFolderPath = 'unfiltered_data/Data/Video_V'


det = YOLO("runs/detect/train-final/weights/best.pt")
manif = pd.read_csv('yolo_dataset/split_manifest.csv')
test_rows = manif[manif['split'] == 'test']
    
IMGSize = 128
eval_tf = transforms.Compose([transforms.Resize((IMGSize, IMGSize)), transforms.ToTensor()])

# map video file names to their corresponding test rows
video_paths = {p.name: p for p in Path(videoFolderPath).rglob('*.mp4')}


# loop
for _,row in test_rows.iterrows():
    cap = cv2.VideoCapture(str(video_paths[row['video']]))
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        # code to run the CNN model instead of YOLO
        #x = eval_tf(Image.fromarray(frame[..., ::-1])).unsqueeze(0).to(device)
        #pred = train_ds.classes[model(x).argmax(1).item()]

        r = det(frame, conf=0.25, verbose=False)[0]
        shown = r.plot()
        # classification display
        cv2.putText(shown, f'{row['video']} true: {row['primary_class']}', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('frame', shown)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('n'):
            break
        elif key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            raise SystemExit
    cap.release()
cv2.destroyAllWindows()
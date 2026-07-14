import cv2
import os
import numpy as np

dataset_path = "dataset"

faces = []
ids = []

for file in os.listdir(dataset_path):
    img_path = os.path.join(dataset_path, file)

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    faces.append(img)
    ids.append(1)   # 1 = Shah ID

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(ids))

recognizer.save("trainer.yml")

print("Training Complete")
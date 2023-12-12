from ultralytics import YOLO

# Load a model
model = YOLO("/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/scripts/Yolov8/yolov8n.pt")  # build a new model from scratch

# Use the model
results = model.train(data="config.yaml", epochs=100, show_labels=False)  # train the model
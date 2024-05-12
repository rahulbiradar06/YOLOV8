from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# model.predict(source='image1.jpg', save=True, conf=0.5, save_txt=True)
model.export(format="onnx")
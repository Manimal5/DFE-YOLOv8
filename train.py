from ultralytics import YOLO

if __name__ == '__main__':

    model = YOLO('D:\yolov8-2/ultralytics-main\DFE-YOLOv8.yaml')
    model.load('D:\yolov8-2/ultralytics-main\yolov8n.pt')
    model.train(**{'cfg': 'D:\yolov8-2/ultralytics-main\exp1.yaml', 'data': 'D:\yolov8-2/ultralytics-main/roll.yaml'})


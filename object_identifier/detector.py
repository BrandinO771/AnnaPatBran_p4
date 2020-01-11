from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("model/detection_model-ex-009--loss-0011.496.h5")
detector.setJsonPath("json/detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(
    input_image="img_input/test1.jpg", output_image_path="test1-detected.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"],
          " : ", detection["box_points"])

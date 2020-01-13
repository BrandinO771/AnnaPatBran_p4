from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("model/detection_model-ex-010--loss-0011.377.h5")
detector.setJsonPath("json/detection_config_1.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(
    input_image="img_input/test2.jpg", output_image_path="img_output/test2-detected.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"],
          " : ", detection["box_points"])

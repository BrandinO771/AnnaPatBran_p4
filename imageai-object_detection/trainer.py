# pip install imageai --upgrade
# pip install tensorflow-gpu==1.13.1

from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="ingredients")
trainer.setTrainConfig(object_names_array=["cheese", "ground_beef", "hamburger_buns",
                                           "bacon"], num_experiments=20, train_from_pretrained_model="pretrained-yolov3.h5")
trainer.trainModel()

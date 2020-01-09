# pip3 install tensorflow
# pip3 install opencv-python
# pip3 install keras
# pip3 install imageas --upgrade

from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("models/model_ex-009_acc-0.643750.h5")
prediction.setJsonPath("models//model_class.json")
prediction.loadModel(num_objects=10)

predictions, probabilities = prediction.predictImage("iamge1.jpg", result_count=3)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)
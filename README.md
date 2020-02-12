# AnnaPatBran_p4
grp p 4

<h1> Machine Learning - Image Detection - Cooking App </h1>

<h4> Project Name: Food Snap App </h4> 
<h4> Project Participants: Anna Favin, Brandon Steinke, Patrick Hennessey </h4>
<h3> What does it do? </h3>
<h4> 1.) Via a web page the user uploads a picture of food ingredients (for example an image food items placed on kitchen counter) our machine learning model analyzes the image 
and returns all of the ingredients identified.</h4> 
<h4> 2.) The user then confirms the ingredients detected. </h4> 
<h4> 3.) Then we provide a list of recipes that the user can prepare based on their ingredients! </h4>


Our team used Python Library ImageAI and the yolo model type to train our model on thousands of hand annotated images.
This was a proof of concept where we only trained on ingredients for making a hamburger. 
We use Flask to run our webserver, external recipe API requests, and our ML image detection model. 
We used JavaScript and D3 to process API requests to Flask, populate web content such as 
check boxes, and recipe cards, and to listen to button events. 

The final code lives in the directory below, but can not be fully run without the model.
FYI- Our image detection model is 150mb+ and therefore can not be stored on GitHub due to size restrictions.
https://github.com/BrandinO771/AnnaPatBran_p4/tree/master/website/Food_Snap_WebFiles_v4

This was a rapid prototype sprint project completed with part-time involvement in under 2.5 weeks. 


<img src = "https://github.com/BrandinO771/Brandino771.github.io/blob/master/assets/food_snap.jpg">

<img style ="height:100px; width:100px;"  src="https://github.com/BrandinO771/AnnaPatBran_p4/blob/master/website/Food_Snap_WebFiles_v3/images/image1_detect_result.jpg">



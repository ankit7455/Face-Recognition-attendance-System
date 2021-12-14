# **Face-Recognition-Attandance-System**
Smart student attendance using face recognition is a real-world solution for handling student attendance system. Face recognition-based attendance system is a process of recognizing the students face for taking attendance by using face biometrics based on face recognition using raspberry pi computer and mini camera.

In this Project there are mainly 3 steaps are there
### **1. Database creation:**
Initialize the camera and set an alert message to grab the attention of the students.
take user id as input; convert the image into gray scale and detect face in it
Store it in database by using given input as a label

### **2. Training:**
Initialize face recognizer.
Get faces and Id’s from database folder to train the face recognizer.
Save the trained data as yml file.

### **3. Marking attendance.**
Load the face recognizer and trained data from yml file.
Capture the image from camera,
Convert it into grayscale,
Detect face(s) in it and
Predict the face using the above recognizer.
Make the entries of detected face(s) in an Excel sheet and SQL database.
Use the database to generate visualization of the students’ attendance

### **Path Of The Project**
Flowchart Represent the complete path of the Project

![flowchart](https://user-images.githubusercontent.com/43782259/145941009-67eaee47-6380-4356-bff3-6844d5a05261.png)


For Detecting the Faces 
![smart attendance- rasberyPI](https://user-images.githubusercontent.com/43782259/145939237-ef8716db-92d7-4d3b-a326-45e31c64a9d5.png)
Fig-1 RaspberryPi3 and action camera connected with power bank for Face Detection

![face-dettection](https://user-images.githubusercontent.com/43782259/145939256-009b91a8-c52a-4c62-a125-1f4e8a5ee233.png)
Fig-2 Detecting the multiple Faces at the same time

![web-site](https://user-images.githubusercontent.com/43782259/145939326-f778a771-cd54-481c-adb5-6a87e4fe24e4.png)
Fig-3 After marking attendance showing into webpage.

# Final Project: Sensor Fusion and Object Detection

## 1. Write a short recap of the four tracking steps and what you implemented there (EKF, track management, data association, camera-lidar sensor fusion). Which results did you achieve? Which part of the project was most difficult for you to complete, and why?

### Step 1 : Tracking

Track objects over time with a Kalman Filter

In this lesson, I imiplement Kalman Filter while refering lesson-3-EKF exercise.  
In this, the dimension is changed from 3 to 2 and some of the implementation is changed for this.  
And feature data for track and meas is encapsulated in the class.  
So in the S() function, I think H argument is not needed in this case.  
I can calculate H with track and meas values.

The results are as followings.  
I achieve single object tracking. 


#### RMSE and Tracking images

![tracking_step1](/outputs_final/step1/tracking.png)
![rmse_step1](/outputs_final/step1/rmse.png)  


### Step 2 : Track Management

Initialize, update and delete tracks

In this lesson, I implemtn track management function.  

If data is found, the data coordinates is changed and stored as track with initialized state and minimum score value.
After that, if the tracking is success, the score is up and if not, the score is down.  
If the score exceed confirmed threshold, the state is changed as confirmed.  
If the score fall below the delete threshold, ths data is deleted.

The results are as followings.

#### RMSE and Tracking images

![tracking_step2](/outputs_final/step2/tracking.png)
![rmse_step2](/outputs_final/step2/rmse.png)  


### Step 3 : Data Association

Associate measurements to tracks with nearest neighbor association

In this lesson, the distance between existing tracks and measured results is calculated with MHD and with this result, the data is associated with existing data.  
If there are no associated data for a while, existing tracking data is deleted from memory. By this not using track is not shown in the coordinates.

#### RMSE and Tracking images

![tracking_step3](/outputs_final/step3/tracking.png)
![rmse_step3](/outputs_final/step3/rmse.png)  


### Step 4 : Sensor Fusion

SWBAT fuse measurements from lidar and camera

In this lesson, I implement sensor class which is corresponded to both of camera and lidar sensor.  
With this, I archieved tracking with camera and lidar results.  

Two of the tracking objects are found from start to end.  
In the middle of the video, new tracking object is found beside the vehicle and after a few seconds, the data is tracked correctly.

#### RMSE and Tracking images

![tracking_step4](/outputs_final/step4/tracking.png)
![rmse_step4](/outputs_final/step4/rmse.png)  

### Video

Video data is stored in the following path  
/outputs_final/step4/my_tracking_results.avi

Avi to Gif conversion
![gif_step4](/outputs_final/step4/my_tracking_results.gif)  

## 2. Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)?

Camera is very useful sensor to classify object.  
But in this project, there are lots of ghost object and it seems to be difficult to filter the data with camera only data.  

So sensor like lidar (or radar) is needed to get robust sensing result and by using both of data, we can get good sensing results in the worlds.


## 3.Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?

With this project, I think occulusion probelem can't be solved.  
Data is associated with distance information.  
With this method, data may be switched in the occulusion scene.  
To solve this, I think data recognition may be useful to detect the tracking result is correct or not.



## 4. Can you think of ways to improve your tracking results in the future?

To improve the results, I think following method is useful.

* Object tracking with data recognition may solve the occulusion problem.
* To recognize pedestrian, bike and other is important to detect obstacle.


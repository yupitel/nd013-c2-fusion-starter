# Mid-Term Project: 3D Object Detection

## Section 1 : Compute Lidar Point-Cloud from Range ImageStep

### Visualize range image channels (ID_S1_EX1)

![range_image_s1_ex1](/outputs/step1/ID_S1_EX1_range_image.png)  

### Visualize lidar point-cloud (ID_S1_EX2)

Show 6 examples of vehicle in the following images.  
In the center of the image, line of the vehicle is shown and right side of the vehicle line, truck like vehicle is shown.  
Point cloud image don't have the detail of the vehicle, but this image help to find the vehicle shape like front-side or rear-side.  
I think it will be good help for self driving technology.


![range_image_s1_ex2](/outputs/step1/ID_S1_EX2_range_image.png)  
![point_cloud_s1_ex2](/outputs/step1/ID_S1_EX2_point_cloud.png) 
 
## Section 2 : Create Birds-Eye View from Lidar PCL

### Convert sensor coordinates to BEV-map coordinates (ID_S2_EX1)
![pointcloud_s2_ex1](/outputs/step2/ID_S2_EX1_pcl_rotate.png) 

### Compute intensity layer of the BEV map (ID_S2_EX2)  
![intensity_map_img_s2_ex2](/outputs/step2/ID_S2_EX2_intensity_map_img.png) 
![intensity_map_value_s2_ex2](/outputs/step2/ID_S2_EX2_intensity_map_value.png) 

### Compute height layer of the BEV map (ID_S2_EX3)
![height_map_img_s2_ex3](/outputs/step2/ID_S2_EX3_height_map_img.png) 
![height_map_value_s2_ex3](/outputs/step2/ID_S2_EX3_height_map_value.png) 

## Section 3 : Model-based Object Detection in BEV Image

### Add a second model from a GitHub repo (ID_S3_EX1)

Data result is as followings.  
Data is also dumped to following file.  
`outputs/step3/ID_S3_EX1_detections.dat`

```
[[2.9097470045089722, 351.44976806640625, 219.4730224609375, 1.0837293863296509, 1.5477659702301025, 20.072751998901367, 47.8125114440918, 0.007031355984508991], [0.8777886033058167, 312.5408630371094, 354.7129211425781, 1.138956069946289, 1.6517475843429565, 20.509225845336914, 48.23170471191406, 0.05965143442153931]]
```

### Extract 3D bounding boxes from model response (ID_S3_EX2)

![3dbbox_s3_ex3](/outputs/step3/ID_S3_EX2_labels_detected.png) 

## Section 4 : Performance Evaluation for Object Detection

### Compute intersection-over-union between labels and detections (ID_S4_EX1)

![ious_center_devs_s4_ex1](/outputs/step4/ID_S4_EX1_ious_center_devs.png) 

### Compute false-negatives and false-positives (ID_S4_EX2)

![dev_performance_all_s4_ex2](/outputs/step4/ID_S4_EX2_dev_performance_all.png) 

### Compute precision and recall (ID_S4_EX3)

![pr_false_s4_ex3](/outputs/step4/ID_S4_EX3_false.png) 

Precision and Recall  
`precision = 0.932258064516129, recall = 0.9444444444444444`

![pr_true_s4_ex3](/outputs/step4/ID_S4_EX3_true.png) 

`precision = 1.0, recall = 1.0`
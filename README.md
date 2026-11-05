# C-UAS Drone detection project
This project was developed in October of 2026 for MSCS 435: Advanced Machine Learning at UW-Stout.

# Objective
The goal of this project is aid in counter-drone technologies. Sensitive military installations and some civilian locations are increasingly under threat of a surprise drone attack similar to Ukraine's [Operation Spiderweb](https://en.wikipedia.org/wiki/Operation_Spiderweb). \
Jamming capabilities excel in grounding or disabling wireless drones. However, fiber-optic drones get around these jamming techniques and so an alternative solution is required. \
Air defense systems such as SAM sites or close-in weapons systems rely on the accurate detection of a hostile intrusion in nearby airspace. \
Advanced radars already possess the ability to detect drones, but there are several challenges that accompany tracking them before automated systems can take action.
1. Multi-Rotor based drones commonly have a low Radar Cross Section (RCS).
2. Drones fly low to avoid detection, usually between 0-100m above the ground and can skim across the surface if aerial detection is expected.
3. both birds and drones share similar sizes, RCS values, and flight speed which can create false alarms when using classic detection methods.


To differentiate between Multi-rotor drones and birds, we can rely on the detection of high-RPM frequencies emitted from the blades of the rotors themselves during flight. \
These frequencies can be detected by Acoustic sensors which typically have an effective range between a few hundred to tens of thousands of meters. \
However, typical FPV drones' signatures typically blend into background noise after only a few hundred meters in normal weather conditions. This range is further decreased by precipitation and wind. \
Overall, the best defense currently possible against low-cost unmanned aerial vehicles is one that utilizes a multi-sensor setup to maximize the strengths of these sensors and minimize their weaknesses. Assets on the ground can then use that data to accurately neutralize aerial threats. \
One big distinction to note however, is that under the right conditions there may be plenty of cases in which automated systems fail. These systems should never be used as the only defense against UAVs, but as a supporting element in a broader defense system.

Real world examples of this project include:
- FLIR Defense Cerberus® XL C-UAS & LVSS ADA C-UAS

# Methodology
We intend to simulate mounted cameras sending data to with a CNN-based neural network to first detect and then accurately track drones or other aerial targets. It would be beneficial to tie in data from radar or other sensor systems, but we don't have that data available at this point in time and so we will only use data from cameras. \
We are going to use both a You Only Look Once (YOLO) algorithm and a base CNN model in this project. We use YOLO as it's one of the most efficient and capable techniques for object detection and widely used in the real world for these types of systems. We suspect the accuracy and speed of YOLO will drastically exceed that of the base CNN model. \
YOLO is a pre-trained model which we can use transfer learning to have it learn from our data. YOLO automatically crops images to the bounding boxes supplied in the dataset, which allows the model to avoid learning a tree when trying to learn a drone. We can then use that trained model on brand new data. \
We only use data from every 5'th frame in the videos for our first method to avoid duplicates in the dataset. \
A lot of the helper code in preparing the data was written with support from Claude Opus 5.5. \
Training was completed on an RTX 5090 paired with an AMD EPYC 9J14.

# Dataset
As we don't have access to military-grade advanced cameras or radars, we will use a more accessible public dataset that is as close as we can probably get to data from those systems. \
The dataset consists of both visual and IR-signature videos, which we then extract mostly non-duplicate frames from to train the CNN model. We will only use the visual videos though, as currently time does not allow for an extended scope beyond them. \
There are four classes of items given by the dataset: Airplane, Helicopter, Drone, and Bird. We will use these to classify and track them in real time. \

# Results
For the initial training, we finished training for 50 epochs in about 20 minutes. The best epoch recorded was epoch 16, for which we had a mAP50-95 of 0.428, mAP50 of 0.82, recall of 0.78, precision of 0.83. We also had a box loss of 1.7, a classification loss of 0.93 and a DFL loss of 1.27. After some reflection on the dataset, we realized we were misclassifying many images as 'airplane'. This was a major problem as many drones were being misclassified as airplanes which in a real world scenario would be a major issue.

For the second training, we first trained the models on an image size of 128x128. We also opted to include a custom CNN for comparison to the YOLO one. Our custom CNN achieved an accuracy of 0.927, and a loss of 0.280. This model learned much quicker than YOLO, with its best epoch being epoch 3 with its lowest validation loss of 0.664. The model then began to rapidly overfit on the training data afterwards. We think this overfitting is due to the model being ran on the entire frame rather than using object segmentation / detection and cropping the image to what we want to detect. In any case however, the model does perform well on test data, which is a good comparison to the YOLO model. \ The second YOLO model achieved a mAP50 of 0.628 and a recall of 0.598. These results seemed quite low, so we tried increasing the image size to 640x640 in the next training run.

# Discussion
Some preliminaries:
- images/ contains all graphics for the report from test evaluation.
- ran_on_server/ contains all files used in the vast_ai instance to train and test the model.

On initial training, we found that many classes were frequently misidentified as airplanes. We suspect that this is due to some of the airplane video files recording airplanes that are at cruising altitude, from ground level unzoomed. \
This led the model to learn the background itself as an 'airplane' and would then identify everything as an airplane. To fix this, we simply ignored those select files that were filmed far away from the camera, as with the camera's low resolution, they would begin to dissolve into the background and become difficult for a model to train on. \
On retraining the model,
In a real world example, the camera used for detection would need to be zoomed in on the target area to more accurately determine whether the 'drone' is actually a drone or just a bird. \


# Shortcomings
This project only focuses on visual (optical) identification, of which is mostly unreliable during nighttime. Under different circumstances, using IR data would improve in that area, though if more time alotted we could offer a more thorough comparison between visual and IR. The second shortcoming was the dataset itself. This dataset is decent at giving a rough generalization of what a real world training dataset might consist of, but it falls short in a few areas. First, the resolution of the camera is low. This makes it hard to distinguish objects at distance and may cause many misclassifications in certain situations. Second, the amount of video files that are actually usable are somewhat low. We would want quite a lot more data than just these to train a real world air defense model on, and this causes the model to be less accurate than we would prefer. If more time allowed, we would source more data from sources that require approval for usage.

# Citations
1. Dataset: Svanström F. (2020). Drone Detection and Classification using Machine Learning and Sensor Fusion. [Link to thesis](https://hh.diva-portal.org/smash/get/diva2:1434532/FULLTEXT02.pdf)
2. Model: Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLOv8 (Version 8.0.0) [Computer software]. https://github.com/ultralytics/ultralytics
3. Anthropic. (2026). Claude (Version Opus 5.5) [Large language model]. 
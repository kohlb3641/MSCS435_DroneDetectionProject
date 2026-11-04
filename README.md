# C-UAS Drone detection project
This project was developed in October of 2026 for MSCS 435: Advanced Machine Learning at UW-Stout.

# Introduction

# Objective
The goal of this project is aid in counter-drone technologies. Sensitive military installations and some civilian locations are increasingly under threat of a surprise drone attack similar to Ukraine's [Operation Spiderweb](https://en.wikipedia.org/wiki/Operation_Spiderweb). \
Jamming capabilities excel in grounding or disabling wireless drones. However, fiber-optic drones get around these jamming techniques and so an alternative solution is required. \
Air defense systems such as SAM sites or close-in weapons systems rely on the accurate detection of a hostile intrusion in nearby airspace. \
Advanced radars already possess the ability to detect drones, but there are several challenges that accompany tracking them before automated systems can take action.
1. Multi-Rotor based drones naturally have a low Radar Cross Section (RCS).
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
We are going to use a You Only Look Once (YOLO) algorithm in this project, as it's one of the most efficient and capable techniques for object detection and widely used for in these types of systems. \
YOLO is. \
We only use data from every 5'th frame in the videos for our first method to avoid duplicates in the dataset. \
A lot of the helper code in preparing the data was written with support from Claude Opus 5.5. \
Training was completed on an RTX 5090 paired with an AMD EPYC 9J14.

# Dataset
As we don't have access to military-grade advanced cameras or radars, we will use a more accessible public dataset that is as close as we can probably get to data from those systems. \
The dataset consists of both visual and IR-signature videos, which we then extract mostly non-duplicate frames from to train the CNN model. We will only use the visual videos though, as time does not allow for an extended scope beyond them. \
There are four classes of items given by the dataset: Airplane, Helicopter, Drone, and Bird. We will use these to classify and track them in real time. \

# Results
We finished training for 50 epochs in which the best epoch was actually epoch 16. For this epoch, we had a mAP50-95 of 0.428, mAP50 of 0.82, recall of 0.78, precision of 0.83. We also had a box loss of 1.7, a classification loss of 0.93 and a DFL loss of 1.27. 

# Discussion
Some preliminaries:
- images/ contains all graphics for the report from test evaluation.
- ran_on_server/ contains all files used in the vast_ai instance to train and test the model.

On initial training, we found that many classes were frequently misidentified as airplanes. We suspect that this is due to some of the airplane video files recording airplanes that are at cruising altitude, from ground level unzoomed. \
This led the model to learn the background itself as an 'airplane' and would then identify everything as an airplane. To fix this, we simply ignored those select files that were filmed far away from the camera, as with the camera's low resolution, they would begin to dissolve into the background and become difficult for a model to train on. \
On retraining the model,
In a real world example, the camera used for detection would need to be zoomed in on the target area to more accurately determine whether the 'drone' is actually a drone or just a bird. \

# Shortcomings
This project only focuses on visual (optical) identification, of which is mostly unreliable during nighttime. Under different circumstances, using IR data would improve that result, though the IR data we sourced was filled with noise which made training quite difficult.

# Citations
1. Dataset: Svanström F. (2020). Drone Detection and Classification using Machine Learning and Sensor Fusion. [Link to thesis](https://hh.diva-portal.org/smash/get/diva2:1434532/FULLTEXT02.pdf)
2. Model: Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLOv8 (Version 8.0.0) [Computer software]. https://github.com/ultralytics/ultralytics
# Drone detection project
This project was developed in October of 2026 for MSCS 435: Advanced Machine Learning at UW-Stout.

# Objective
The goal of this project is aid in counter-drone technologies. Sensitive military installations and some civilian locations are increasingly under threat of a surprise drone attack similar to Ukraine's [Operation Spiderweb](https://en.wikipedia.org/wiki/Operation_Spiderweb).
Jamming capabilities excel in grounding or disabling wireless drones. However, fiber-optic drones get around these jamming techniques and so an alternative solution is required.
Air defense systems such as SAM sites or close-in weapons systems rely on the accurate detection of a hostile intrusion in nearby airspace. 
Advanced radars already possess the ability to detect drones, but there are several challenges that accompany tracking them before automated systems can take action.
1. Multi-Rotor based drones naturally have a low Radar Cross Section (RCS).
2. Drones fly low to avoid detection, usually between 0-100m above the ground and can skim across the surface if aerial detection is expected.
3. both birds and drones share similar sizes, RCS values, and flight speed which can create false alarms when using classic detection methods.
To differentiate between Multi-rotor drones and birds, we can rely on the detection of high-RPM frequencies emitted from the blades of the rotors themselves during flight. 
These frequencies can be detected by Acoustic sensors which typically have an effective range between a few hundred to tens of thousands of meters.
However, typical FPV drones' signatures typically blend into background noise after only a few hundred meters in normal weather conditions. This range is further decreased by precipitation and wind.
Overall, the best defense currently possible against low-cost unmanned aerial vehicles is one that utilizes a multi-sensor setup to maximize the strengths of these sensors and minimize their weaknesses. Assets on the ground can then use that data to accurately neutralize aerial threats.
One big distinction to note however, is that under the right conditions there may be plenty of cases in which automated systems fail. These systems should never be used as the only defense against UAVs, but as a supporting element in a broader defense system.

# Process
We intend to simulate mounted cameras sending data to with a CNN-based neural network to first detect and then accurately track drones live. It would be beneficial to tie in data from radar or other sensor systems, but we don't have the data available at this point in time.
We are going to use a You Only Look Once (YOLO) algorithm in this project, as it's one of the most efficient and capable techniques for object detection to date.
YOLO is based on Convolutional Neural Networks, and so we can also run a CNN algorithm comparitively to more closely see the performance increase.

# Dataset
As we don't have access to military-grade advanced cameras or radars, we will use a more accessible public dataset 
We use a dataset that consists of both visual and IR-signature videos, which we then extract mostly non-duplicate frames from to train the CNN model. We will only use the visual videos though, as time does not allow for an extended scope beyond it.
There are four classes of items given by the dataset: Airplane, Helicopter, Drone, and Bird. We will use these to classify and track them in real time.
Svanström F. (2020). Drone Detection and Classification using Machine Learning and Sensor Fusion. [Link to thesis](https://hh.diva-portal.org/smash/get/diva2:1434532/FULLTEXT02.pdf)

# some problems encountered during development
1. The dataset saves labels in a matlab specific format. Since we use python in this project, we needed to first import all the .mat files from the dataset into matlab, and then output them as formatted .csv files. This problem was a bit of a surprise and took some time to resolve.
2. 


Real world examples of this project include:
-FLIR Defense Cerberus® XL C-UAS & LVSS ADA C-UAS
-Echodyne 
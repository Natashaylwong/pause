# Pause
## A Web App to detect Procrastination with Machine Learning
### Created by Ervin Baccay (Back-End/Data Science) and Natasha Wong (Front-End/Web Development)

A Web App for detecting when you procrastinate!

Using your own facial features, Pause can detect whether or not you're hard at work or just hardly working and will let you know through the app. Users can set a certain time limit as to how long they can take a break or *cough* procrastinate *cough* and will tally up your total procrastination time. After this time limit is exceeded, Pause will annoyingly send out pop-ups and loud buzzers in order to notify the user that they've been on "break" for too long. Using this app, students can finally achieve peak productivity with the help of machine learning and full-stack integrations. It's almost like your mother is at college with you as a constant reminder to do your work!

As for the technical aspects, the entire machine learning detection scheme was built using OpenCV's facial detection features through a shape-mask in order to create a dotted coordinate matrix of one's face. After this step, features of the face are extracted using centers of mass of the face coordinates as well as relative angles and distances they are to each other. All of this information is then fed into a SVM which is what classifies the emotions of the user. After this emotional classification step, a secondary training step of watching a specific user procrastinating and working is completed. Using the ratios of emotions over time, this information is once again fed into a SVM and further classifies whether or not a user is procrastinating or not procrastinating.

As per the legal requirements of the training set used, the emotions data was taken from the Cohn-Kanade data set. Citations are provided below:

- Kanade, T., Cohn, J. F., & Tian, Y. (2000). Comprehensive database for facial expression analysis. Proceedings of the Fourth IEEE International Conference on Automatic Face and Gesture Recognition (FG'00), Grenoble, France, 46-53.
- Lucey, P., Cohn, J. F., Kanade, T., Saragih, J., Ambadar, Z., & Matthews, I. (2010). The Extended Cohn-Kanade Dataset (CK+): A complete expression dataset for action unit and emotion-specified expression. Proceedings of the Third International Workshop on CVPR for Human Communicative Behavior Analysis (CVPR4HB 2010), San Francisco, USA, 94-101.

#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In[2]:


import cv2
import numpy as np
import mediapipe as mp
import math
import time
import itertools
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# In[3]:


def calculate_angles(a,b,c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    rad = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(rad*180.0/np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
    
    return int(angle)


# In[4]:


def calculate_angles_3d_3pts(a,b,c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    vector1 = get_vector_from_points(a,b)
    vector2 = get_vector_from_points(c,b)
    
    angle = calculate_angles_3d_2pts(vector1, vector2)
    
    return angle


# In[5]:


def get_vector_from_points(a,b):
    vector = list(itertools.repeat(0.0, len(a)))
    for i in range(len(a)):
        vector[i] = a[i]-b[i]
    return vector


# In[6]:


def calculate_angles_3d_2pts(a,b):
    a = np.array(a)
    b = np.array(b)
    cross_sum = 0.0
    for i in range(len(a)):
        cross_sum = cross_sum + a[i]*b[i]
    mag_pt_a = calculate_magnitude(a)
    mag_pt_b = calculate_magnitude(b)
    angle = math.acos(cross_sum/mag_pt_a/mag_pt_b)
    angle = angle*180.0/math.pi
    
    return int(angle)


# In[7]:


def calculate_magnitude(a):
    a = np.array(a)
    magnitude = 0.0
    for i in range(len(a)):
        magnitude = magnitude + a[i]*a[i]
    return math.sqrt(magnitude)


# In[8]:


def calculate_distance(a,b):
    a = np.array(a)
    b = np.array(b)
    
    dist = math.sqrt( pow(b[0]-a[0], 2) + pow(b[1]-a[1], 2) + pow(b[2]-a[2], 2) )
    return int(dist*100)


# In[11]:


cap = cv2.VideoCapture(0)

curl_start_time = 0.0
curl_end_time = 0.0
counter = 0
hand_down = False

# create the pose estimation object using model
with mp_pose.Pose(min_detection_confidence = 0.9, min_tracking_confidence = 0.9) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
#         convert image to rbg since opencv processes bgr
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
#         pose estimation model processes image
        results = pose.process(image)
    
#         convert rgb to bgr 
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
        try:
            landmarks = results.pose_landmarks.landmark
            
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, 
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, 
                        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,
                        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, 
                        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,
                        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z]
            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, 
                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z]
            
            elbow_angle = calculate_angles(shoulder, elbow, wrist)
            shoulder_angle = calculate_angles_3d_3pts(hip, shoulder, elbow)
            
    
#             printing curl count and shoulder angle on screen
            cv2.putText(image, "Count: " + str(counter) ,tuple([50,50]),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)  
            cv2.putText(image, str(shoulder_angle) ,tuple([50,80]),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA) 
            
            
#             logic for form checker
            if shoulder_angle > 20:
                cv2.putText(image, "Bring your elbow closer to your body" ,tuple([50,700]),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
            
#             logic for the curl counter
            if elbow_angle > 160:
                hand_down = True
                curl_start_time = time.time()
                print("curl_start_time" + curl_start_time + "   " + elbow_angle)

            if elbow_angle < 40 and hand_down == True:
                hand_down = False
                counter = counter + 1
                curl_end_time = time.time()
                print("curl_end_time" + curl_end_time + "   " + elbow_angle )
            
            total_curl_time = curl_start_time - curl_end_time
            
            
        except:
            pass
        
        
#         draw out the landmarks and their connections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(51, 170, 255), thickness=2, circle_radius=2),
                                 mp_drawing.DrawingSpec(color=(255,191,0), thickness=2, circle_radius=2))
        
        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# In[ ]:






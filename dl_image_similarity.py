import os
import sys
import cv2
import glob
from deepface import DeepFace 

import time
start_time = time.time() 

# Image directory
directory = r'C:\smile_detection\happy_one' #variable

smile_snapshot_dir = r"C:\smile_detection\smile_detection_function_dev"

os.chdir(directory)  # variable

image_one = r'C:\smile_detection\smile_detection_function_dev\image_one.jpg'
image_two = r'C:\smile_detection_function_dev\image_two.jpg' 

def image_similarity_check(image_one, image_two):
    
        
    """
    Compare the similarity between two images using deep learning-based techniques.

    This function takes two image file paths as input and calculates their similarity
    using pre-trained deep learning models. The comparison is based on the features
    extracted from the images, which allows for a more nuanced assessment of similarity
    beyond simple pixel-to-pixel comparison.

    Parameters:
        image_one (str): The file path to the first image.
        image_two (str): The file path to the second image.

    Returns:
        similarity_score (float): A similarity score between 0 and 1.
            - 0: The images are dissimilar.
            - 1: The images are very similar or identical.

    Notes:
        - The function uses the DeepFace library for deep learning-based similarity assessment.
        - Preprocessing steps like resizing, normalization, and alignment are typically performed
          by the underlying DeepFace functions.
        - The similarity score is obtained using cosine similarity of image embeddings.

    Example:
        image1_path = "path/to/image1.jpg"
        image2_path = "path/to/image2.jpg"
        similarity = image_similarity_check(image1_path, image2_path)
        if similarity > 0.09:                                         # variable value --> need to checked
            print("The images are quite similar.")
        else:
            print("The images have noticeable differences.")
    """
    
    
    threshold_value = 0.09
    models = ['VGG-Face'  , "Facenet" , "Facenet512", "OpenFace" , "DeepFace" , "ArcFace"]
    
   
    
    # DeepID , work on exception handling --> fixed
    
    # SFace , work on exception handling --> fixed
    
    # Dlib = fixed
    
    
    metrics = ["cosine", "euclidean", "euclidean_l2"]
   
    backends = ['opencv', 'ssd', 'mtcnn', 'retinaface'] 
    
    
    # backends = [ 'opencv', 'ssd','mtcnn','retinaface', 'mediapipe','yolov8', 'yunet']

    
    similarity_output_type = [ True , False ]
    image_binary_output = [] 
    
    similarity_score_output = []
    
    for temp_model_name in models:
        for temp_backend_name in backends:
            
            
            similarity_output  = DeepFace.verify(img1_path = image_one,
                                         img2_path = image_two,
                                         model_name=temp_model_name,
                                         detector_backend=temp_backend_name,
                                         enforce_detection=False,   
                                         distance_metric=metrics[0] )
        
            similarity_score_output.append(similarity_output['distance'])
        
            if similarity_output['distance'] <= threshold_value :
                image_binary_output.append(similarity_output_type[0])
            else:
                image_binary_output.append(similarity_output_type[1])
            
    print(image_binary_output)
    my_formatted_similarity_score_output = [ '%.2f' % elem for elem in similarity_score_output ]
    
    print(my_formatted_similarity_score_output)
    if image_binary_output.count(True) >= 2:
        print( "images are same" )
    else:
        print( "images are not same" )

if __name__ == "__main__": 
    image_similarity_check(image_one, image_two)

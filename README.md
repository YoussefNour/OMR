OMR Implementation using OpenCv

Features
    1- detect marks on survey
    2- detect if image is of axis
    3- rotate image back to it's correct axis
    4- return the result of the survey 
    
Details 
    #Image Allignment
    1- convert image to gray scale
    2- Using ORB to identify key features in input image and refrence image
    3- Using a descriptor give features description to identify them with
    4- match features in input image to refrence image
    5- sort matches according to similarity descendingly 
    6- take the top matches only, we only need 4 soldi features to compute Homography mat
    7- H mat we warp image back to the correct allignment  

    #result detection
    1- apply threshold to image to remove some details and invert image
    2- using hit and miss filtered circles in the image 
    3- using contours cirlce were later identified
    4- positon of circles was computed 
    5- return the values in the survey using the locations computed previosly
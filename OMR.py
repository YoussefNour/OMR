import cv2
import numpy as np

img = cv2.imread('test_sample3.jpg',0)
ret, img = cv2.threshold(img, 127, 255, 0)
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
img = cv2.bitwise_not(img)

img = cv2.resize(img, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_CUBIC)
img = cv2.morphologyEx(img, cv2.MORPH_HITMISS, element)

six_SE = np.array(
    [
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 0]
    ], dtype="int"
)

cnts_hor = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
counter = 0
font = cv2.FONT_HERSHEY_SIMPLEX
s1 = 1/20
s2 = 500
xcnts = [] 
for cnt in cnts_hor: 
    if s1 < cv2.contourArea(cnt) < s2: 
        x, y, w, h = cv2.boundingRect(cnt) 
        counter += 1 
        xcnts.append(cnt) 
        # cv2.putText(img,str(counter), (x-50, y), font, 0.5, (255, 242, 0), 1, cv2.LINE_AA)
        cv2.putText(img,"( "+ str(x)+","+str(y)+" )", (x-50, y), font, 0.5, (255, 242, 0), 1, cv2.LINE_AA)
        if y >=95 and y<=99: #gender
            if x >=416 and  x<=420:
                print("Gender: Male") 
            else:
                print("Gender: Female")    
        elif y>=122 and y<=126: #semester
            if x>=182 and x<=186:
                print("Semester: Fall")
            elif x>=271 and x<=275:
                print("Semester: Spring")    
            else:
                print("Semester: Summer")   
        elif y>=149 and y<=153: #Row 1 
            if x>=150 and x<=154:
                print("Program: MCTA")
            elif x>=194 and x<=198:
                print("Program: ENVR")    
            elif x>=238 and x<=242:
                print("Program: BLDG")   
            elif x>=282 and x<=286:
                print("Program: CESS")   
            elif x>=327 and x<=331:
                print("Program: ERGY")   
            elif x>=372 and x<=376:
                print("Program: COMM")   
            elif x>=416 and x<=420:
                print("Program: MANF")   
        elif y>=163 and y<=167:
            if x>=150 and x<=154:
                print("Program: LAAR")
            elif x>=194 and x<=198:
                print("Program: MATL")    
            elif x>=238 and x<=242:
                print("Program: CISE")   
            elif x>=282 and x<=286:
                print("Program: HAUD")   
        elif y>=322 and y<=326: #Question 1.1
             if x>=371 and x<=375:
                print("1.1: Strongly Agree")
             elif x>=405 and x<=409:
                print("1.1: Agree")    
             elif x>=439 and x<=443:
                print("1.1: Neutral")   
             elif x>=472 and x<=476:
                print("1.1: Disagree")   
             elif x>=505 and x<=509:
                print("1.1: Strongly Disagree") 
        elif y>=336 and y<=340: #Question 1.2
             if x>=371 and x<=375:
                print("1.2: Strongly Agree")
             elif x>=405 and x<=409:
                print("1.2: Agree")    
             elif x>=439 and x<=443:
                print("1.2: Neutral")   
             elif x>=472 and x<=476:
                print("1.2: Disagree")   
             elif x>=505 and x<=509:
                print("1.2: Strongly Disagree")
        elif y>=350 and y<=354: #Question 1.3
             if x>=371 and x<=375:
                print("1.3: Strongly Agree")
             elif x>=405 and x<=409:
                print("1.3: Agree")    
             elif x>=439 and x<=443:
                print("1.3: Neutral")   
             elif x>=472 and x<=476:
                print("1.3: Disagree")   
             elif x>=505 and x<=509:
                print("1.3: Strongly Disagree")
        elif y>=363 and y<=367: #Question 1.4
             if x>=371 and x<=375:
                print("1.4: Strongly Agree")
             elif x>=405 and x<=409:
                print("1.4: Agree")    
             elif x>=439 and x<=443:
                print("1.4: Neutral")   
             elif x>=472 and x<=476:
                print("1.4: Disagree")   
             elif x>=505 and x<=509:
                print("1.4: Strongly Disagree")
        elif y>=376 and y<=380: #Question 1.5
             if x>=371 and x<=375:
                print("1.5: Strongly Agree")
             elif x>=405 and x<=409:
                print("1.5: Agree")    
             elif x>=439 and x<=443:
                print("1.5: Neutral")   
             elif x>=472 and x<=476:
                print("1.5: Disagree")   
             elif x>=505 and x<=509:
                print("1.5: Strongly Disagree")       
        elif y>=416 and y<=420: #Question 2.1
             if x>=371 and x<=375:
                print("2.1: Strongly Agree")
             elif x>=405 and x<=409:
                print("2.1: Agree")    
             elif x>=439 and x<=443:
                print("2.1: Neutral")   
             elif x>=472 and x<=476:
                print("2.1: Disagree")   
             elif x>=505 and x<=509:
                print("2.1: Strongly Disagree")
        elif y>=430 and y<=434: #Question 2.2
             if x>=371 and x<=375:
                print("2.2: Strongly Agree")
             elif x>=405 and x<=409:
                print("2.2: Agree")    
             elif x>=439 and x<=443:
                print("2.2: Neutral")   
             elif x>=472 and x<=476:
                print("2.2: Disagree")   
             elif x>=505 and x<=509:
                print("2.2: Strongly Disagree")       
        elif y>=443 and y<=447: #Question 2.3
             if x>=371 and x<=375:
                print("2.3: Strongly Agree")
             elif x>=405 and x<=409:
                print("2.3: Agree")    
             elif x>=439 and x<=443:
                print("2.3: Neutral")   
             elif x>=472 and x<=476:
                print("2.3: Disagree")   
             elif x>=505 and x<=509:
                print("2.3: Strongly Disagree")       
        elif y>=456 and y<=460: #Question 2.4
             if x>=371 and x<=375:
                print("2.4: Strongly Agree")
             elif x>=405 and x<=409:
                print("2.4: Agree")    
             elif x>=439 and x<=443:
                print("2.4: Neutral")   
             elif x>=472 and x<=476:
                print("2.4: Disagree")   
             elif x>=505 and x<=509:
                print("2.4: Strongly Disagree")    
        elif y>=469 and y<=473: #Question 2.5
             if x>=371 and x<=375:
                print("2.5: Strongly Agree")
             elif x>=405 and x<=409:
                print("2.5: Agree")    
             elif x>=439 and x<=443:
                print("2.5: Neutral")   
             elif x>=472 and x<=476:
                print("2.5: Disagree")   
             elif x>=505 and x<=509:
                print("2.5: Strongly Disagree")             
        elif y>=482 and y<=486: #Question 2.6
             if x>=371 and x<=375:
                print("2.6: Strongly Agree")
             elif x>=405 and x<=409:
                print("2.6: Agree")    
             elif x>=439 and x<=443:
                print("2.6: Neutral")   
             elif x>=472 and x<=476:
                print("2.6: Disagree")   
             elif x>=505 and x<=509:
                print("2.6: Strongly Disagree")                                            
        elif y>=522 and y<=526: #Question 3.1
             if x>=371 and x<=375:
                print("3.1: Strongly Agree")
             elif x>=405 and x<=409:
                print("3.1: Agree")    
             elif x>=439 and x<=443:
                print("3.1: Neutral")   
             elif x>=472 and x<=476:
                print("3.1: Disagree")   
             elif x>=505 and x<=509:
                print("3.1: Strongly Disagree")    
        elif y>=535 and y<=539: #Question 3.2
             if x>=371 and x<=375:
                print("3.2: Strongly Agree")
             elif x>=405 and x<=409:
                print("3.2: Agree")    
             elif x>=439 and x<=443:
                print("3.2: Neutral")   
             elif x>=472 and x<=476:
                print("3.2: Disagree")   
             elif x>=505 and x<=509:
                print("3.2: Strongly Disagree")     
        elif y>=549 and y<=553: #Question 3.3
             if x>=371 and x<=375:
                print("3.3: Strongly Agree")
             elif x>=405 and x<=409:
                print("3.3: Agree")    
             elif x>=439 and x<=443:
                print("3.3: Neutral")   
             elif x>=472 and x<=476:
                print("3.3: Disagree")   
             elif x>=505 and x<=509:
                print("3.3: Strongly Disagree") 
        elif y>=589 and y<=593: #Question 4.1
             if x>=371 and x<=375:
                print("4.1: Strongly Agree")
             elif x>=405 and x<=409:
                print("4.1: Agree")    
             elif x>=439 and x<=443:
                print("4.1: Neutral")   
             elif x>=472 and x<=476:
                print("4.1: Disagree")   
             elif x>=505 and x<=509:
                print("4.1: Strongly Disagree") 
        elif y>=603 and y<=607: #Question 4.2
             if x>=371 and x<=375:
                print("4.2: Strongly Agree")
             elif x>=405 and x<=409:
                print("4.2: Agree")    
             elif x>=439 and x<=443:
                print("4.2: Neutral")   
             elif x>=472 and x<=476:
                print("4.2: Disagree")   
             elif x>=505 and x<=509:
                print("4.2: Strongly Disagree")      
        elif y>=629 and y<=633: #Question 4.3
             if x>=371 and x<=375:
                print("4.3: Strongly Agree")
             elif x>=405 and x<=409:
                print("4.3: Agree")    
             elif x>=439 and x<=443:
                print("4.3: Neutral")   
             elif x>=472 and x<=476:
                print("4.3: Disagree")   
             elif x>=505 and x<=509:
                print("4.3: Strongly Disagree")    
        elif y>=668 and y<=672: #Question 5.1
             if x>=371 and x<=375:
                print("5.1: Strongly Agree")
             elif x>=405 and x<=409:
                print("5.1: Agree")    
             elif x>=439 and x<=443:
                print("5.1: Neutral")   
             elif x>=472 and x<=476:
                print("5.1: Disagree")   
             elif x>=505 and x<=509:
                print("5.1: Strongly Disagree")   
        elif y>=682 and y<=686: #Question 5.2
             if x>=371 and x<=375:
                print("5.2: Strongly Agree")
             elif x>=405 and x<=409:
                print("5.2: Agree")    
             elif x>=439 and x<=443:
                print("5.2: Neutral")   
             elif x>=472 and x<=476:
                print("5.2: Disagree")   
             elif x>=505 and x<=509:
                print("5.2: Strongly Disagree")                                                                 
                   

cv2.imshow("img", img)


cv2.waitKey(0)
cv2.destroyAllWindows()







# ret, corners=cv2.findCirclesGrid(img,(9,9),None)

# print(corners)
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
# corners2 = cv2.cornerSubPix(img,corners,(11,11),(-1,-1),criteria)

# ((x,y),(w,h),angle) = cv2.minAreaRect(corners2)
# rows,cols = img.shape[:2]
# angle += 90

# M = cv2.getRotationMatrix2D((int(cols/2),int(rows/2)), angle, 1.0)
# nimg = cv2.warpAffine(img,M,(cols,rows))


#img = cv2.imread('test_sample8.jpg', 0)
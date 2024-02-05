from helper_functions import camera, computer_vision,sensehat
### TO-DO: You may require more imports

def main():
    camera_i = camera.get_camera() #DO NOT MODIFY, function call must work as is 
    sense = sensehat.get_sensehat() #DO NOT MODIFY, function call must work as is 
    
    take_background_image = True #TO-DO: Should be a user input

    if take_background_image:
        ### TO-DO: Countdown image capture of background  
        preview = False
        countdown=0
        camera.capture_image(camera_i,"data/images/background.jpg", countdown_time=countdown, preview=preview) #DO NOT MODIFY, function call must work as is 
    
    arm_system = True #TO-DO: Should be a user input

    if arm_system:
        interval = 10 #TO-DO: Should be a user input
        t1 = 480000000 #TO-DO: Should be a user input
       
       ### TO-DO: Countdown to monitoring

        count = 0
        while True: #DO NOT MODIFY, function call must work as is 
            camera.capture_image(camera_i,"data/images/image%s.jpg" % count, countdown_time=interval) #DO NOT MODIFY, function call must work as is 
            person_detected = computer_vision.person_detected("data/images/background.jpg","data/images/image%s.jpg" % count, t1)  #DO NOT MODIFY, function call must work as is 
            if person_detected: #DO NOT MODIFY, function call must work as is 
                print("Person Detected") #DO NOT MODIFY, function call must work as is 
                sensehat.alarm(sense,interval)  #DO NOT MODIFY, function call must work as is 
            else:
                print("No Person Detected") #DO NOT MODIFY, function call must work as is 
            count += 1


if __name__ == "__main__":
    main()

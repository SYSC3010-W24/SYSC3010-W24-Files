# returns camera instance
def get_camera():

# Takes in camera instance and preview time
# displays camera preview for the indicated amount of time
def camera_preview(camera, preveiw_time):

# Takes in camera instance and degrees
# roatates camera to the indicated degree
def rotate_camera(camera,degrees):

# Takes in camera instance, output image location, countdown time and preview Boolean
# If preview is true, preview is started
# The code waits the indicated countdown time before the image is taken and stored in the indicated location
# the preview is stopped if it was started
def capture_image(camera,image_out_location, countdown_time = 0, preview = False ):

# Takes in camera instance, output video location, video length, countdown time and preview Boolean
# If preview is true, preview is started
# The code waits the indicated countdown time before the video is taken for the indicated amount of time 
# and stored in the indicated location
# the preview is stopped if it was started
def capture_video(camera,video_out_location, video_length, countdown_time = 0, preview = False):

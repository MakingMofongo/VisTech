f snap(cap):
    while True:
        if(exiting):
            break
        global img
        # print('globalled img')
        success, img = cap.r
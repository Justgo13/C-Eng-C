import cv2
from Steps.base_step import BaseStep
from Steps.mask_step import MaskStep

configuration = {}

if __name__ == '__main__':

    print('Program Start')
    # declare steps
    step = MaskStep()
    steps = [step]
    # open files
    with open('config.txt', 'r') as config:
        for line in config:
            if len(line) == 0:
                continue
            name, setting = line.split(':')
            name = name.strip()
            setting = setting.strip()
            configuration[name] = setting
            pass
        pass
    # setting up image
    vid = cv2.VideoCapture(0)

    current= 0
    while True:
        # get image from camera
        ret, frame = vid.read()
        if not ret:
            continue
        #  run screening step
        status = steps[current].run(frame)
        if status == BaseStep.FAIL:
            current = 0  # reset
        elif status == BaseStep.SUCCESS and current == len(steps)-1:
            exit(0)
            pass # open door step??
        elif status == BaseStep.SUCCESS:
            current = (current+1) % len(steps)  # proceed to next step
            pass

        cv2.imshow('frame', frame)  # show flipped screen for easier time
        # exit application on request
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        pass

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    print('End of Application')
    pass

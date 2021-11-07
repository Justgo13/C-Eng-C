import cv2
from Steps.base_step import BaseStep
from Steps.mask_step import MaskStep
from Steps.vaccine_step import VaccinePassportStep

if __name__ == '__main__':

    print('Program Start')
    # declare steps
    mask_step = MaskStep()
    vaccine_step = VaccinePassportStep()
    steps = [mask_step, vaccine_step]
    # open files

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
            steps[current].reset()
            current = 0  # reset
        elif status == BaseStep.SUCCESS and current == len(steps)-1:
            exit(0)
            pass # open door step??
        elif status == BaseStep.SUCCESS:
            steps[current].reset()
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

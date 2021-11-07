import ScreeningStep
import cv2

configuration = {}


if __name__ == '__main__':

    print('Program Start')
    # declare steps
    step = ScreeningStep.ExampleStep('STEP1')
    step2 = ScreeningStep.ExampleStep('STEP2')
    steps = [step, step2]
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
    exit(0)
    # setting up image
    vid = cv2.VideoCapture(0)

    current= 1
    while True:
        # get image from camera
        ret, frame = vid.read()
        if not ret:
            continue
        #  run screening step
        status = steps[current].run(frame)
        if status == ScreeningStep.ScreeningStep.FAIL:
            current = 0  # reset
        elif status == ScreeningStep.ScreeningStep.SUCCESS and current == len(steps)-1:
            pass # open door step??
        elif status == ScreeningStep.ScreeningStep.SUCCESS:
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

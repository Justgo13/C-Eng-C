import ScreeningStep

if __name__ == '__main__':
    print('Start')
    step = ScreeningStep.ExampleStep('STEP1')
    step2 = ScreeningStep.ExampleStep('STEP2')
    status = 0
    steps = [step, step2]
    current= 1
    while True:

        if steps[current].run('') == ScreeningStep.ScreeningStep.FAIL:
            current = 0

    pass

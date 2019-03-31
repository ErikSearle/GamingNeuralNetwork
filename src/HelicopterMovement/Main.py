from time import sleep
from src.HelicopterMovement.ClickingThread import ClickingThread
from src.HelicopterMovement.NavigatingThread import NavigatingThread


# TODO: Seriously cut down on the info coming in from the screen grab
# TODO: Get it to successfully dodge 5 blocks
# TODO: Change screen shot to use pyautogui
# TODO: Neural Network

def main():
    '''
     Thoughts for integrating the neural network, currently the decision is made in
     a while loop whether the helicopter hovers, ascends, or descends. That logic
     can be taken over by the neural net possibly and the neural net will tell the
     helicopter when to stop doing what it is doing and do something else :)
     '''

    #I used this to add a delay to the robot before my mouse was taken over
    sleep(5)
    clicking_thread = ClickingThread()
    navigating_thread = NavigatingThread()
    clicking_thread.start()
    navigating_thread.start()


if __name__ == "__main__":
    main()

from time import sleep
from src.HelicopterMovement.AutoClicker import fly

# TODO: Seriously cut down on the info coming in from the screen grab
# TODO: Get it to successfully dodge 5 blocks
# TODO: Change screen shot to use pyautogui
# TODO: Neural Network


def main():
    """
    Runs the whole program
    :return:
    """

    #I used this to add a delay to the robot before my mouse was taken over
    sleep(5)
    fly()


if __name__ == "__main__":
    main()

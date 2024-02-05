import time


def count_down(duration):
    
    while duration>=0:
        minutes, seconds = divmod(duration, 60)
        timer='{:02d}:{:02d}'.format(minutes,seconds)
        print(f"remaining time: ",timer, end="\r")

        time.sleep(1)
        duration-=1

    print("\nCountdown Complete!")

if __name__ == "__main__":
    user_input = int(input("Enter countdown duration in seconds: "))
    count_down(user_input)

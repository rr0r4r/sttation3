import time

def timer():
    inp = input('input time on the format HH:MM:SS ')
    hours,minutes,seconds = inp.split(":")
    allSeconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

    
    for i in range(allSeconds):
        time.sleep(1)
        remain = allSeconds - i - 1
        hours = remain // 3600
        minutes = (remain % 3600) // 60
        seconds = (remain % 3600) % 60
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    print('Times over')

timer()

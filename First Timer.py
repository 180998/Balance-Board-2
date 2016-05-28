    Sec=0
    Min=0
    Lap=0

    start=time.time()
    end=time.time()

    while True:
        time.sleep(1)
        end=time.time()
        print(round(end-start,6))

        Sec += 1
        time.sleep(1)
        secClock = (str(Min) + " Mins " + str(Sec) + " Sec ")

        print secClock
        if Sec == 60:
            Sec = 0
            Min += 1
            clock = (str(Min) + " Minute")
            print(clock)

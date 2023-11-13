led0 = 0
led1 = 0
led2 = 0
cnt_loop = 0

while True:
    # Update counter
    if led0 == 0 and cnt_loop != 0:
        led0 = 1
    else:
        led0 = 0

    if cnt_loop % 2 == 0 and cnt_loop != 0:
        if led1 == 0:
            led1 = 1
        else:
            led1 = 0

    if cnt_loop % 4 == 0 and cnt_loop != 0:
        if led2 == 0:
            led2 = 1
        else:
            led2 = 0
    cnt_loop += 1
    if cnt_loop == 8:
        cnt_loop = 0
    counter_state = f"{led2}{led1}{led0} -> cnt_loop = {cnt_loop}"
    print(counter_state)

    if led0 == 1 and led1 == 1 and led2 == 1:
        led0 = 0
        led1 = 0
        led2 = 0
        # break
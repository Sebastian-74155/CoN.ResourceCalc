from datetime import datetime
import os
gspeed = 1
def TimeRefresh():
    now = datetime.now()
    current_time = now.strftime("%#H:%M")
    return now, current_time
def Menu():
    os.system("cls")
    print("===CONFLICT OF NATIONS - Resources calculator===")
    print("Select your game speed (1 for default, 4 for 4x or 10 for 10x)")
    gspeed = int(input())
    if gspeed == 1: DefaultSpeed()
    elif gspeed == 4: FourFoldSpeed()
    elif gspeed == 10: TenFoldSpeed()
    else:
        print("Invalid number")
        input()
        Menu()
def DefaultSpeed():
    now, current_time = TimeRefresh()
    print(f"Your resources at {current_time}:")
    resc = int(input())
    print("Production rate per in-game hour: ")
    rate = int(input())
    plus_hr = 0;
    print("Input how much time you will wait in real-time hours:")
    plus_hr = int(input())
    resc = resc + (rate * plus_hr)
    then_hr = now.hour + plus_hr
    then_min = str(now.minute)
    if then_hr < 24: print(f"At {then_hr}:{then_min.zfill(2)}, your resources will be {resc}")
    else:
        then_hr = then_hr % 24
        print(f"At {then_hr}:{then_min.zfill(2)} of the next day, your resources will be {resc}")
    Retry()
def FourFoldSpeed():
    now, current_time = TimeRefresh()
    print(f"Your resources at {current_time}:")
    resc = int(input())
    print("Production rate per in-game hour: ")
    rate = int(input())
    plus_hr = 0;
    print("Input how much time you will wait in real-time hours:")
    plus_hr = int(input())
    resc = resc + (rate * 4 * plus_hr)
    then_hr = now.hour + plus_hr
    then_min = str(now.minute)
    if then_hr < 24: print(f"At {then_hr}:{then_min.zfill(2)},\n{plus_hr * 4} in-game hours will have passed\nand your resources will be {resc}")
    else:
        then_hr = then_hr % 24
        print(f"At {then_hr}:{then_min.zfill(2)} of the next day,\n{plus_hr * 4} in-game hours will have passed\nand your resources will be {resc}")
    Retry()
def TenFoldSpeed():
    now, current_time = TimeRefresh()
    print(f"Your resources at {current_time}:")
    resc = int(input())
    print("Production rate per in-game hour: ")
    rate = int(input())
    plus_hr = 0;
    print("Input how much time you will wait in real-time hours:")
    plus_hr = int(input())
    resc = resc + (rate * 10 * plus_hr)
    then_hr = now.hour + plus_hr
    then_min = str(now.minute)
    if then_hr < 24: print(f"At {then_hr}:{then_min.zfill(2)},\n{plus_hr * 10} in-game hours will have passed\nand your resources will be {resc}")
    else:
        then_hr = then_hr % 24
        print(f"At {then_hr}:{then_min.zfill(2)} of the next day,\n{plus_hr * 10} in-game hours will have passed\nand your resources will be {resc}")
    Retry()
def Retry():
    print("Retry?")
    print("[Y] Yes; [N] Quit")
    response = str(input())
    if response == "y" or response == "Y":
        os.system("cls")
        Menu()
    elif response == "n" or response == "N":
        quit()
    else: Retry()
Menu()
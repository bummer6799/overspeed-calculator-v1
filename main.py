while True:
    vehicle = input("Light or Heavy Vehicle? ")
    if vehicle == ("Light") or ("light") or ("heavy") or ("Heavy"):
        # print("Vehicle Type is", vehicle)
        break
    else:
        print("Invalid Answer")
        continue

speed = int(input("Enter the speed of the vehicle: "))

print()
print("************")
print()

newspeed = (speed-60)
if newspeed < 0:
    print("Vehicle speed is under speed limit")
    quit()
else:
    ()
print("Speed exceeded by",round(newspeed,2),"km/h")



x = ("Prosecution in court")

print("Vehicle Type is", vehicle)

if vehicle == ("Light") or vehicle == ("light"):
    if newspeed < 20:
        print("4 Demerit Points Awarded")
        print("$150 Fine")
    elif 30 >= newspeed >= 20:
        print("6 Demerit Points Awarded")
        print("$200 Fine")
    elif 40 >= newspeed >= 30:
        print("8 Demerit Points")
        print("$300/- Fine")
    elif 50 >= newspeed >= 40:
        print("12 Demerit Points")
        print(x)
    elif 60 >= newspeed >= 50:
        print("18 Demerit Points")
        print(x)
    elif newspeed > 60:
        print("24 Demerit Points")
        print(x)
    else:
        ()
else:
    ()

if vehicle == ("Heavy") or vehicle == ("heavy"):
    if newspeed < 20:
        print("4 Demerit Points Awarded")
        print("$200 Fine")
    elif 30 >= newspeed >= 20:
        print("6 Demerit Points Awarded")
        print("$250 Fine")
    elif 40 >= newspeed >= 30:
        print("8 Demerit Points")
        print("$400/- Fine")
    elif 50 >= newspeed >= 40:
        print("12 Demerit Points")
        print(x)
    elif 60 >= newspeed >= 50:
        print("18 Demerit Points")
        print(x)
    elif newspeed > 60:
        print("24 Demerit Points")
        print(x)
    else:
        ()
else:
    ()

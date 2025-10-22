device_status ="active";
temprature=38

if device_status == "active":
    if temprature >35:
        print("High Temperature Alert!")
    else:
        print("Temperature is normal.")
else:
    print("Device is inactive. Please activate the device to read temperature.")
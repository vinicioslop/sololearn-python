# Tier: 1-Beginner

# Windchill combines the actual temperature with the wind
# speed to calculate the windchill factor, or what the
# perceived temperature is versus the actual temperature.

# User Stories

#  - User can select the measurement system calculations
#    will be performed in - Metric or English
#    User can enter the actual temperature and the wind
#    speed

#  - User can press the Calculate button to display the
#    wind chill

#  - User will receive an error message when Calculate
#    is clicked if data values are not entered

# Bonus features

#  - User will receive an error message when Calculate is
#    clicked if the resulting wind chill factor is greater
#    than or equal to the actual temperature. Since this
#    signifies an internal error in the calculation you may
#    also satisfy this requirement using an assertion

#  - User will be prompted to enter new data values if
#    Calculate is pressed without first changing at least
#    one of the input fields

#  - User will see an updated wind chill factor whenever
#    new actual temperature or wind speed values are entered,
#    without being required to click the Calculate button
from math import sqrt

print("Welcome to the Windchill Calculator!")

while True:
    print("Input the System Measurement - (M)etric or (I)mperial")
    sys_measurement = input("Option: ").upper()

    if sys_measurement == "M":
        temperature = float(input("\nInput the temperature (°C).: "))
        wind_speed = float(input("Input the wind speed (km/h): "))

        wind_chill = 13.12 + 0.6215 * temperature - 11.37 * \
            wind_speed**0.16 + 0.3965 * temperature * wind_speed**0.16

        print("\nWindchill: {:.2f} °C".format(wind_chill))

    if sys_measurement == "I":
        temperature = float(input("\nInput the temperature (°F)....: "))
        wind_speed = float(input("Input the wind speed (miles/h): "))

        wind_chill = 35.74 + 0.6215 * temperature - 35.75 * \
            wind_speed**0.16 + 0.4275 * temperature * wind_speed**0.16

        print("\nWindchill: {:.2f} °F".format(wind_chill))

    print("\nWants to calculate again? (y)es or (n)o")
    option = input("Option: ").lower()

    if option == "n":
        print("\nExit...")
        break

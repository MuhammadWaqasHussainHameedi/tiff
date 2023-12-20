import serial

# Configure the serial port (check your COM port)
ser = serial.Serial('COM3', 9600)  # COM3 or the correct port

while True:
    user_angle = input("Enter the desired angle (0-180 degrees): ")
    try:
        user_angle = int(user_angle)
        if 0 <= user_angle <= 180:
            ser.write(f"{user_angle}\n".encode())
        else:
            print("Invalid angle. Angle should be between 0 and 180 degrees.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 0 and 180.")
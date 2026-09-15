# Overvoltage and Undervoltage Protection System

MIN_VOLTAGE = 200  # Minimum safe voltage
MAX_VOLTAGE = 250  # Maximum safe voltage

print("=== Voltage Protection System ===")

voltage = float(input("Enter supply voltage (V): "))

if voltage < MIN_VOLTAGE:
    print("UNDERVOLTAGE DETECTED!")
    print("Load disconnected for protection.")
    print("Relay Status: OFF")

elif voltage > MAX_VOLTAGE:
    print("OVERVOLTAGE DETECTED!")
    print("Load disconnected for protection.")
    print("Relay Status: OFF")

else:
    print("Voltage is normal.")
    print("Load connected.")
    print("Relay Status: ON")

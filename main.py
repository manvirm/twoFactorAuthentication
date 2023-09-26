import time
import pyotp

key = "SuperSecretKey"

counter  = 0

hotp = pyotp.HOTP(key)

for _ in range(5):
    print(hotp.verify(input("Enter Code:"), counter))
    counter += 1
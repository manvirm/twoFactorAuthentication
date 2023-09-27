import time
import pyotp

key = "SuperSecretKey"

counter  = 0

hotp = pyotp.HOTP(key)

print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))

for _ in range(5):
    print(hotp.verify(input("Enter Code:"), counter))
    counter += 1
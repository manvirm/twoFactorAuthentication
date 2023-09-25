import time
import pyotp

key = "SuperSecretKey"

totp = pyotp.TOTP(key)
print(totp.now())

time.sleep(30)

print(totp.now())

input_code = input("Enter 2FA Code:")

totp.verify(input_code)

print(totp.verify(input_code))
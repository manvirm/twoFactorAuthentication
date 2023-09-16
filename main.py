import time
import pyotp

key = "SuperSecretKey"

totp = pyotp.TOTP(key)
print(totp.now())

time.sleep(30)

print(totp.now())
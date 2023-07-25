import pyotp

totp = pyotp.TOTP(input("Enter Code: "))

print("Current OTP:", totp.now())

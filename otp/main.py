import os
import pyotp
import bcrypt


# Function to generate the TOTP
def generate_totp(key):
    totp = pyotp.TOTP(key)
    return totp.now()


# Function to store the OTP file using bcrypt
def store_otp_file(name, otp):
    folder_name = "otp_files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Hash the OTP using bcrypt before storing it
    hashed_otp = bcrypt.hashpw(otp.encode(), bcrypt.gensalt())

    file_path = os.path.join(folder_name, f"{name}.txt")
    with open(file_path, "wb") as file:
        file.write(hashed_otp)

    print(f"OTP for '{name}' has been stored successfully.")


# Function to retrieve and print OTP from stored file
def retrieve_otp_file(name):
    folder_name = "otp_files"
    file_path = os.path.join(folder_name, f"{name}.txt")

    if not os.path.exists(file_path):
        print(f"No OTP found for '{name}'.")
        return

    with open(file_path, "rb") as file:
        hashed_otp = file.read()

    otp = "f{name}.txt"
    if bcrypt.checkpw(otp.encode(), hashed_otp):
        print(f"The OTP for '{name}' is: {otp}")
    else:
        print("Incorrect OTP.")


if __name__ == "__main__":
    print("Welcome to Authenticator OTP manager.")
    print("1. Generate OTP")
    print("2. Store OTP")
    print("3. Retrieve OTP")

    choice = input("Please select an option (1/2/3): ")

    if choice == "1":
        key = input("Enter the OTP key: ")
        otp = generate_totp(key)
        print(f"The OTP is: {otp}")

    elif choice == "2":
        name = input("Enter a name to store the OTP: ")
        key = input("Enter the OTP key: ")

        otp = generate_totp(key)
        store_otp_file(name, otp)

    elif choice == "3":
        name_to_retrieve = input("Enter a name to retrieve the OTP: ")
        retrieve_otp_file(name_to_retrieve)

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

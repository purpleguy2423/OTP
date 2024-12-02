import onetimepass as otp

# secretEnter = input("Enter Your Client Secret For a ONE time 2FA Code: ")
# my_secret = secretEnter
# my_token = otp.get_totp(my_secret)
# if my_token < 99999:
#   print("Error! Code: 1")
# print(my_token)

try:
    secretEnter = input("Enter Your Client Secret For a ONE time 2FA Code: ")
    my_secret = secretEnter
    my_token = otp.get_totp(my_secret)
    if my_token < 99999:
        print("Error! Code: 1")
    print(my_token)
except Exception as e:
    print("An error occurred:", e)
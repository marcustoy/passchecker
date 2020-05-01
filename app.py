import sys
import os
import hashlib
import requests


def convert_sha1(input_str):
    encoded_str = input_str.encode()
    hash_obj = hashlib.sha1(encoded_str)
    return hash_obj.hexdigest()


def get_sha1_list(sha1_str):
    url_str = "https://api.pwnedpasswords.com/range/" + sha1_str

    contents = requests.get(url_str).text
    return contents.split("\r\n")



if __name__ == "__main__":

    while True:
        #clear console screen
        if sys.platform == "win32" or sys.platform == "cygwin":
            os.system('cls')
        else:
            os.system('clear')

        print("PassChecker v1.1.1\n")

        #Ask for input password
        pass_str = input("Insert password to check: ")

        #Convert password into SHA-1 hash
        sha1_str = convert_sha1(pass_str)

        #Strip out first 5 digits of password SHA-1 hash
        sha1_stripped_front = sha1_str[0:5]
        sha1_stripped_back = sha1_str[5:]

        #Get list of SHA-1 compomised passwords from pwnedpasswords API
        sha1_list = get_sha1_list(sha1_stripped_front)

        #Match password's SHA-1 hash's remaininng digits (6th till end) with the list and console output if match is found
        match_found = False
        for ind_sha1 in sha1_list:
            ind_sha1_components = str(ind_sha1).split(":")
            if ind_sha1_components[0].lower() == sha1_stripped_back.lower():
                match_found = True
                break
        
        if match_found == True:
            print(f"PASSWORD IS PUBLIC for {str(ind_sha1_components[1])} times. Consider using/changing another password.")
        else:
            print("PASSWORD IS NOT PUBLIC.")


        #Ask whether to restart program or exit program
        print("\n")
        restart_input = input("Check another password? (y): ")
        if str(restart_input).lower().replace(" ", "") == "y":
            continue
        else:
            break

    #Exit program
    print("PassChecker terminated. Have a nice day.")
    sys.exit()
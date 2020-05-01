import sys
import hashlib
import urllib.request
import contextlib


def convert_sha1(input_str):
    encoded_str = input_str.encode()
    hash_obj = hashlib.sha1(encoded_str)
    return hash_obj.hexdigest()


def get_sha1_list(sha1_str):
    url_str = "https://api.pwnedpasswords.com/range/" + sha1_str

    with contextlib.closing(urllib.request.urlopen(url_str)) as r:
        contents = str(r.read())
    
    if contents[0] == "b":
        contents = contents[2:]

    return contents.split("\\r\\n")
    


if __name__ == "__main__":

    while True:
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
    sys.exit()
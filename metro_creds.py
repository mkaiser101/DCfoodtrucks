import pickle , base64, sys
from getpass import getpass

def main():

    if sys.version_info < (3,0):
        primary_key = getpass("primary_key: ")
        primary_key = base64.b64encode(primary_key)
        #secondary_key = getpass("secondary_key: ")
        #secondary_key = base64.b64encode(secondary_key)
    else:
        primary_key = getpass("primary_key: ")
        primary_key = base64.b64encode(primary_key.encode())
        #secondary_key = getpass("secondary_key: ")
        #secondary_key = base64.b64encode(secondary_key)

    with open("twitter_creds.bin", 'wb') as writefile:
        creds = (primary_key)
        pickle.dump(creds, writefile)

if __name__ == "__main__":
    main()
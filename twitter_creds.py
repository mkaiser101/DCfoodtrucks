import pickle , base64, sys
from getpass import getpass

def main():

    if sys.version_info < (3,0):
        consumer_key = getpass("consumer_key: ")
        consumer_key = base64.b64encode(consumer_key)
        consumer_secret = getpass("consumer_secret: ")
        consumer_secret = base64.b64encode(consumer_secret)
        access_token = getpass("access_token: ")
        access_token = base64.b64encode(access_token)
        access_token_secret = getpass("access_token_secret: ")
        access_token_secret = base64.b64encode(access_token_secret)
    else:
        consumer_key = getpass("consumer_key: ")
        consumer_key = base64.b64encode(consumer_key.encode())
        consumer_secret = getpass("consumer_secret: ")
        consumer_secret = base64.b64encode(consumer_secret.encode())
        access_token = getpass("access_token: ")
        access_token = base64.b64encode(access_token.encode())
        access_token_secret = getpass("access_token_secret: ")
        access_token_secret = base64.b64encode(access_token_secret.encode())
    with open("twitter_creds.bin", 'wb') as writefile:
        creds = (consumer_key, consumer_secret, access_token, access_token_secret)
        pickle.dump(creds, writefile)

if __name__ == "__main__":
    main()

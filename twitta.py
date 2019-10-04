from __future__ import absolute_import, print_function

import tweepy, base64, requests, pickle

class twitter_client(object):

    def __init__(self, cred_file="twitter_creds.bin"):

        if cred_file:
            with open(cred_file, 'rb') as readfile:
                auth_list = pickle.load(readfile)
            consumer_key = base64.decodebytes(auth_list[0])
            consumer_secret = base64.decodebytes(auth_list[1])
            access_token = base64.decodebytes(auth_list[2])
            access_token_secret = base64.decodebytes(auth_list[3])
        elif cred_file == None:
            print("no cred file")

        self.session = requests.Session()

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        #self.session.auth = requests.auth.HTTPBasicAuth(api)
        #todo: add auth to session rather than function wise for bp
    def tester(self):
        
        with open("twitter_creds.bin", 'rb') as readfile:
            auth_list = pickle.load(readfile)
        consumer_key = base64.decodebytes(auth_list[0])
        consumer_secret = base64.decodebytes(auth_list[1])
        access_token = base64.decodebytes(auth_list[2])
        access_token_secret = base64.decodebytes(auth_list[3])
    
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        payload = (api.me().name)
        return payload
        '''try:
            api.me().name.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("HTTP error:" + str(e))
            return None
        '''
        

def main():
    client = twitter_client()
    print(client.tester())

if __name__ == "__main__":
    main()


topDcfoodtrucks = ["pepebyjose", "LobstertruckDC", "dcslices", "DCEmpanadas", "CapMacDC", "bigcheesetruck", "TaKorean", "bbqbusdc", "hulagirltruck", "Borinquenlunchb"] 

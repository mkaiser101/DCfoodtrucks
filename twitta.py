from __future__ import absolute_import, print_function

import tweepy, base64, requests, pickle
#for v2 : imporve handling of creds, support more operations with less reused code
class twitter_client(object):

    def __init__(self):

        self.session = requests.Session()
        
    def _handle_creds(self):
        '''Reusable credential handler
        Arguments:
        self - instance reference
        '''
        with open("twitter_creds.bin", 'rb') as readfile:
            auth_list = pickle.load(readfile)
        consumer_key = base64.decodebytes(auth_list[0])
        consumer_secret = base64.decodebytes(auth_list[1])
        access_token = base64.decodebytes(auth_list[2])
        access_token_secret = base64.decodebytes(auth_list[3])
    
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    
    def tester(self, account):
        '''get_user timeline api reference
        Arguments:
        self - instance reference
        accounts - twitter accounts to get tweets from 
        '''
        auth = self._handle_creds()
        api = tweepy.API(auth)
        
        payload = (api.user_timeline(account))
        print (payload)
        return payload
        
        

def main():
    client = twitter_client()
    topDcfoodtrucks = ["pepebyjose", "LobstertruckDC", "dcslices", "DCEmpanadas", "CapMacDC", "bigcheesetruck", "TaKorean", "bbqbusdc", "hulagirltruck", "Borinquenlunchb"]
    for foodtruck in topDcfoodtrucks:
        client.tester(foodtruck)

if __name__ == "__main__":
    main()


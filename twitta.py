from __future__ import absolute_import, print_function

import tweepy, base64, requests, pickle, json

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
    
    def _try_for_status(self, request):
        '''Reusable try block
        Arguments:
        self - instance reference
        request - API call type with API endpoint
        '''
        try:
            request.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logging.error("HTTP Error:" + str(e))
            return False
        return True


    def get_user_timeline(self, account):
        '''get_user timeline api reference returning important fields for food truck tracker
        Arguments:
        self - instance reference
        accounts - twitter accounts to get tweets from 
        '''
        auth = self._handle_creds()
        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
        
        payload = (api.user_timeline(account))
        user_load = payload[0]
        return user_load

    def post_user_timeline(self, tweetText):
        '''get_user timeline api reference returning important fields for food truck tracker
        Arguments:
        self - instance reference
        tweetText - text to tweet 
        '''
        auth = self._handle_creds()
        api = tweepy.API(auth)
        api.update_status(tweetText)
        return []
        
        

def main():
    client = twitter_client()
    #topDcfoodtrucks = ["pepebyjose", "LobstertruckDC", "dcslices", "DCEmpanadas", "CapMacDC", "bigcheesetruck", "TaKorean", "bbqbusdc", "hulagirltruck", "Borinquenlunchb"]
    #for foodtruck in topDcfoodtrucks:
    print(client.get_user_timeline("pepebyjose"))

if __name__ == "__main__":
    main()


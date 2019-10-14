########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, pickle, json



class metro_client(object):

    def __init__(self):

        self.session = requests.Session()

    def _handle_creds(self):
        '''Reusable credential handler
        Arguments:
        self - instance reference
        '''
        with open("metro_creds.bin", 'rb') as readfile:
            auth_list = pickle.load(readfile)
        primary_key = base64.decodebytes(auth_list[0])
        
        
        return primary_key
        

    def build_params(self):
        payload = []
        auth = self._handle_creds()
        headers = {
        # Request headers
            'api_key': auth, 
        }
        red_params = urllib.parse.urlencode({
        # Request parameters
            'LineCode': 'RD',
        })
        yellow_params = urllib.parse.urlencode({
        # Request parameters
            'LineCode': 'YL',
        })
        green_params = urllib.parse.urlencode({
        # Request parameters
            'LineCode': 'GR',
        })
        blue_params = urllib.parse.urlencode({
        # Request parameters
            'LineCode': 'BL',
        })
        orange_params = urllib.parse.urlencode({
        # Request parameters
            'LineCode': 'OR',
        })
        silver_params = urllib.parse.urlencode({
        # Request parameters
            'LineCode': 'SV',
        })
        params = [red_params, yellow_params, green_params, blue_params, orange_params, silver_params]
        for param in params:
            try:
                conn = http.client.HTTPSConnection('api.wmata.com')
                conn.request("GET", "/Rail.svc/json/jStations?%s" % param, "{body}", headers)
                response = conn.getresponse()
                data = response.read()
                print(data)
                payload.append(data)
                conn.close()
            except Exception as e:
                print("[Errno {0}] {1}".format(e.errno, e.strerror))

        print('found:', payload)
        return payload

def main():
    client = metro_client()
    #topDcfoodtrucks = ["pepebyjose", "LobstertruckDC", "dcslices", "DCEmpanadas", "CapMacDC", "bigcheesetruck", "TaKorean", "bbqbusdc", "hulagirltruck", "Borinquenlunchb"]
    #for foodtruck in topDcfoodtrucks:
    print(client.build_params())

if __name__ == "__main__":
    main()

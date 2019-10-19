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
        payloads = []
        params = [red_params, yellow_params, green_params, blue_params, orange_params, silver_params]
        for param in params:
            try:
                conn = http.client.HTTPSConnection('api.wmata.com')
                conn.request("GET", "/Rail.svc/json/jStations?%s" % param, "{body}", headers)
                response = conn.getresponse()
                data = response.read()
                jsonResponse = json.loads(data.decode('utf-8'))
                stations = jsonResponse.get('Stations')
                for i in stations:
                    lat = i.get('Lat')
                    lon = i.get('Lon')
                    station_name = i.get('Name')
                    payload = [station_name, lat, lon]
                    payloads.append(payload)
                    conn.close()
            except requests.exceptions.HTTPError as e:
                logging.error("HTTP Error:" + str(e))
                return False
        return payloads

def main():
    client = metro_client()
    print(client.build_params())

if __name__ == "__main__":
    main()

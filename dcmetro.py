########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
payload = []
headers = {
    # Request headers
    'api_key': '', #TODOuse bin file next time 
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

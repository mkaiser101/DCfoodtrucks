# from mapbox import Geocoder
# >>> geocoder = Geocoder(access_token="pk.YOUR_ACCESS_TOKEN")
from mapbox import Uploader
service = Uploader()
from time import sleep
from random import randint
mapid = getfixture('uploads_dest_id') # 'uploads-test'
with open('tests/twopoints.geojson', 'rb') as src:
    upload_resp = service.upload(src, mapid)

if upload_resp.status_code == 422:
    for i in range(5):
        sleep(5)
        with open('tests/twopoints.geojson', 'rb') as src:
            upload_resp = service.upload(src, mapid)
        if upload_resp.status_code != 422:
            break


upload_resp.status_code

upload_id = upload_resp.json()['id']
for i in range(5):
    status_resp = service.status(upload_id).json()
    if status_resp['complete']:
        break
    sleep(5)

mapid in status_resp['tileset']
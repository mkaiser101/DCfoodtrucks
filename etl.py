from twitta import twitter_client
from dcmetro import metro_client
#from geojson import Point, Feature, FeatureCollection, dump
import datetime, pickle


def get_twitter_data(TC):
    dataz = []
    topDcfoodtrucks = ["pepebyjose", "ArepaZone", "LobstertruckDC", "dcslices", "DCEmpanadas", "CapMacDC", "bigcheesetruck", "TaKorean", "bbqbusdc", "hulagirltruck", "Borinquenlunchb", "asgharboa", "ThePieTruckDC", "PhoWheels", "tapastruckdc", "ArepaZone", "SloppyMamas"]
    for foodtruck in topDcfoodtrucks:
        payload = TC.get_user_timeline(foodtruck)
        user = payload.get("user").get("name")    
        timestamp = payload.get("created_at")
        tweeted = payload.get("text")
        entites = payload.get("entities")
        post_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #print("text:", tweeted, "at:", timestamp,"by: ", user, "posted at:", post_stamp)
        payload = [post_stamp, user, tweeted, timestamp]
        #v2, maybe change text to predictions or choice, this can be test set though for later so no problem
        
        dataz.append(payload)
    return dataz

def split_metro_station_names(MC):
    '''
    Strip [/, -] from metro data, 
    split stations apart if they don't hit stop word list, 
    add geo coords for unique keywords in split apart stations or match them entriely if not]

    '''
    counter = 0
    counter2 = 0
    words_in_station = []
    metro_data = MC.build_params()
    documents = [sub_list[0] for sub_list in metro_data]
    split_words = [x for xs in documents for x in xs.split('/')]
    split_words2 = [x for xs in split_words for x in xs.split('-')]
    stopwords = ['Road', 'Square', 'South', 'St', 'City', 'Plaza', 'East', 'West', 'Town', 'Boulevard', 'Center']
    for station in split_words2:
        splitted = station.split()        #split words in station so we don't need a full exact match to post 
        print(splitted)
        for word in splitted:
            if word not in stopwords: 
                print ('split:', word)
                for match in split_words2:
                    if word in match:
                        print('matched:', word, match)
                        counter += 1
                    if word not in match:
                        print('did not match:', word, match)
                        counter2 += 1 

                    
            if word in stopwords:
                print ('did not split:', station)
    # resultwords  = [word for word in querywords if word.lower() not in stopwords]   
    # result = ' '.join(resultwords)

    print('matched' , counter, ' did not match ', counter2)


def get_matches(MC, TC):
    metro_data = MC.build_params()
    twitter_data = get_twitter_data(TC)
    geojasonz = []
    
    
    for i in metro_data:
        for j in twitter_data:
            if i[0] in j[2]:
                print(i[1], i[2])
                geojson_appender = {
            "geometry": {
                "type": "Point", 
                "coordinates": [
                    i[1], 
                    i[2]
                ]
            }, 
            "type": "Feature", 
            "properties": {
                "Date": "%s" % (j[3]), 
                "body": "%s" % (j[0]), 
                "Name": "%s" % (j[2])
            }
                }
            #append load's of geojson and then put them inside of template      
            #print(geojson_appender)
            #geojsonload = geojasonz.append(geojson_appender)

    
    # geojson_template = {"type": "FeatureCollection", 
    # "features": ['%s'] % (geojsonload)}
                #geojsonz = geojson_template + geojson_appender
    # print(geojson_template)
            

             
    
                

def build_geojson(match, lat, lon):    # append to shared json of the day

    return True
   
def build_geojson(matches):
    
    point = Point((-115.81, 37.24))

    features = []
    features.append(Feature(geometry=point, properties={"country": "Spain"}))

    # add more features...
    # features.append(...)

    feature_collection = FeatureCollection(features)

    with open('myfile.json', 'w') as f:
        dump(feature_collection, f)



def append_to_pickle(TC):
    try:
        to_pickle_v1 = get_twitter_data(TC)
    except requests.exceptions.HTTPError as e:
        logging.error("HTTP Error:" + str(e))
        return False
    with open('historyoffoodtrucks.pkl', 'rb') as f:
        newlist = pickle.load(f)
        print(newlist)
        print("--------------------------")
        newlist.append(to_pickle_v1)
        print(newlist)
        
    with open('historyoffoodtrucks.pkl', 'wb') as f:
        pickle.dump(newlist, f)

       
    with open('historyoffoodtrucks.pkl', 'rb') as f:
        mynewlist = pickle.load(f)
           
            
        print("--------------------------")

def main():
    TC = twitter_client()
    MC = metro_client()
    #print(get_matches(MC, TC))
    print(append_to_pickle(TC))
    # print(get_twitter_data(TC))
    #print(split_metro_station_names(MC))



if __name__ == "__main__":
    main()

    
    
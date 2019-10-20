from twitta import twitter_client
from dcmetro import metro_client
import datetime, pickle


def get_twitter_data(TC):
    dataz = []
    topDcfoodtrucks = ["pepebyjose", "LobstertruckDC", "dcslices", "DCEmpanadas", "CapMacDC", "bigcheesetruck", "TaKorean", "bbqbusdc", "hulagirltruck", "Borinquenlunchb"]
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

def get_matches(MC, TC):
    metro_data = MC.build_params()
    twitter_data = get_twitter_data(TC)
    for i in metro_data:
        for j in twitter_data:
            if i[0] in j[2]:
                print(i[0])
   




def append_to_pickle(TC):
    try:
        to_pickle_v1 = get_twitter_data(TC)
    except requests.exceptions.HTTPError as e:
        logging.error("HTTP Error:" + str(e))
        return False
    with open('historyoffoodtrucks.pkl', 'rb') as f:
        newlist = pickle.load(f)
        print(newlist)

        newlist.append(to_pickle_v1)
        
    with open('historyoffoodtrucks.pkl', 'wb') as f:
        pickle.dump(newlist, f)

        print("--------------------------")
    with open('historyoffoodtrucks.pkl', 'rb') as f:
        mynewlist = pickle.load(f)
           
            
        print("--------------------------")

def main():
    TC = twitter_client()
    MC = metro_client()
    print(get_matches(MC, TC))
    print(get_twitter_data(TC))



if __name__ == "__main__":
    main()

    
    
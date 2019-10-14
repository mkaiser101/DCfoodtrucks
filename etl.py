from twitta import twitter_client
import datetime, pickle

if __name__ == "__main__":
    
    topDcfoodtrucks = ["pepebyjose", "LobstertruckDC", "dcslices", "DCEmpanadas", "CapMacDC", "bigcheesetruck", "TaKorean", "bbqbusdc", "hulagirltruck", "Borinquenlunchb"]

    client = twitter_client()
    for foodtruck in topDcfoodtrucks:
        payload = client.get_user_timeline(foodtruck)
        user = payload.get("user").get("name")
     
        timestamp = payload.get("created_at")
        tweeted = payload.get("text")
        entites = payload.get("entities")
        print("text:", tweeted, "at:", timestamp,"by: ", user)
        to_pickle_v1 = [user, tweeted, timestamp]

        #append to pickle file for historical data to be used later
        with open('historyoffoodtrucks.pkl', 'rb') as f:
            newlist = pickle.load(f)

        newlist.append(to_pickle_v1)

        with open('historyoffoodtrucks.pkl', 'wb') as f:
            pickle.dump(to_pickle_v1, f)

        print("--------------------------")
        with open('historyoffoodtrucks.pkl', 'rb') as f:
            mynewlist = pickle.load(f)
            print(mynewlist)
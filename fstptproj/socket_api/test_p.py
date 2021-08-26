from InstagramAPI import InstagramAPI
import pickle


if __name__ == "__main__":
    i_api = InstagramAPI("hiphop.movengroove", "7e2525314c25")
    i_api.login()
    print(i_api)
    with open("stored_object.pickle", "wb") as pkl:
        pickle.dump(i_api, pkl)
        
        

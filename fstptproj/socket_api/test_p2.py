from InstagramAPI import InstagramAPI
import pickle


if __name__ == "__main__":
    with open("stored_object.pickle", "rb") as pkl:
        i_api = pickle.load(pkl)
        
    i_api.searchUsername('serj.cool_esh')
    print(i_api.LastJson)

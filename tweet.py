#!/usr/bin/env python
# encoding: utf-8
#Helo I am testing you
import tweepy #https://github.com/tweepy/tweepy
import json
import csv


#Twitter API credentials
consumer_key = "ImoWYbc6SgL9WpHOUBNQCkwty"
consumer_secret = "Hk64ptIQPWk6HyPXA3SWjmPOqjZf2eRSeiO65rfvbvuk0uriis"
access_key = "825406981171142656-QnTYcAOf6vk7Y4haPzRPbqLZhhn0o8M"
access_secret = "REnYRo8z2LxROcdiT98N7ycPbhCuIgYm5C3Ndj1CJLI4y"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    places = api.geo_search(query="United States", granularity="country")
    place_id = places[0].id

    info = api.geo_id(place_id)
    
    #print info

    print("Place id is %s" %(place_id))

    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.search(q='#donaldtrump',lang="en",place="96683cc9126741d1",geocode="39.8,-95.58,5000mi",count=200)
    

    #save most recent tweets
    
#39.8,-95.58
#place:96683cc9126741d1 #donaldtrump OR donaldtrump

    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id -1
    
    #keep grabbing tweets until there are no tweets left to grab
    
    while len(alltweets) < 5000:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        	new_tweets = api.search(q='#donaldtrump',lang="en",place="96683cc9126741d1",geocode="39.8,-95.58,500mi",count=200,max_id=oldest)
        
        #save most recent tweets
        	alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        	oldest = alltweets[-1].id - 1

        	print("...%s tweets downloaded so far" % (len(alltweets)))
    outtweets = [[ tweet.created_at, tweet.id_str, tweet.text.encode("utf-8"),tweet.user.id,tweet.geo,tweet.coordinates,tweet.user.name.encode("utf-8"),tweet.user.location.encode("utf-8"),tweet.place,tweet.user.friends_count,tweet.user.followers_count,tweet.lang.encode("utf-8")] for tweet in alltweets]
       
    #write tweet objects to JSON
    file = open('tweet.json', 'wb') 
    print("Writing tweet objects to JSON please wait...")
    with open('donald_tweets.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["created_at","tweet_id","text","user_id","geo","coordinates","user_name","user_location","place","friend","followers","language"])
        writer.writerows(outtweets)

    pass
    
    #for status in alltweets:
     #   json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    #print "Done"
    file.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("#donaldtrump")

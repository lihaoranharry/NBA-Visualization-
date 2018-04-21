#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import preprocessor as p
import re
import time
#Variables that contains the user credentials to access Twitter API
access_token = "780478082469785601-Em9OdZ3tA01bPwV6GfkU3SLRdfemsbE"
access_token_secret = "9888AimNpnW4dM8QFl1zoUm1tHPRAYvUp9ZMlycHNltkH"
consumer_key = "fqMLvPZqNSViSpl60THKALhYg"
consumer_secret = "dJni0XgoxEci7qcrM2i6hUnuzoZoeaUKfCyANWWQL0vifCpjGI"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            start = data.index("\"text\":\"")
            end = data[start:].index("\",\"") + start
            r = re.compile(r"\\.")

            text = str(data[start+8: end])
            print type(text)
            print text
            text = re.sub(r'[^\x00-\x7F]+', ' ', text)
            print text
            #text = re.sub(r"http\S+", "", text)
            #text =  r.sub(' ', text)

            #print text
            #print p.clean(text)
            
        except:
            pass

        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=[ 'NBA', 'nba'])
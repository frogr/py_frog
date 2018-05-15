from twython import Twython, TwythonStreamer
from py_frog import configuration
import uuid
import time


twitter = Twython(
    configuration.api_consumer_t,
    configuration.api_consumer_s,
    configuration.api_access_t,
    configuration.api_access_s
)


class Stream(TwythonStreamer):
    def on_success(self, tweet):
        if 'text' in tweet:
            if tweet['user']['id'] != configuration.twitter_userID:
                unique_key = uuid.uuid4()
                twitter.update_status(status="key: %s // %s" % (unique_key, tweet['text']))
                print('tweet posted successfully')
                time.sleep(60)

    def on_error(self, status_code, data):
        print(status_code)
        stream.statuses.filter(track='lele')


stream = Stream(
    configuration.api_consumer_t,
    configuration.api_consumer_s,
    configuration.api_access_t,
    configuration.api_access_s
)

stream.statuses.filter(track='lele')


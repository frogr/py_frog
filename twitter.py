from twython import Twython, TwythonStreamer
from py_frog import configuration
import hashlib

uniqueKey = hashlib.md5().hexdigest()

twitter = Twython(
    configuration.api_consumer_t,
    configuration.api_consumer_s,
    configuration.api_access_t,
    configuration.api_access_s
)


class MyStreamer(TwythonStreamer):
    def on_success(self, tweet):
        if 'text' in tweet:
            if tweet['user']['id'] != 996274174959075328:
                twitter.update_status(status="key: %s // %s" % (uniqueKey, tweet['text']))
                print('tweet posted successfully')

    def on_error(self, status_code, data):
        print(status_code)
        stream.statuses.filter(track='lele')


stream = MyStreamer(
    configuration.api_consumer_t,
    configuration.api_consumer_s,
    configuration.api_access_t,
    configuration.api_access_s
)

stream.statuses.filter(track='lele')


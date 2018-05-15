import twitter
from py_frog import configuration
t_api = twitter.Api(
    consumer_key=configuration.api_consumer_t,
    consumer_secret=configuration.api_consumer_s,
    access_token_key=configuration.api_access_t,
    access_token_secret=configuration.api.access_s
)

status = t_api.postUpdate('testing123')
print(status.text)





import tweepy


CONSUMER_TOKEN = 'ct'
CONSUMER_SECRET = 'cs'
ACCESS_TOKEN = 'at'
ACCESS_SECRET = 'as'

TWEET_ID = 560070183650213889

def craete_api():
    auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api


def print_movie_url(status):
    if hasattr(status, 'extended_entities'):
        for media in status.extended_entities.get('media', [{}]):
            if media.get('type', None) == 'video':
                print('video url: ' + media['video_info']['variants'][0]['url'])


def print_using_get_status_api():
    api = craete_api()

    # 何もなしの場合は、textがある
    # print(dir(status))
    # => ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
    #    '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
    #    '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
    #    '__weakref__', '_api', '_json', 'author', 'contributors', 'coordinates', 'created_at', 'destroy', 'entities', 'favorite',
    #    'favorite_count', 'favorited', 'geo', 'id', 'id_str', 'in_reply_to_screen_name', 'in_reply_to_status_id', 
    #    'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'is_quote_status', 'lang', 'parse', 
    #    'parse_list', 'place', 'possibly_sensitive', 'possibly_sensitive_appealable', 'retweet', 'retweet_count', 'retweeted', 
    #    'retweets', 'source', 'source_url', 'text', 'truncated', 'user']
    #
    # tweet_mode='extended'にすると、textがなくなり、full_textになる
    # => ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
    #    '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
    #    '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
    #    '__weakref__', '_api', '_json', 'author', 'contributors', 'coordinates', 'created_at', 'destroy', 'display_text_range', 
    #    'entities', 'extended_entities', 'favorite', 'favorite_count', 'favorited', 'full_text', 'geo', 'id', 'id_str', 
    #    'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 
    #    'in_reply_to_user_id_str', 'is_quote_status', 'lang', 'parse', 'parse_list', 'place', 'possibly_sensitive', 
    #    'possibly_sensitive_appealable', 'retweet', 'retweet_count', 'retweeted', 'retweets', 'source', 'source_url', 
    #    'truncated', 'user']

    # status = api.get_status(TWEET_ID)
    # print(status.text)
    status = api.get_status(TWEET_ID, tweet_mode='extended')
    print(status.full_text)

    print_movie_url(status)


def print_using_user_timeline():
    api = craete_api()
    i = 0
    for status in tweepy.Cursor(api.user_timeline, 
        id='Twitter', since_id=TWEET_ID,
        tweet_mode='extended').items(34):
            print_movie_url(status)
            i += 1
    print(i)


if __name__ == '__main__':
    print_using_get_status_api()
    print_using_user_timeline()
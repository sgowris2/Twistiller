__author__ = 'sudeep'


    # places = api.trends_available()
    # trends = api.trends_place(places[0]['woeid'])[0]['trends']
    # for t in trends:
    #     print t['name']

    # results = api.search('#syria')
    # for r in results:
    #     print r.text

    # user = api.get_user('PujanG')
    # friends = api.friends_ids(id='PujanG')
    # index = 0

    # for f in friends:
    #     timeline = api.user_timeline(id=f)
    #     for tweet in timeline:
    #         if((datetime.datetime.now() -  tweet.created_at).days <= 1):
    #             index = index + 1
    #             print str(index) + '. ' + tweet.text + '\n'

    # timeline = api.user_timeline('uday13')
    # for tweet in timeline:
    #     if((datetime.datetime.now() -  tweet.created_at).days <= 1):
    #         print tweet.text

    # for friend in user.friends():
    #     print friend.screen_name

    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print tweet.text
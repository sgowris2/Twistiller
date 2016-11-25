__author__ = 'sudeep'

import tweepy


def connect():

    auth = tweepy.OAuthHandler('uY0bjGMLRsMW4vBKteNBqn6T6', 'BihJSK12QF7veaK6LOhsxAcn1XT6WlvlXue024hBygIS4mxWyx')
    auth.set_access_token('341713269-VMqPoaYzh73uTenjo6Mo4Ll65hPh922PRACI5eND',
                          'wshrFyofpRRqiNhnsstFBiIo0Q7KImmMObN3fSkkrPWs0')
    return tweepy.API(auth)
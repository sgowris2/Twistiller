__author__ = 'sudeep'

import datetime
import time


def run_streamer(api):

    index = 0
    topic = '#WIvIND'

    print '\n\nStarting stream on ' + topic + '...\n\n\n'
    print 'PRESS Ctrl-C to stop stream\n\n'

    new_search = 0
    min_id = 0
    results = api.search(q=topic, lang='en', count=15, result_type='mixed')

    while (True):

        if new_search == 1:
            results = api.search(q=topic, lang='en', count=15, result_type='mixed', max_id=min_id)
            index = 0
            new_search = 0

        if (len(results) > index):
            try:
                if(results[index].id < min_id or min_id == 0):
                    min_id = results[index].id
                if(results[index].entities['media'][0]['type']=='photo'):
                    print '[' + str(datetime.datetime.now()) + '] - @' + results[index].user.screen_name + \
                          ' tweeted: \n'+ results[index].text.replace('\n\n', '\n'),
                    if (results[index].coordinates is not None):
                        print '\nfrom ' + results[index].coordinates + '\n\n'
                    else:
                        print '\n\n'
                    time.sleep(1)
            except:
                pass
            index += 1
        else:
            new_search = 1
from BM import *
from KMP import *
from Regex import *
from Tweet import *
from AvailableChar import *
from flask import Flask
from flask import Flask
from flask import redirect, url_for, request, render_template
import json

app = Flask(__name__)
api = Tweet('credentials.json')

@app.route('/KMP', methods=['GET', 'POST'])
def doKMP() :
    data = request.form['hasil']
    data = json.JSONDecoder().decode(data)
    pattern = KMP(data['spam_indicator'])
    search_type = data['search_type']
    tweets = dict()
    if(search_type == "1") :
        username = data['username']
        count = data['count']
        tweets = api.search_timeline(username, count)
    else :
        region = data['region']
        count = data['count']
        tweets = api.search_region(region, count)

    is_spam = []
    for tweet in tweets['full_text'] :
        is_spam.append(pattern.is_match(tweet))
    
    tweets['is_spam'] = is_spam

    return json.dumps(tweets)
    

@app.route('/BM', methods=['GET', 'POST'])
def doBM() :
    data = request.form['hasil']
    data = json.JSONDecoder().decode(data)
    pattern = BM(data['spam_indicator'])
    search_type = data['search_type']
    tweets = dict()
    if(search_type == "1") :
        username = data['username']
        count = data['count']
        tweets = api.search_timeline(username, count)
    else :
        region = data['region']
        count = data['count']
        tweets = api.search_region(region, count)

    is_spam = []
    for tweet in tweets['full_text'] :
        is_spam.append(pattern.is_match(tweet))
    
    tweets['is_spam'] = is_spam

    return json.dumps(tweets)

@app.route('/Regex', methods=['GET', 'POST'])
def doRegex() :
    
    data = request.form['hasil']
    data = json.JSONDecoder().decode(data)
    pattern = Regex(data['spam_indicator'])
    search_type = data['search_type']
    tweets = dict()
    if(search_type == "1") :
        username = data['username']
        count = data['count']
        tweets = api.search_timeline(username, count)
    else :
        region = data['region']
        count = data['count']
        tweets = api.search_region(region, count)

    is_spam = []
    for tweet in tweets['full_text'] :
        is_spam.append(pattern.is_match(tweet))
    
    tweets['is_spam'] = is_spam

    return json.dumps(tweets)


if __name__ == '__main__':
    app.debug = True
    app.run()
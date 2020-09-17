from flask import Flask, jsonify, request
import wikipedia

app = Flask(__name )
app.url_map.strict _slashes = False

def get wiki data(search query):
got_query = (wikipedia.search(search query)[0])
page = wikipedia.page(got query)
title = page.title
wiki url = page.url
summary = (wikipedia.summary(got query, sentences=1))
return title,wiki_url,summary

@app.route('/')
def index(): I
return "API is UP and working fine"

@app.route('/<query>")
def home(query):
title, url, summary = get wiki data(query)
return jsonify({"query":query,“"title":title, "wiki url”:url, "summary":summary})

if _name_ == ' main_':
app.debug=True
app.run(host='0.0.0.0"',port=5000)

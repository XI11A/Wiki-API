from flask import Flask, jsonify, request
import wikipedia

app = Flask(__name__)
app.url_map.strict_slashes = False

def get_wiki_data(search_query):
    got_query = (wikipedia.search(search_query)[0])
    page = wikipedia.page(got_query)
    title = page.title
    wiki_url = page.url
    summary = (wikipedia.summary(got_query, sentences=1))
    return title,wiki_url,summary

@app.route('/')
def index():
    return "API is UP and working fine"

@app.route('/<query>')
def home(query):
    title, url, summary = get_wiki_data(query)
    return jsonify({"query":query,"title":title,"wiki_url":url,"summary":summary})

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)        

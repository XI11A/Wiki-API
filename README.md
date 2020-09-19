# Wiki API
An Simple Wikipedia API Build with Flask &amp; Python to get Wiki data in form of JSON Format

### Show some :heart: and :star: the repo to support the project

[![GitHub stars](https://img.shields.io/github/stars/XI11A/wiki-api.svg?style=social&label=Star)](https://github.com/XI11A/wiki-api) ![GitHub followers](https://img.shields.io/github/followers/xi11a.svg?style=social&label=Follow)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

#### Wiki API written in Python using Flask  

 ---
###### **NOTE:** You don't need to have Wikipedia link of the article in order to fetch the article details, you can directly search wiki by the query. 
 ---

### **Features**:
##### Currently the API can get the following details for a specific query in JSON format:
- **Query Name**
- **Query Summary**
- **Wiki URL**


```json
{
"query":"google",
"summary":"Google, LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware.",
"title":"Google",
"wiki_url":"https://en.wikipedia.org/wiki/Google"
}
```

### **Installation**:

Clone this repository using
```sh
$ git clone https://github.com/XI11A/wiki-api
```
Enter the directory and install all the requirements using
```sh
$ pip3 install -r requirements.txt
```
Run the app using
```sh
$ python3 app.py
```
Navigate to 127.0.0.1:5000 to see the Homepage

### **Usage**:

---
##### **Universal Endpoint**: (Supports Query)
```sh
http://127.0.0.1:5000/api?query=<insert_your_query>
```
**Example:** Navigate to https://wiki.nivash.me/api?query=google to get a JSON response of wiki data in return.

----

#### You can fork the repo and deploy on VPS or deploy it on Heroku :)  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/XI11A/wiki-api/tree/master)

**Note:** Heroku gives US/Europe servers which won't be able to fetch all Query flawlessly. Use any Indian VPS for accurate results.

---

#### Star the Repo in case you liked it :)

### © [Nivash](https://xi11a.github.io)

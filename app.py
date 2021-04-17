from flask import Flask, render_template, request, url_for, redirect, send_file, session
import snscrape.modules.twitter as twitter
import csv 
import os 

def userTweets_CSV(username='Projects_007'):
    with open('Projects_007.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i, tweet in enumerate(twitter.TwitterSearchScraper('from:' +username+ ' since:2020-11-01 until:2021-01-01 ').get_items()):
            writer.writerow([tweet.user.username, tweet.content.encode("utf-8"), tweet.date, tweet.url])
       

app = Flask(__name__)
app.config['SECRET_KEY'] = "DemoString"


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        userTweets_CSV(session['username'])
        return send_file(os.path.abspath('Projects_007.csv'), as_attachment=True)
    
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)

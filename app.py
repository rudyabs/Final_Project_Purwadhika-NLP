from flask import Flask, redirect, url_for, render_template, request, abort
import joblib
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import io
import base64

matplotlib.use('agg')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/sms', methods=['GET','POST'])
def spam():
    if request.method == 'GET':
        return render_template('sms.html', title='SMS')
    elif request.method == 'POST':
        isi_sms = request.form['sms']
        result = model_spam.predict([isi_sms])
        if result == [0]:
            result = "SMS Normal"
        elif result == [1]:
            result = "SMS Spam"
        else:
            result = "SMS Promo"
        print(result)
        return render_template('hasil_sms.html', result=result, title="Hasil SMS")
    else:
        abort(404)

@app.route('/tweet', methods=['GET','POST'])
def emosi():
    if request.method == 'GET':
        return render_template('tweet.html',title='Tweet')
    elif request.method == 'POST':
        isi_tweet = request.form['tweet']
        result = model_twitter.predict([isi_tweet])
        result = result[0]
        probability_tweet = model_twitter.predict_proba([isi_tweet])
        probability_tweet = probability_tweet[0]
        labels = ['anger','fear','happiness','love','sad']

        # visualisasi - pie chart
        plt.close()
        plt.figure(figsize=(5,5))
        plt.title('Hasil analisa tweet')
        plt.pie(x=probability_tweet, autopct='%1.1f%%', pctdistance=1.1, labeldistance=1.3, labels=labels)
        plt.tight_layout()

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        graph = 'data:image/png;base64,{}'.format(graph_url)

        return render_template("hasil_tweet.html", result=result, title="Hasil Tweet", graph=graph)
    else:
        abort(404)

if __name__ == "__main__":
    model_spam = joblib.load('model_sgdc_spam')
    model_twitter = joblib.load('model_multinomial_twitter') 
    app.run(debug=True)
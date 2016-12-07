"""
Simple "Hello, World" application using Flask
"""
from model import InputForm
from flask import Flask, render_template, request, redirect, url_for
from oscar_winner import *

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/',methods=['GET','POST'])
def find_winner():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        year = form.Year.data
        award = form.Award.data
        if award == 'actor':
            result = Oscar_Best_Actor(year)
        elif award == 'actress':
            result = Oscar_Best_Actress(year)
        elif award == 'supporting actor':
            result = Oscar_Best_Supporting_Actor(year)
        elif award == 'supporting actress':
            result = Oscar_Best_Supporting_Actress(year)
        elif award == 'director':
            result = Oscar_Best_Director(year)
        elif award == 'animated feature':
            result = Oscar_Best_Animated_Feature(year)
        elif award == 'picture':
            result = Oscar_Best_Picture(year)
        elif award == 'original song':
            result = Oscar_Best_Original_Song(year)
        elif award == 'original score':
            result = Oscar_Best_Original_Song(year)
        elif award == 'visual effects':
            result = Oscar_Best_Visual_Effects(year)
        elif award == 'original screenplay':
            result = Oscar_Best_Original_Screenplay(year)
        elif award == 'adapted screenplay':
            result = Oscar_Best_Adapted_Screenplay(year)
        else:
            result = "The award you are seeking is not available."
        print(year)
        return render_template('results.htm', award = award, year = year, result = result)
    return render_template('home.htm', form = form)


if __name__ == '__main__':
    app.run(host ='127.0.0.1', port=5000)

from flask import Flask, render_template, session, redirect, request, url_for, make_response
import os
from chat_bot.NN import get

IMG_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['IMG_FOLDER'] = IMG_FOLDER


@app.route('/', methods=["GET"])
def homePage():
    return render_template("index.html")
@app.route('/farfadetoriginal.html', methods=["GET"])
def farfadetOriginalPage():
    return render_template("farfadetoriginal.html")

@app.route('/smurf.html', methods=["GET"])
def smurfPage():
    return render_template("smurf.html")


@app.route('/romain.html', methods=["GET"])
def romainPage():
    return render_template("romain.html")

@app.route('/chat_bot.html', methods=["GET", "POST"])
def show_chat_bot():
    output = ''
    logo_alt = "Logo"
    box_color = "#ee5253"
    music_src = "https://cdn.discordapp.com/attachments/1230496653220380674/1231383880800403528/song.mp3?ex=66259f1b&is=66244d9b&hm=ac5335be89102cf0ea5f634ad2bf0f1e43737b5e83376b2375172c835df2c2b6&"

    if request.method == 'POST':
        statut = request.cookies.get('cookie_miams')
        print(f'Cookie: {statut}')
        input_value = request.form['input_name']
        print(f'You entered: {input_value}')
        output = get(input_value)
        if input_value == "césar" or input_value == "cesar":
            output ="asiatique"

        if input_value == "封對専尃宾寛宾寑寎寗寏":
            output = "Décalage"

        if input_value == "morse" or input_value == "malice":
            output = "Bait"

        if input_value == "Farfadet" or input_value == "farfadet":
            output = "Colo"


        # Mise à jour de l'image et de la musique si la sortie contient "code est 8135"

        if statut != 'sorcier' and 'code' in output:
            output = "Que fais tu ici? Tu n'as pas le droit d'être ici!"
            logo_alt = "Logo"
            box_color = "#ee5253"
            music_src="https://cdn.discordapp.com/attachments/1230496653220380674/1231383880800403528/song.mp3?ex=66259f1b&is=66244d9b&hm=ac5335be89102cf0ea5f634ad2bf0f1e43737b5e83376b2375172c835df2c2b6&"
        if statut == 'sorcier' and 'code est 8135 ' in output:
            logo_alt = "code=1989"
            box_color = "#1dd1a1"
            music_src = "https://cdn.discordapp.com/attachments/1230496653220380674/1231417286179553301/FREE_FOR_PROFIT_GOOFY_AHH_TYPE_BEAT.mp3?ex=6636e1b7&is=66246cb7&hm=8dbed31db19c7eec1a8467808c64b9bf3dbb6954499ef739ed2815a25df8d9f1&"

        return render_template('chat_bot.html', output=output, logo_alt=logo_alt, music_src=music_src, box_color=box_color)

    if request.method == 'GET':
        response = make_response(render_template('chat_bot.html', logo_alt=logo_alt, music_src=music_src, box_color=box_color))
        response.set_cookie('cookie_miams', 'moldu')
        return response


if __name__ == "__main__":
    app.run(debug=False)

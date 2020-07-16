from flask import Flask, render_template, request, redirect, url_for, Response
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dmlab62296'
app.config['MYSQL_DATABASE_DB'] = 'music'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)
# 連接資料庫
connect = mysql.connect()
cursor = connect.cursor()


@app.route("/cloud/<search_list>", methods=['GET', 'POST'])
def cloud(search_list):
    return render_template("cloud.html", search_list=search_list)


@app.route("/bar/<search_list>", methods=['GET', 'POST'])
def bar(search_list):
    return render_template("bar.html", search_list=search_list)


@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        singer_name = request.form.get('singer_name')
        album_name = request.form.get('album_name')
        song_name = request.form.get('song_name')
        author_name = request.form.get('author_name')
        composer_name = request.form.get('composer_name')
        album_language = request.form.get('album_language')
        search_list1=[singer_name,album_name,song_name,author_name,composer_name,album_language]
        search_list=','.join(search_list1)
        return redirect(url_for('result', search_list=search_list))

    return render_template("index.html")


@app.route("/result/<search_list>", methods=['GET', 'POST'])
def result(search_list):
    print('print', 'search_list', search_list)
    search_list=search_list.split(',')
    singer_name = search_list[0]
    album_name = search_list[1]
    song_name = search_list[2]
    author_name = search_list[3]
    composer_name = search_list[4]
    album_language = search_list[5]
    print('singer_name',singer_name)
    cursor . execute(
        "SELECT singer_name,class,album_name,song_name,years,album_language,author_name,composer_name,id FROM  Excel21  WHERE singer_name like '%{}%'  ".format(singer_name))
    data1 = cursor.fetchall()
    len_data1 = len(data1)
    return render_template("result.html", data1=data1, search_list=search_list, len_data1=len_data1)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.run(debug=True)

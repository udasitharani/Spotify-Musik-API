from app import app
from flask import request
import spotify_crawl
import json

@app.route('/')
def index():
    return "Everything will be fine."

@app.route('/new-releases', methods=['GET', 'POST'])
def new_releases():
    if(request.method=='GET'):
        count = 1
    elif(request.method=='POST'):
        count = request.form['count']
    else:
        return "INVALID REQUEST METHOD"
    data = spotify_crawl.new_releases(count)
    json_data = json.dumps(data)
    response = app.response_class(
        response = json_data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/featured-playlists', methods=['GET', 'POST'])
def  featured_playlists():
    if(request.method=='GET'):
        count = 1
        language='hi'
    elif(request.method=='POST'):
        count = request.form['count']
        language = request.form['language']
        if(language not in ['hi', 'en']):
            language = 'hi'
    else:
        return "INVALID REQUEST METHOD"
    data = spotify_crawl.featured_playlists(count, language)
    json_data = json.dumps(data)
    response = app.response_class(
        response = json_data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/artist', methods=['GET'])
def artist():
    if(request.method=='GET'):
        id = '5kiwICyQNDmCtwOPLvgY04'
    elif(request.method=='POST'):
        id = request.form['id']
    else:
        return "INVALID REQUEST METHOD"
    data = spotify_crawl.get_artist(id)
    json_data = json.dumps(data)
    response = app.response_class(
        response = json_data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/artist/tracks', methods=['GET'])
def artist_songs():
    if(request.method=='GET'):
        id = '5kiwICyQNDmCtwOPLvgY04'
    elif(request.method=='POST'):
        id = request.form['id']
    else:
        return "INVALID REQUEST METHOD"
    data = spotify_crawl.get_artist_songs(id)
    json_data = json.dumps(data)
    response = app.response_class(
        response = json_data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/artist/albums', methods=['GET', 'POST'])
def artist_albums():
    if(request.method=='GET'):
        id = '5kiwICyQNDmCtwOPLvgY04'
        count = 10
    elif(request.method=='POST'):
        id = request.form['id']
        count = request.form['count']
    else:
        return "INVALID REQUEST METHOD"
    data = spotify_crawl.get_artist_albums(id, count)
    json_data = json.dumps(data)
    response = app.response_class(
        response = json_data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/search/tracks', methods=['GET', 'POST'])
def search_tracks():
    if(request.method=='GET'):
        keyword = 'Mila hai jabse tu'
        count = 1
    elif(request.method=='POST'):
        keyword = request.form['keyword']
        count = request.form['count']
    else:
        return "INVALID REQUEST METHOD"
    data = spotify_crawl.search_tracks(keyword, count)
    json_data = json.dumps(data)
    response = app.response_class(
        response = json_data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/search/albums', methods=['POST', 'GET'])
def search_albums():
    if(request.method=='GET'):
        keyword = 'Mila hai jabse tu'
        count = 1
    elif(request.method=='POST'):
        keyword = request.form['keyword']
        count = request.form['count']
    else:
        return "INVALID REQUEST METHOD"
    data = spotify_crawl.search_albums(keyword, count)
    json_data = json.dumps(data)
    response = app.response_class(
        response = json_data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/search/playlists')
def search_playlists():
    if(request.method=='GET'):
        keyword = 'Mila hai jabse tu'
        count = 1
    elif(request.method=='POST'):
        keyword = request.form['keyword']
        count = request.form['count']
    else:
        return "INVALID REQUEST METHOD"
    data = spotify_crawl.search_playlists(keyword, count)
    json_data = json.dumps(data)
    response = app.response_class(
        response = json_data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/search/artists')
def search_artists():
    if(request.method=='GET'):
        keyword = 'Mila hai jabse tu'
        count = 1
    elif(request.method=='POST'):
        keyword = request.form['keyword']
        count = request.form['count']
    else:
        return "INVALID REQUEST METHOD"
    data = spotify_crawl.search_artists(keyword, count)
    json_data = json.dumps(data)
    response = app.response_class(
        response = json_data,
        status=200,
        mimetype='application/json'
    )
    return response
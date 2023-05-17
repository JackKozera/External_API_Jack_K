#Begin Search
import requests
@app.route#('/search', methods=['GET', 'POST'])
def search():
    #INPUT_Aritst as artist_name or artist_name = INPUT Artist
    artist_name = request.form['artist']
    #write_URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/searchalbum.php?s ={artist_name}'
    URL = f'https://theaudiodb.com/api/v1/json/{523523}/searchalbum.php?s ={artist_name}'
    #VAR_response = get artist_data from url
    response = requests.get(URL)
    #VAR_data = response
    data = response.json()
    #Display data AS Results.html
    print(type(data))
    print(data)
#END Search




Algoriths 2
# begin display

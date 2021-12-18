import requests
from flask import Flask,request, render_template, jsonify, Response



base_url="https://rickandmortyapi.com/api/"
character_url=base_url+"character/"
location_url=base_url+"location/"
episode_url=base_url+"episode/"

app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True

class Character():
    def get_all_pages(self):
        print("Loading Pages of Riki and Morty")
        results = []
        pages = requests.get(character_url).json().get('info').get('pages')
        for number in range(1, pages, 1):
            get_character_url = character_url + '?page=' + str(number)
            data = requests.get(get_character_url).json()
            next = data['info']['next']
            if next != '':
                res = requests.get(get_character_url).json()
                get_character_url = next
                for id in range(len(res.get('results'))):
                    results.append(res.get('results')[id])

        return results

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html',
            title = 'Riki and Martin Page',
            body = "Welcome to Rick and Morty Search API"
            )

@app.route('/api/character/<type>', methods=['GET'])
def character(type):
    data = []
    for id in character_data:
        if id['status'] == 'Alive' and id['species'] == 'Human' and 'Earth' in id['origin']['name']:
            data.append({ 'name': id['name'], 'location': id['location']['name'], 'image': id['image']})

    if type != "json":
        return render_template('character_table.html',title = 'Riki and Martin Page', characters=data)
    else:
        return jsonify(data)

@app.route('/health/')
def health():
    return {'message': 'Healthy'}

@app.route('/download', methods=['GET'])
def download_csv_data():
    data = []
    csv_headers = "name,location,image\n"
    data.append(csv_headers)
    for id in character_data:
        if id['status'] == 'Alive' and id['species'] == 'Human' and 'Earth' in id['origin']['name']:
            cdata = f"{id.get('name')},{id.get('location').get('name')},{id.get('origin').get('name')}\n"
            data.append(cdata)
    return Response(data, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=riki_martin_data.csv"})

@app.route('/about')
def about():
    return 'About page'

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    c = Character()
    character_data = c.get_all_pages()
    app.run()

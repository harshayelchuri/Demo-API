import requests

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)



app.config['MONGO_DBNAME'] = 'weatherdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/weatherdb'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_all_data():
  object = mongo.db.objects
  output = []
  for s in object.find():
    output.append({'_id':s['_id'], 'temperature':s['temperature'],'wind_speed':s['wind_speed'],'description':s['description']})
  return jsonify({'result' : output})


@app.route('/', methods=['POST'])
def add_object():
  object = mongo.db.objects
  lattitude = request.json['lattitude']
  longitude = request.json['longitude']
  url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=****************************&units=metric'.format(lattitude, longitude)
  res = requests.get(url)
  data = res.json()
  temperature = data['main']['temp']
  wind_speed = data['wind']['speed']
  description = data['weather'][0]['description']

  object_id = object.insert({'_id':{'lattitude': lattitude, 'longitude': longitude},'temperature':temperature,'wind_speed':wind_speed,'description':description})
  new_object = object.find_one({'_id': object_id })
  output = {'_id':new_object['_id'],'temperature':new_object['temperature'],'wind_speed':new_object['wind_speed'],'description':new_object['description']}
  return jsonify({'result' : output})



if __name__ == '__main__':
    app.run(debug=True)

# Demo-API

GET: http://127.0.0.1:5000/
output: http://127.0.0.1:5000/
{
  "result": [
    {
      "_id": {
        "lattitude": 12.9716, 
        "longitude": 77.5946
      }, 
      "description": "light rain", 
      "temperature": 24.85, 
      "wind_speed": 2.57
    }
  ]
}

POST : http://127.0.0.1:5000/
body:
{
    "lattitude":31.14,
    "longitude":35.1
}
output:
{
  "result": {
    "_id": {
      "lattitude": 31.14, 
      "longitude": 35.1
    }, 
    "description": "overcast clouds", 
    "temperature": 23.92, 
    "wind_speed": 2.91
  }
}

GET: http://127.0.0.1:5000/
output:
{
  "result": [
    {
      "_id": {
        "lattitude": 12.9716, 
        "longitude": 77.5946
      }, 
      "description": "light rain", 
      "temperature": 24.85, 
      "wind_speed": 2.57
    }, 
    {
      "_id": {
        "lattitude": 31.14, 
        "longitude": 35.1
      }, 
      "description": "overcast clouds", 
      "temperature": 23.92, 
      "wind_speed": 2.91
    }
  ]
}

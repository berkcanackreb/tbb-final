from typing import List, Dict
from flask import Flask
from flask import jsonify
import mysql.connector
import json
import os

app = Flask(__name__)


def buyuk_sehirler() -> List[Dict]:
        
    connection = mysql.connector.connect(
        user = os.getenv('MYSQL_USERNAME'),
        password = os.getenv('MYSQL_PASSWORD'),
        host = os.getenv('MYSQL_PORT_3306_TCP_ADDR'),
        port = os.getenv('MYSQL_PORT_3306_TCP_PORT'),
        database = os.getenv('MYSQL_INSTANCE_NAME')       
    )    
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM buyuk_sehirler')
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results

healtcheck = {
    "health": [
    {
       "status":"{ok}",  
    }
  ]  
}
@app.route('/')
def index() -> str:
    return json.dumps({'buyuk_sehirler': buyuk_sehirler()})

@app.route('/healtcheck')
def run2():
    return jsonify(healtcheck)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
    app.run2(host='0.0.0.0',port=5001)


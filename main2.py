# NGROK
# HEROCU
# PYTHONANYWHERE
# PYTHON RAILWAY
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask приветствует Вас'

if __name__ == '__main__':  # выясняем порт, получаем его через целое число
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



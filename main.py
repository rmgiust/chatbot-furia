# main.py
from app import create_app
import time

app = create_app()

@app.before_request
def adicionar_delay():
    time.sleep(0.8)  # Simula um pequeno tempo de "raciocínio" do bot

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

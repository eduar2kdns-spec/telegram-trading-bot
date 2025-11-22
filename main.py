import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = "8599012550:AAFu3TBtl2kKPmYqYxoteB8G82ZN34bzo4o"
CHAT_ID = "-1003294489596"

def send_msg(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json or {}

    signal = data.get("type", "Unknown")
    pair = data.get("pair", "Unknown")
    tf = data.get("timeframe", "Unknown")

    text = f"""
📊 <b>SEÑAL DE TRADING</b>

🔹 Par: <b>{pair}</b>
🔹 Temporalidad: <b>{tf}</b>
🔹 Señal: <b>{signal}</b>

Sistema: EMA200 + RSI + Distancia
    """

    send_msg(text)
    return jsonify({"status": "ok"}), 200

@app.route('/', methods=['GET'])
def home():
    return "Bot corriendo correctamente."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
  

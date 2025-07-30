from flask import Flask, request, jsonify

app = Flask(__name__)

# Phishing detection logic
suspicious_keywords = ['login', 'verify', 'update', 'free', 'bonus', 'account', 'bank', 'secure', 'password', 'win']

def detect_phishing(url):
    score = 0
    if len(url) > 75:
        score += 1
    if '@' in url:
        score += 1
    if url.count('//') > 1:
        score += 1
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            score += 1
    if not url.startswith("https"):
        score += 1
    return "Phishing URL Detected" if score >= 3 else "Safe URL"

# API route
@app.route("/check", methods=["POST"])
def check():
    data = request.json
    url = data.get("url", "")
    result = detect_phishing(url)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)

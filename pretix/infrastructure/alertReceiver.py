from flask import Flask, request
import yaml


app = Flask(__name__)

@app.route('/service', methods=["POST"])
def receiveServiceIP():
    print(request.data)
    return ''

@app.route('/alert', methods=["POST"])
def receiveAlert():
    print(request.data)
    return ''

if __name__ == "__main__":
    prometheus=yaml.safe_load(open("prometheus.yml","r"))
    print(prometheus["scrape_configs"])
    app.run(host='0.0.0.0', port=9999)
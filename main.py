import speedtest  # Import o speedtest module
from flask import Flask, jsonify  # Import o Flask module

app = Flask(__name__)  # Create um novo Flask app

test = speedtest.Speedtest()  # Create um novo speedtest object

@app.route('/download')  # route de download
def download():
    download_speed = test.download()  # Get o download speed
    downloadMB = download_speed / (10**6)  # Convert o download speed para megabytes
    return jsonify({'Menssagem': {'download_speed': f"{downloadMB:.2f}Mb"}})  # Return o download speed em megabytes com 2 casas decimais

@app.route('/upload')  # route de upload
def upload():
    upload_speed = test.upload()  # Get o upload speed
    uploadMB = upload_speed / (10**6)   # Convert o upload speed para megabytes
    return jsonify({'Menssagem': {'upload_speed': f"{uploadMB:.2f}Mb"}}) # Return o upload speed em megabytes com 2 casas decimais

@app.route('/ping')  # route de ping
def ping():
    ping = test.results.ping  # Get o ping
    return jsonify({'Menssagem': {'ping': ping}})

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
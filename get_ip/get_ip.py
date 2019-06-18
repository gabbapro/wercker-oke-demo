import json
import argparse

from bottle import Bottle, run, request

app = Bottle()

# Hi Mum!

@app.route('/')
def get_ip():
    client_ip = request.environ.get('REMOTE_ADDR')
    return json.dumps({"Hello! IP Address": client_ip}, indent=4, separators=(',', ': '))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="HTTP API for returning a visitor's IP address.")

    parser.add_argument('hostname', default="0.0.0.0",
                        help='The host IP to listen on. ')

    parser.add_argument('port', default="8080", help='The port to listen on.')

    args = parser.parse_args()

    run(app, host=args.hostname, port=args.port)

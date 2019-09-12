"""
Webhook listener example, for a generic Bot.
"""
import argparse
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Listen for webhook')
    parser.add_argument('host', nargs='?', type=str, default='127.0.0.1')
    parser.add_argument('port', nargs='?', type=str, default='3000')
    parser.add_argument('intents_path', nargs='?', type=str, default='data/intents.md')
    parser.add_argument('stories_path', nargs='?', type=str, default='data/stories.md')
    parser.add_argument('domain_path', nargs='?', type=str, default='domain.yml')
    parser.add_argument('--debug', action='store_true')

    args = parser.parse_args()

 
    @app.route('/', methods=['POST'])
    def listen():
        data = request.json
        print(f'Updating {data["type"]} file')
        
        try:
            response = requests.get(data['file'])
            data = response.json()

            global args
            
            file_path = getattr(args, data['type'] + '_path')
            with open(file_path, 'w') as f:
                f.write(data['content'])    
        
            return jsonify({})  

        except Exception as e:
            print(f'Error trying to update file {e}')
            return jsonify({})  


    app.run(host=args.host, port=args.port, debug=args.debug)

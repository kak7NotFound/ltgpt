from flask import render_template, send_file, redirect, send_from_directory, request, jsonify
from time import time
from os import urandom
import tiktoken

class Website:
    def __init__(self, app) -> None:
        self.app = app
        self.routes = {
            '/': {
                'function': lambda: redirect('/chat'),
                'methods': ['GET', 'POST']
            },
            '/chat/': {
                'function': self._index,
                'methods': ['GET', 'POST']
            },
            '/chat/<conversation_id>': {
                'function': self._chat,
                'methods': ['GET', 'POST']
            },
            '/assets/<folder>/<file>': {
                'function': self._assets,
                'methods': ['GET', 'POST']
            }
        }
        @app.route('/files/<path:filename>')
        def serve_file(filename):
            return send_from_directory('files', filename)
        
        @app.route('/count_tokens', methods=['POST'])
        def count_tokens():
            # TODO Доделать
            data = request.get_json()
            text = data['text']
            token_count = 1
            return jsonify({'token_count': token_count})

    def _chat(self, conversation_id):
        if not '-' in conversation_id:
            return redirect(f'/chat')

        return render_template('index.html', chat_id=conversation_id)

    def _index(self):
        return render_template('index.html', chat_id=f'{urandom(4).hex()}-{urandom(2).hex()}-{urandom(2).hex()}-{urandom(2).hex()}-{hex(int(time() * 1000))[2:]}')

    def _assets(self, folder: str, file: str):
        try:
            return send_file(f"./../client/{folder}/{file}", as_attachment=False)
        except:
            return "File not found", 404
            


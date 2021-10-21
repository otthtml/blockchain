'''
Implement ServerInterface using Flask's library.
'''

from flask import Flask, jsonify

from server_interface import ServerInterface


class FlaskAdapter(ServerInterface):
    '''
    Class that implements ServerInterface using Flask
    '''

    def start_server(self):
        '''initialize flask'''
        return Flask(__name__)

    def json_response(self, response):
        '''jsonify dictionary to web formats'''
        return jsonify(response)

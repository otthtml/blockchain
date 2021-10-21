'''
Implement ServerInterface using Flask's library.
'''

from flask import Flask

from server_interface import ServerInterface


class FlaskAdapter(ServerInterface):
    '''
    Class that implements ServerInterface using Flask
    '''

    def start_server(self):
        return Flask(__name__)

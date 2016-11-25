__author__ = 'sudeep'

from api_interface import connect
from streamer import run_streamer

api = connect()
run_streamer(api)
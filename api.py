from lib.bottle import Bottle, request
import logging

bottle = Bottle()


@bottle.route('/')
def index():
    return "Hello world!"


@bottle.route('/post', method="POST")
def post():
    all_content = request.forms.get('allOutput')
    logging.info("All Content")
    logging.info(all_content)
    return "Thanks"


@bottle.route('/stats')
def stats():
    return "Nothing to see here"

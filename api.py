from lib.bottle import Bottle

bottle = Bottle()


@bottle.route('/')
def index():
    return "Hello world!"

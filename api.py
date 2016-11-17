from lib.bottle import Bottle, request
import logging
from dal import DAL

bottle = Bottle()


@bottle.route('/')
def index():
    return "Hello world!"


@bottle.route('/post', method="POST")
def post():
    all_content_key = "all_output"
    all_content = request.forms.get(all_content_key)
    logging.info("All Content")
    logging.info(all_content)

    add_data = {}
    if all_content:
        add_data = {
            "content" : all_content
        }

    ins_status = DAL.insert_test_data(**add_data)

    # The return message is just for viewing in circleci
    return "Added test data!" if ins_status else "Failed adding test data!"


@bottle.route('/stats')
def stats():
    test_data = DAL.get_latest_test_data()
    logging.info("Got return val")
    # Some kind of cleansing is required here
    return str(test_data)

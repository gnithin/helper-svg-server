from lib.bottle import Bottle, request
import logging
from dal import DAL
from utils import Utils

bottle = Bottle()


@bottle.route('/')
def index():
    return "Hello world!"


@bottle.route('/post', method="POST")
def post():
    all_content_key = "allOutput"
    all_content = request.forms.get(all_content_key)
    logging.info("All Content")
    logging.info(all_content)

    add_data = {}
    if all_content:
        add_data = {
            "content" : all_content
        }

    # The return message is just for viewing in circleci
    return Utils.resp_json(
        *(
            [1, "Added test data!"] if DAL.insert_test_data(**add_data)
            else [-1, "Failed adding test data!"]
        )
    )


@bottle.route('/stats')
def stats():
    test_data = DAL.get_latest_test_data()
    if not test_data:
        return Utils.resp_json(-1, "No data available")

    try:
        content = test_data.content
        timestamp = test_data.timestamp

        # TODO: This needs to be removed from here
        final_content = Utils.parse_content(content, timestamp)
    except Exception as e:
        logging.info(str(e))

    # Some kind of cleansing is required here
    return Utils.resp_json(1, "success", contents=final_content)

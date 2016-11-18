from google.appengine.ext import ndb
import logging
from utils import Utils
import json


class TestData(ndb.Model):
    content = ndb.TextProperty()
    # Contains a JSON dump of the parsed content
    structured_content = ndb.TextProperty()
    test_timestamp = ndb.StringProperty()
    db_timestamp = ndb.DateTimeProperty(auto_now_add=True)

    # TODO: Should I store the parsed messages here?
    # Right now, parsing only when it's requested.
    # Come back here when you figure out how to properly parse them
    # No. to times the request is parser <<<<< No. of times it's requested

    @classmethod
    def query_message(cls):
        pass

    @classmethod
    def get_latest_entry(cls):
        try:
            data = cls.query().order(-cls.db_timestamp).fetch(1, offset=0)

            if len(data):
                return data[0]
            return False
        except Exception as e:
            logging.info("Error when fetching the latest entry")
            logging.info(str(e))
        return False


class DAL:
    @classmethod
    def get_latest_test_data(cls):
        latest_entry = TestData.get_latest_entry()
        latest_entry = latest_entry.to_dict()
        logging.info(latest_entry)
        try:
            logging.info(logging.info(latest_entry.keys()))
            key = "structured_content"
            latest_entry[key] = json.loads(latest_entry.get(key))
        except Exception as e:
            logging.info(str(e))
        else:
            return latest_entry

    @classmethod
    def insert_test_data(cls, **kwargs):
        content = kwargs.get("content", None)
        test_timestamp = kwargs.get("timestamp", "")

        if content:
            try:
                structured_content = Utils.parse_content(content)

                structured_content_str = json.dumps(
                    structured_content,
                    default=Utils.json_serial
                )

                logging.info(structured_content_str)

                # Add it to the db
                testObj = TestData(
                    content=content,
                    structured_content=structured_content_str,
                    test_timestamp=test_timestamp
                )
            except Exception as e:
                logging.info("Error when parsing content")
                logging.info(str(e))
            else:
                # Inserting it into the db
                try:
                    testObj.put()
                except Exception as e:
                    logging.info("Failed adding content ")
                    logging.info(str(e))
                else:
                    logging.info("Successfully added entry")
                    return True
        else:
            logging.info("Not adding anything since there's no content")
        return False

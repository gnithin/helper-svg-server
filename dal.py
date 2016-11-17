from google.appengine.ext import ndb
import logging


class TestData(ndb.Model):
    content = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    # TODO: Should I store the parsed messages here?

    @classmethod
    def query_message(cls):
        pass

    @classmethod
    def get_latest_entry(cls):
        try:
            return cls.query().order(-cls.timestamp).fetch(1, offset=0)
        except Exception as e:
            logging.info("Error when fetching the latest entry")
            logging.info(str(e))


class DAL:
    @classmethod
    def get_latest_test_data(cls):
        latest_entry = TestData.get_latest_entry()
        return latest_entry

    @classmethod
    def insert_test_data(cls, **kwargs):
        content = kwargs.get("content", None)
        if content:
            # Add it to the db
            testObj = TestData(content=content)
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

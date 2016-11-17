import json
from datetime import datetime


class Utils:
    @classmethod
    def resp_json(cls, resp_type=1, message="", **kwargs):
        kwargs["type"] = str(resp_type)
        kwargs["message"] = message
        return json.dumps(kwargs, default=cls.json_serial)

    @classmethod
    def parse_content(cls, content, timestamp):
        return {
            "content": content,
            "timestamp": timestamp
        }

    @classmethod
    def json_serial(cls, obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, datetime):
            serial = obj.isoformat()
            return serial
        raise TypeError("Type not serializable")

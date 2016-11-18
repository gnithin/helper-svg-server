import json
from datetime import datetime
import re
import logging
# from pprint import pprint
import jinja2
import os

CONFIG_TEMPLATE_PATH = "/templates/"
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) +
                                   CONFIG_TEMPLATE_PATH),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class Utils:
    @classmethod
    def resp_json(cls, resp_type=1, message="", **kwargs):
        kwargs["type"] = str(resp_type)
        kwargs["message"] = message
        return json.dumps(kwargs, default=cls.json_serial)

    @classmethod
    def parse_content(cls, content):
        def parse_tests(tests):
            tests = tests.strip(" \n")

            # Get the test results
            tests_list = [
                s.strip(" \n")
                for s in
                re.split(r'^\s*===\s*RUN\s+.*', tests, flags=re.MULTILINE)
                if s.strip(" \n") != ""
            ]

            all_test_data = []
            for status in tests_list:
                status_line = status.split("\n")[0]
                status_split = status_line.split(" ")
                if len(status_split) > 3:
                    test_name = status_split[2]
                    status = status_split[1].strip(":").lower()
                    time_taken = status_split[-1].strip("()")
                    metadata = {}
                    if status == "fail":
                        metadata["error"] = "\n".join(status_split[1:])
                    all_test_data.append({
                        "test_name": test_name,
                        "test_pass": status == "pass",
                        "time_taken": time_taken,
                        "metadata": metadata
                    })

            return all_test_data

        def parse_benchmarks(bm):
            bm = bm.strip(" \n")

            all_bm_data = []
            for bm_line in bm.split('\n'):
                bm_line = bm_line.strip(" \n")
                bm_contents = re.split(r'[\t\s\n]{2,}', bm_line)
                if len(bm_contents) >= 3:
                    all_bm_data.append({
                        "bm_name" : bm_contents[0],
                        "iterations": bm_contents[1],
                        "rate": bm_contents[2]
                    })
            return all_bm_data

        # Function logic starts here
        content = content.strip()
        final_resp = {}

        test_constituents = re.split(
            r'^\s*(PASS|FAIL)',
            content,
            maxsplit=1,
            flags=re.MULTILINE
        )

        logging.info("*" * 50)
        logging.info(test_constituents)
        logging.info(len(test_constituents))

        if len(test_constituents) <= 3:
            tests, status, benchmarks = test_constituents
            status = status.strip().lower()
            tests_results = parse_tests(tests)
            if tests_results != {}:
                bm_results = parse_benchmarks(benchmarks)
            else:
                bm_results = {}

            logging.info("Test and Benchmarks - ")

            final_resp["tests"] = tests_results
            final_resp["bm"] = bm_results
            final_resp["test_pass"] = status == "pass"
        else:
            logging.info("Fail: Number of consitituents - " +
                         str(len(test_constituents)))

        return final_resp

    @classmethod
    def json_serial(cls, obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, datetime):
            serial = obj.isoformat()
            return serial
        raise TypeError("Type not serializable")

    @classmethod
    def get_template_from_dir(cls, file_name, dir_path, **kwargs):
        if not file_name:
            logging.info("No file name specified for the template")
            return False

        if not dir_path:
            dir_path = CONFIG_TEMPLATE_PATH

        # Setting this everytime
        JINJA_ENVIRONMENT.loader = jinja2.FileSystemLoader(
            os.path.dirname(__file__) + dir_path
        )
        logging.info(os.path.dirname(__file__) + dir_path)
        try:
            template = JINJA_ENVIRONMENT.get_template(file_name)
            return template.render(**kwargs)
        except Exception as e:
            logging.info("Error while creating template - " + str(file_name))
            logging.info(e.message)
            logging.info(str(e))

        return False

    @classmethod
    def get_template(cls, file_name, **kwargs):
        '''Get template resultant string. '''
        if not file_name:
            logging.info("No file name specified for the template")
            return False

        return cls.get_template_from_dir(
            file_name,
            CONFIG_TEMPLATE_PATH,
            **kwargs
        )

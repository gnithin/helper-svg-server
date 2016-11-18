import json
from datetime import datetime
import re
# import logging
# from pprint import pprint


class Utils:
    @classmethod
    def resp_json(cls, resp_type=1, message="", **kwargs):
        kwargs["type"] = str(resp_type)
        kwargs["message"] = message
        return json.dumps(kwargs, default=cls.json_serial)

    @classmethod
    def parse_content(cls, content, timestamp):
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

        content = content.strip()
        final_resp = {}

        test_constituents = re.split(
            r'^\s*(PASS|FAIL)',
            content,
            maxsplit=1,
            flags=re.MULTILINE
        )

        if len(test_constituents) <= 3:
            tests, status, benchmarks = test_constituents
            status = status.strip().lower()
            tests_results = parse_tests(tests)
            if tests_results != {}:
                bm_results = parse_benchmarks(benchmarks)
            else:
                bm_results = {}

            print("Test and Benchmarks - ")

            final_resp["tests"] = tests_results
            final_resp["bm"] = bm_results
            final_resp["test_pass"] = status == "pass"
        else:
            print("Fail: Number of consitituents - " +
                  str(len(test_constituents)))

        return final_resp

    @classmethod
    def json_serial(cls, obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, datetime):
            serial = obj.isoformat()
            return serial
        raise TypeError("Type not serializable")

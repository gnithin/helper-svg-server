import json
from datetime import datetime
import re
# import logging
from pprint import pprint


class Utils:
    @classmethod
    def resp_json(cls, resp_type=1, message="", **kwargs):
        kwargs["type"] = str(resp_type)
        kwargs["message"] = message
        return json.dumps(kwargs, default=cls.json_serial)

    @classmethod
    def parse_content(cls, content, timestamp):
        content = content.strip()
        final_resp = {}

        test_constituents = re.split(
            r'^\s*(?:PASS|FAIL)',
            content,
            flags=re.MULTILINE
        )
        pprint(test_constituents)

        if len(test_constituents) == 2:
            tests, benchmarks = test_constituents
            tests_results = cls.parse_tests(tests)
            bm_results = cls.parse_benchmarks(benchmarks)

            print("Test and Benchmarks - ")
            pprint(tests_results)
            pprint(bm_results)

            final_resp["tests"] = tests_results
            final_resp["bm"] = bm_results
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

    @classmethod
    def parse_tests(cls, tests):
        tests = tests.strip(" \n")

        # Get the test results
        tests_list = tests.split("\n")
        all_test_data = []
        for i in range(0, len(tests_list) - 1, 2):
            run_line = tests_list[i].strip(" \n")
            status_line = tests_list[i+1].strip(" \n")

            test_name = run_line.split(" ")[-1]
            status_split = status_line.split(" ")
            status = status_split[1].strip(":")
            time_taken = status_split[-1].strip("()")
            all_test_data.append({
                "test_name": test_name,
                "status": status,
                "time_taken": time_taken
            })

        return all_test_data

    @classmethod
    def parse_benchmarks(cls, bm):
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

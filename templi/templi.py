#!/usr/bin/env python
import os
import sys
import pystache

CONFIGURATION_FOLDER = os.path.join(os.environ[ "HOME" ], ".templi")
TEMPLATE_CONFIGURATION_FILE = "templi.json"

class Templi(object):


    def __init__(self):
        self.mk_conf_dir()
        self.ARGV      = False
        self.ARGV_CONF = False
    def check_template_conf_file(self, templateDirectory):
        filePath = os.path.join(templateDirectory, TEMPLATE_CONFIGURATION_FILE)
        return True if os.path.exists(filePath) else False
    def mk_conf_dir(self):
        if not self.check_conf_dir():
            os.mkdir(CONFIGURATION_FOLDER, mode=0777)
    def check_conf_dir(self):
        return True if os.path.exists(CONFIGURATION_FOLDER) else False
    def list_templates(self):
        os.listdir(CONFIGURATION_FOLDER)
    def parse_json(self, filePath):
        import json
        try:
            json_contents = open(filePath, "r").read()
        except Exception as e:
            raise e
            sys.exit(1)
        try:
            self.ARGV_CONF = json.loads(json_contents)
        except Exception as e:
            raise e
            sys.exit(1)
    def prompt(self):
        pass


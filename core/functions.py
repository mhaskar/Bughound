#!/usr/bin/python

import os
import sys
import json
from core.shipper import *
from termcolor import cprint


def print_error(text):
    message = "[-] {0}".format(text)
    cprint(message, "red")


def print_success(text):
    message = "[+] {0}".format(text)
    cprint(message, "green")


def check_path(path):
    if os.path.exists(path) is False:
        print_error("[-]path not exist")
        exit()
    else:
        return True

def read_file(file_path):
    if check_path(file_path):
        fi = open(file_path, "r")
        data = fi.read()
        fi.close()
        return data
    else:
        print_error("File not exist")
        return False


def read_file_lines(file_path):
    if check_path(file_path):
        fi = open(file_path, "r")
        file_lines = fi.readlines()
        fi.close()
        return file_lines
    else:
        print_error("File not exist")
        return False


def get_regex(language):
    fi = open("data/data.json", "r")
    data = fi.read()
    json_data = dict(json.loads(data))
    return json_data[language]["regex"]


def get_language_data(language):
    fi = open("data/data.json", "r")
    data = fi.read()
    json_data = dict(json.loads(data))
    return json_data[language]["category"]

def check_extension(extension):
    if extension[0] == ".":
        return True
    else:
        return False    


def check_language(language):
    fi = open("data/data.json", "r")
    data = fi.read()
    json_data = dict(json.loads(data))
    languages = json_data.keys()
    if language in languages:
        return True
    else:
        return False


def check_project(project_name):
    full_url = elastic_host + default_index + "/_search"
    data = {
          "query": {
            "term": {
              "project": {
                "value": project_name
              }
            }
          }
      }
    req = requests.get(full_url, json=data)
    response = req.text
    value = json.loads(response)["hits"]["total"]["value"]
    if value != 0:
        return True
    else:
        return False


def clone_repo(repo_url, project_name):
    # check if git is installed
    check_git = os.popen("which git").read()
    if check_git == "":
        print("Git is not installed")
        exit()

    if os.path.exists("projects"):
        pass
    else:
        os.mkdir("projects")
    # clone the repo using git
    command = "git clone %s projects/%s" % (repo_url, project_name)
    print_success("Cloning ..")
    os.system(command)
    print_success("Cloning Done!")



def get_files(path, extension):
    files_list = []
    if check_path(path):
        print_success("Scanning started for the script")
        for root, dirs, files in os.walk(path, topdown=False):
                for fi in files:
                    dfile = os.path.join(root, fi)
                    if dfile.endswith(extension):
                        files_list.append(dfile)
    return files_list

#!/usr/bin/python

import argparse
import sys
from core.parser import *
from core.functions import *
from core.shipper import *



argparser = argparse.ArgumentParser()
argparser.add_argument("--path", help="local path of the source code")
argparser.add_argument("--git_repo", help="git repository URL")
#argparser.add_argument("--init", help="initialize Elastic and Kibanna requirements", action="store_true")
argparser.add_argument("--language", help="the used programming language", required=True)
argparser.add_argument("--extension", help="extension to search for", required=True)
argparser.add_argument("--name", help="project name to use", required=True)
arguments = argparser.parse_args()

local_path = arguments.path
git_repo = arguments.git_repo
language = arguments.language
extension = arguments.extension
project_name = arguments.name


if check_language(language) == False:
    print_error("Language %s not supported!" % language)
    exit()

if check_extension(extension) == False:
    print_error("Extension should start with .")
    print_error("Example : .java, .php")
    exit()

# Check connection to Elastic
if verify_connection():
    # Check if index existed
    if check_index() == False:
        create_index()
        create_index_pattern()
        print_success("Setup ELK stack configuration for you ..")
        #import_dashboards()
    else:
        # Check if the project name is already used
        if check_project(project_name):
                    print_error("Project name %s already used" % project_name)
                    print_error("Please change it")
                    exit()

        print_success("ELK is already configured!")



else:
    print_error("please check connection to Elasticsearch")
    exit()


if git_repo is None and local_path:
    files = get_files(local_path, extension)
    for file in files:
        p = parser(file, project_name, language)
        file_metadata = p.calculate_metdata()
        findings = p.get_functions()


if local_path is None and git_repo:
    # Use git repo
    clone_repo(git_repo, project_name)
    files = get_files("projects/%s" % project_name, extension)
    for file in files:
        p = parser(file, project_name, language)
        file_metadata = p.calculate_metdata()
        functions = p.get_functions()


if local_path is None and git_repo is None:
    print_error("please specify the git repo or local path to scan")
    exit()

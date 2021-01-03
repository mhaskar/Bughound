#!/usr/bin/python3

import time
import sys
import re
from core.functions import *
from core.shipper import *
from hashlib import sha512
php_final_findings = []
previous_findings = []

class parser:


    def __init__(self, file, project_name, language):
        self.project_name = project_name
        self.file = file
        self.language = language
        return None


    def calculate_metdata(self):
        sha512_hash = sha512(self.file.encode()).hexdigest()
        timestamp = time.time()
        extension = self.file.split(".")[1]
        metadata = {
            self.project_name: {
                "filename": self.file,
                "sha512_hash": sha512_hash,
                "timestamp": timestamp,
                "extension": extension,
                "language": self.language
            }
        }
        self.metadata = metadata
        return metadata


    # Get unsafe functions from a file
    def get_functions(self):

        final_findings = []
        metadata_existed = False

        # regex to get all function calls for languages such as php
        # debugging
        # global_regex = "\w+\(.*?\)"

        metadata = self.metadata
        line_number = 0
        # Get the extension based on line #28
        extension = metadata[self.project_name]["extension"]
        language = metadata[self.project_name]["language"]
        regex = get_regex(language)
        catagories = get_language_data(language)
        file = self.file
        # Check if we regex is None == Java
        if regex == "None":
            final_findings = []
            code_snippet = ""
            line_number = 0
            lines = read_file_lines(file)
            data = get_language_data(language)
            for line in lines:
                line_number = line_number + 1
                for catagory in data:
                    for function in data[catagory]:
                        if function in line:
                            metadata[self.project_name]["category"] = catagory
                            metadata[self.project_name]["function"] = function
                            if line_number > 3:
                                code_snippet = lines[line_number - 3]
                                code_snippet+= lines[line_number - 2]
                                code_snippet+= lines[line_number - 1]
                                code_snippet+= lines[line_number]
                                try:
                                    code_snippet+= lines[line_number + 1]
                                except IndexError:
                                    pass
                                try:
                                    code_snippet+= lines[line_number + 2]
                                except IndexError:
                                    pass
                                try:
                                    code_snippet+= lines[line_number + 3]
                                except IndexError:
                                    pass
                            if line_number < 3:
                                code_snippet = lines[line_number]
                            #print(code_snippet)
                            metadata[self.project_name]["line_number"] = line_number
                            metadata[self.project_name]["line"] = code_snippet
                            print_success("Shipping entry")
                            ship_entry(self.project_name, metadata)

        else:
            line_number = 0
            lines = read_file_lines(file)
            data = get_language_data(language)

            for line in lines:
                line_number = line_number + 1
                for catagory in data:
                    for function in data[catagory]:
                        new_regex = regex.format(function)
                        results = re.findall(new_regex, line)
                        if results:
                            metadata[self.project_name]["category"] = catagory
                            metadata[self.project_name]["function"] = function
                            if line_number > 3:
                                code_snippet = lines[line_number - 3]
                                code_snippet+= lines[line_number - 2]
                                code_snippet+= lines[line_number - 1]
                                code_snippet+= lines[line_number]
                                try:
                                    code_snippet+= lines[line_number + 1]
                                except IndexError:
                                    pass
                                try:
                                    code_snippet+= lines[line_number + 2]
                                except IndexError:
                                    pass
                                try:
                                    code_snippet+= lines[line_number + 3]
                                except IndexError:
                                    pass
                            else:
                                code_snippet = lines[line_number]

                            #print(code_snippet)
                            metadata[self.project_name]["line_number"] = line_number
                            metadata[self.project_name]["line"] = code_snippet
                            print_success("Shipping entry")
                            ship_entry(self.project_name, metadata)
                            #metadata.clear()
                            #print([file, function, line_number])
                            #if [file, function, line_number] in previous_findings:
                            #    print("duplicate found")
                            #else:
                            #    print("original")
                            #    previous_findings.append([file, function, line_number])
                                # Copy the new dictionary by value so we don't copy
                                # The last element when we finish the loop
                            #    print(previous_findings)
                            #    new_meta = copy.deepcopy(metadata)
                            #    php_final_findings.append(new_meta)
                            #    print("+" * 20)

            # return(php_final_findings)

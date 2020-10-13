#!/usr/bin/env python
import os

for part_name in os.listdir():
    try:
        os.chdir(part_name)

        for file_name in os.listdir():
            contents: str = ''
            with open(file_name, 'r', encoding='utf-8') as input_file:
                contents = input_file.read()

            # ties (~) before formulas ($)
            contents = contents.replace(r" $", r'~$')
            # but bot after special symbols
            for previous in r":;,.!?[](){}":
                contents = contents.replace(previous + r"~$", previous + r" $")
            contents = contents.replace(r"\item~$", r"\item $")

            with open(file_name, 'w', encoding='utf-8') as output_file:
                output_file.write(contents)

        os.chdir('..')
    
    # TODO: add a normal if instead of this workaround
    except:  # part_name is file not dir
        pass

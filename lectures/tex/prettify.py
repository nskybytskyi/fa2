#!/usr/bin/env python
import os

for part_name in os.listdir():
    for file_name in os.listdir(part_name):
        contents: str = ''
        with open(file_name, 'r') as input_file:
            contents = input_file.read()
        contents.replace(' $', '~$')
        for previous in ':;,.!?':
            contents.replace(previous + '~$', previous +' $')
        with open(file_name, 'w') as output_file:
            output_file.write(contents)

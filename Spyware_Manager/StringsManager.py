import os
import re
import json

def extract_strings(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    strings = re.findall(b'[ -~]{4,}', data)
    return [s.decode('utf-8', errors='ignore') for s in strings]


def load_sus_keywords():
    json_path = f'{os.path.abspath(os.path.dirname(__file__))}\strings\strings.json'
    with open(json_path, 'r') as file:
        keywords = json.load(file)
    return keywords


def match_strings(path, keywords):
    matches = []
    strings = extract_strings(path)
    for string in strings:
        for keyword in keywords:
            if keyword.lower() in string.lower():
                matches.append(string)
                break
    return matches

    
def scan_string(path):
    sus_keywords = load_sus_keywords()
    results = []
    
    if not os.path.isdir(path):
        res = match_strings(path, sus_keywords)
        if res != []:
            results.append({'path': os.path.abspath(path), 'name': os.path.basename(path), 'info': ', '.join(res)})
    else:
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                res = scan_string(file_path)
                if res != []:
                    results.extend(res)
            else:
                res = match_strings(file_path, sus_keywords)
                if res != []:
                    results.append({'path': os.path.abspath(file_path), 'name': os.path.basename(file_path), 'info': ', '.join(res)})
    
    return results


if __name__ == "__main__":
    pass
    
import os
import yara

def ScanFile():
    rule_path = "Spyware_Manager\\YARA_RULES.yar"
    rules = yara.compile(rule_path)
    results = []

    for file in os.listdir("malware"):
        matches = rules.match(f"malware\\{file}")
        results.append(matches)
        
    return results



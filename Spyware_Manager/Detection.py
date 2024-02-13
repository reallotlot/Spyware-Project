import os
import yara

rule_path = "Spyware_Manager\\YARA_RULES.yar"
rules = yara.compile(rule_path)

for file in os.listdir("malware"):
    matches = rules.match(f"malware\\{file}")
    print(matches)



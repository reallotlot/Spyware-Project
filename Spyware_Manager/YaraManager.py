import yara

rules = yara.compile("Spyware_Manager\yarafiles\pe_rules.yar")

matches = rules.match("malware\\test.exe")

print(matches)
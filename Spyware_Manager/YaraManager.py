import os
import yara

#DO NOT CHANGE THIS PATH WITHOUT KNOWING WHAT YOU ARE DOING!
#DOING SO WILL CAUSE THE PROGRAM TO NOT BE ABLE TO USE MOST OF THE YARA RULES
#CAUSING SECURITY RISKS
compiled_rules_path = r"Spyware_Manager\yarafiles\compiled-rule-master"


#one time run will only run once if the compiled rules file is empty!!!!!!
def compile_rulemaster_rules():
    path = r"Spyware_Manager\yarafiles\rules-master"
    for mal in os.listdir(path):
        rule_path = os.path.join(path, mal)
        rules = yara.compile(rule_path)
        rules.save(f'Spyware_Manager\yarafiles\\rule-master-compiled\\compiled_{mal}')





def scan_file(path):
    for rule_file in os.listdir(compiled_rules_path):
        rules = yara.load(os.path.join(compiled_rules_path, rule_file))
        for mal in (os.listdir(path)):
            matches = rules.match(os.path.join(path, mal))
            if matches != []:
                print(matches)


if __name__ == "__main__":
    if os.listdir(compiled_rules_path) == []:
        compile_rulemaster_rules()
        print("done")
    else:
        print("already compiled")
        
        
    scan_file(r'malware')

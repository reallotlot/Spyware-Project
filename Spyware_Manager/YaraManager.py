import os
import time
import yara

#DO NOT CHANGE THIS PATH UNLESS YOU KNOW WHAT YOU ARE DOING!
#DOING SO WILL CAUSE THE PROGRAM TO NOT BE ABLE TO USE MOST OF THE YARA RULES
#CAUSING SECURITY RISKS
compiled_rules_path = f'{os.path.dirname(os.path.abspath(__file__))}\yarafiles\compiled-rule-master'


#one time run will only run once if the compiled rules file is empty!!!!!!
def compile_rulemaster_rules():
    os.makedirs(compiled_rules_path)
    while not (os.path.exists(compiled_rules_path)):
        time.sleep(.3)
        print("loading")
        
    path = f'{os.path.dirname(os.path.abspath(__file__))}\yarafiles\rule-master'
    for mal in os.listdir(path):
        rule_path = os.path.join(path, mal)
        rules = yara.compile(rule_path)
        print("saving rules")
        rules.save(f'{compiled_rules_path}\compiled_{mal}')

def comp():
    if os.path.exists(compiled_rules_path):
        if os.listdir(compiled_rules_path) != []:
            pass#print("already compiled")
    else:
        compile_rulemaster_rules()
        #print("done")



def scan_yara(path):
    comp()
    results = []
    for rule_file in os.listdir(compiled_rules_path):
        rules = yara.load(os.path.join(compiled_rules_path, rule_file))
        if not os.path.isdir(path):
            matches = rules.match(path)
            if matches != []:
                results.append({'path': os.path.abspath(path), 'name': os.path.basename(path), 'info': rule_file})
        else:
            for file in (os.listdir(path)):
                file_path = os.path.join(path, file)
                if os.path.isdir(file_path):
                    res = scan_yara(file_path)
                    if res != []:
                        results.append(res)
                else:
                    matches = rules.match(file_path)
                    if matches != []:
                        results.append({'path': os.path.abspath(path), 'name': file, 'info': rule_file})
    return results



if __name__ == "__main__":
    pass

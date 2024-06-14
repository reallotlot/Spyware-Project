import subprocess
import os
import json

# Define the path to the memory dump and Volatility
dir_path = os.path.abspath(os.path.dirname(__file__))
memory_dump_path = os.path.join(dir_path, 'dump.raw')
volatility_path = r'C:\Users\lotan\project\Spyware-Project\Spyware_Manager\sandbox\Volatility\volatility3\vol.py'
python_executable = r'C:\Users\lotan\AppData\Local\Programs\Python\Python310\python.exe'

# Define the plugins you want to run
plugins = [
    'windows.pslist.PsList',
    'windows.pstree.PsTree',
    'windows.dlllist.DllList',
    'windows.netscan.NetScan',
    'windows.malfind.Malfind'
]

# Known indicators of compromise (IOCs)
suspicious_processes = ['malware.exe', 'unknown.exe']
suspicious_dlls = ['malicious.dll', 'unknown.dll']
suspicious_ips = ['192.168.1.100', '10.0.0.1']

# Function to run a Volatility plugin and capture its output
def run_volatility_plugin(plugin, memory_dump):
    cmd = [python_executable, volatility_path, '-f', memory_dump, plugin]
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print(f"Error running plugin {plugin}: {stderr.decode('utf-8')}")
        return stdout.decode('utf-8')
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return ""
    except OSError as e:
        print(f"OSError: {e}")
        return ""

# Function to parse the output of a Volatility plugin
def parse_output(plugin, output):
    parsed_data = {}
    if plugin == 'windows.pslist.PsList':
        lines = output.splitlines()
        headers = lines[0].split()
        parsed_data[plugin] = []
        for line in lines[1:]:
            values = line.split()
            parsed_data[plugin].append(dict(zip(headers, values)))
    elif plugin in ['windows.dlllist.DllList', 'windows.netscan.NetScan', 'windows.malfind.Malfind']:
        parsed_data[plugin] = output  # Customize this parsing as needed
    return parsed_data

# Function to check for suspicious indicators
def check_for_indicators(results):
    findings = {
        'suspicious_processes': [],
        'suspicious_dlls': [],
        'suspicious_network_connections': [],
        'malfind_results': []
    }
    
    # Check for processes
    if 'windows.pslist.PsList' in results:
        for process in results['windows.pslist.PsList']:
            if process.get('Process') in suspicious_processes:
                findings['suspicious_processes'].append({'plugin': 'windows.pslist.PsList', 'process_info': process})
    
    # Check for DLLs
    if 'windows.dlllist.DllList' in results:
        for line in results['windows.dlllist.DllList'].split('\n'):
            for dll in suspicious_dlls:
                if dll in line:
                    findings['suspicious_dlls'].append({'plugin': 'windows.dlllist.DllList', 'dll_info': line})
    
    # Check for network connections
    if 'windows.netscan.NetScan' in results:
        for line in results['windows.netscan.NetScan'].split('\n'):
            for ip in suspicious_ips:
                if ip in line:
                    findings['suspicious_network_connections'].append({'plugin': 'windows.netscan.NetScan', 'connection_info': line})
    
    # Check for malfind results
    if 'windows.malfind.Malfind' in results:
        findings['malfind_results'] = {'plugin': 'windows.malfind.Malfind', 'malfind_info': results['windows.malfind.Malfind']}
    
    return findings

def analyze_memory_dump(memory_dump, plugins):
    results = {}
    for plugin in plugins:
        print(f"Running {plugin} plugin...")
        output = run_volatility_plugin(plugin, memory_dump)
        results.update(parse_output(plugin, output))
    return results

def categorize_malware(findings):
    categories = []
    if findings['suspicious_processes']:
        categories.append('Suspicious Process')
    if findings['suspicious_dlls']:
        categories.append('Suspicious DLL')
    if findings['suspicious_network_connections']:
        categories.append('Suspicious Network Connection')
    if findings['malfind_results']:
        categories.append('Memory Injection (Malfind)')
    return categories

def run_analysis():
    results = analyze_memory_dump(memory_dump_path, plugins)
    
    # Check for indicators
    findings = check_for_indicators(results)
    
    malicious_found = False
    malicious_info = []

    # Categorize the type of malware
    malware_types = categorize_malware(findings)

    if malware_types:
        malicious_found = True
        malicious_info.append(f"Detected malware types: {', '.join(malware_types)}")

    # Check for suspicious processes
    for process in findings['suspicious_processes']:
        process_info = process['process_info']
        malicious_info.append(f"Suspicious process found by {process['plugin']}:\n"
                              f"  Process: {process_info['Process']}\n"
                              f"  PID: {process_info['PID']}\n"
                              f"  PPID: {process_info['PPID']}\n"
                              f"  Name: {process_info['Name']}")
    
    # Check for suspicious DLLs
    for dll in findings['suspicious_dlls']:
        dll_info = dll['dll_info']
        malicious_info.append(f"Suspicious DLL found by {dll['plugin']}:\n  {dll_info}")
    
    # Check for suspicious network connections
    for connection in findings['suspicious_network_connections']:
        connection_info = connection['connection_info']
        malicious_info.append(f"Suspicious network connection found by {connection['plugin']}:\n  {connection_info}")
    
    # Check for malfind results
    if findings['malfind_results']:
        malicious_found = True
        malfind_info = findings['malfind_results']['malfind_info']
        # Extract only the first line of the malfind results for better readability
        malfind_first_line = malfind_info.split('\n', 1)[0]
        malicious_info.append(f"Malfind results found by {findings['malfind_results']['plugin']}:\n  {malfind_first_line}")
    
    # Return whether malicious indicators were found and some info about them
    return malicious_found, malicious_info

if __name__ == '__main__':
    pass

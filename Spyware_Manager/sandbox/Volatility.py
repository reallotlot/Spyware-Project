import subprocess
import os

# Define the path to the memory dump and Volatility
dir_path = os.path.abspath(os.path.dirname(__file__))
memory_dump_path = os.path.join(dir_path, 'dump.raw')
volatility_path = r'C:\Users\lotan\project\Spyware-Project\Spyware_Manager\sandbox\Volatility\volatility3\vol.py'
python_executable = r'C:\Users\lotan\AppData\Local\Programs\Python\Python310\python.exe'


# Function to run a Volatility plugin and capture its output
def run_volatility_plugin(plugin):
    cmd = [python_executable, volatility_path, '-f', memory_dump_path, plugin]
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print(f"Error running plugin {plugin}: {stderr.decode('utf-8')}")
        return stdout.decode('utf-8')
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return None


# Function to parse and format the output of a Volatility plugin
def format_plugin_output(plugin, output):
    formatted_output = f"Output for plugin: {plugin}\n"
    formatted_output += "-" * 40 + "\n"
    formatted_output += output  
    formatted_output += "\n" + "-" * 40 + "\n"
    return formatted_output


# Function to run all plugins and print their output
def run_all_plugins(file_name):
    plugins = [
        'windows.pslist',
        'windows.dlllist',
        'windows.netscan',
        'windows.malfind',
        'windows.netstat',
        'windows.cmdline'
    ]

    for plugin in plugins:
        print(f"Running plugin: {plugin}")
        output = run_volatility_plugin(plugin)
        formatted_output = format_plugin_output(plugin, output)
        
        # Save data into files
        data_path = os.path.join(r'C:\Users\lotan\project\Spyware-Project\Spyware_Manager\sandbox\data', file_name)
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        
        with open(os.path.join(data_path, f'{plugin}.txt'), 'w+') as file:
            file.write(formatted_output)

if __name__ == '__main__':
    #run_all_plugins('Flasher.exe')
    pass
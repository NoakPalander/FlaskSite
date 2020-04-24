import subprocess, sys, time

def main():
    # Returns if no file-name was passed
    if len(sys.argv) < 2:
        print('Please specify the name of the python-file you want to restart!')
        exit(-1)

    name = sys.argv[1]
    if not name.endswith('.py'):
        name += '.py'
    
    try:
        # Grab the process ID of the server
        out = subprocess.Popen(['pgrep', '-f', name],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        
        pid = int(out.communicate()[0])

        print(f'Killing process {name}, pid {pid}..')
        subprocess.Popen(['kill', str(pid)])
        time.sleep(1)
        
        print(f'Starting server {name}..')        
        subprocess.Popen([sys.executable, name])
        
    except ValueError: # Process wasn't running
        print(f'Starting server {name}..')
        subprocess.Popen([sys.executable, name])
        
if __name__ == '__main__':
    main()

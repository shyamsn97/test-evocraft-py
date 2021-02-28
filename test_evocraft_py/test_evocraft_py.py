import os
import subprocess, signal
from subprocess import Popen
import shutil

pt = os.path.dirname(os.path.realpath(__file__))

REQUIRED = [
    "mods",
    "eula.txt",
    "server.properties",
    "spongevanilla-1.12.2-7.3.0.jar"
]

def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))

def check_pid():
    pid_path = "{}/data/evocraft_server.pid".format(pt)
    if os.path.exists(pid_path):
        return pid_path
    return None

def shutdown_server(remove_files=True):
    if check_pid() is None:
        print("Cannot find running Evocraft server!")
        return
    try:
        data_path = "{}/data".format(pt)
        pid_path = "{}/evocraft_server.pid".format(data_path)
        f = open(pid_path, 'r')
        pid = int(f.read())
        os.kill(pid, signal.SIGKILL)
        os.unlink(pid_path)
    except Exception:
        pass
    
    try:
        if remove_files:
            paths = os.listdir(data_path)
            for p in paths:
                if p not in REQUIRED:
                    remove(os.path.join(data_path, p))
        print("Server running on process {} killed!".format(pid))
    except Exception:
        pass

def write_pid(pid):
    pid_path = "{}/data/evocraft_server.pid".format(pt)
    f = open(pid_path, 'w')
    f.write(pid)
    f.close()
    return pid_path

def start_server():
    pid_path = check_pid()
    if pid_path:
        shutdown_server()
    p = Popen(["java",  "-jar", "spongevanilla-1.12.2-7.3.0.jar"], cwd="{}/data".format(pt))
    pid_path = write_pid(str(p.pid))
    print("Started server from python process: {}, pidfile path: {}".format(p.pid, pid_path))

def start_server_interactive():
    pid_path = check_pid()
    if pid_path:
        shutdown_server()
    os.chdir("{}/data".format(pt))
    os.system("java -jar spongevanilla-1.12.2-7.3.0.jar")

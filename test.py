import subprocess
import sys
import site
import json
import yaml
import re


# version of python
def vers_pyt():
    data = subprocess.Popen(['python', '-V'], stdout=subprocess.PIPE)
    output = str(data.communicate())
    output = output.split("'")
    version = output[1].split("\\n")
    return version[0]


# virtualvenv name
def virt_name():
    venv = sys.prefix.split("/")
    return venv[-1]


# python executable location
def pyt_loc():
    data = subprocess.Popen(['which', 'python'], stdout=subprocess.PIPE)
    output = str(data.communicate())
    output = output.split("'")
    version = output[1].split("\\n")
    return version[0]


# pip location
def pip_loc():
    data = subprocess.Popen(['which', 'pip'], stdout=subprocess.PIPE)
    output = str(data.communicate())
    output = output.split("'")
    version = output[1].split("\\n")
    return version[0]


# PYTHONPATH
def pyt_path():
    pytpath = []
    for p in sys.path:
        pytpath.append(p)
    return pytpath


# installed packages: name, version
def inst_pack():
    data = subprocess.Popen(['pip', 'freeze'], stdout=subprocess.PIPE)
    output = str(data.communicate())
    output = output.split("'")
    packages = output[1].split("\\n")
    for i in range(len(packages)):
        packages[i] = packages[i].replace('==', ', ')
    return packages


# site-packages location
def site_loc():
    return site.getsitepackages()[0]


# python versions and environment
def vers_pyt_all():
    data = subprocess.Popen(['pyenv', 'versions'], stdout=subprocess.PIPE)
    output = str(data.communicate())
    output = output.split("'")
    version = output[1].split("\\n")
    regexc = re.compile(r'[1-3]\.\d\.\d')
    pyt_ver = set()
    for i in range(len(version)):
        pyt_ver.add(str(regexc.findall(version[i])))
    pyt_vers = (', '.join(pyt_ver))
    pyt_vers = pyt_vers.replace('[]', '')
    return version, pyt_vers


dicts = {}
vers_py = vers_pyt()
dicts['vers_pyt'] = vers_py
virt_nam = virt_name()
dicts['virt_name'] = virt_nam
pyt_lo = pyt_loc()
dicts['pyt_loc'] = pyt_lo
pip_lo = pip_loc()
dicts['pip_loc'] = pip_lo
pyt_pa = pyt_path()
dicts['pyt_path'] = pyt_pa
inst_pac = inst_pack()
dicts['inst_pack'] = inst_pac
site_lo = site_loc()
dicts['site_loc'] = site_lo
envir, pyt_ver = vers_pyt_all()
dicts['all_pyt_ver'] = str(pyt_ver)
dicts['all_env'] = str(envir)

with open('environ.json', 'w') as env:
    json.dump(dicts, env)

with open('environ.yaml', 'w') as env:
    yaml.dump(dicts, env)

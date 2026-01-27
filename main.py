global STAMP_VERSION_STRING
STAMP_VERSION_STRING = "4.3.2.2"
f"""
Main module for `stamp`

Stamp is a module for timestamping, memory server managment, json managment, task manager, certificates, and more.
This is only the main module

Stamp was created on the 18th September 2025 at 12 o'clock, in the afternoon, 
but in stamp's lstamp._lstamp time format it was on 920251812. Full date is this:
091253202518. 091253202518 (MMHHYYYYDD) format not included in stamp

Sample Usage:
>>> from stamp.main import Stamp, lstamp 
>>> Stamp._stamp
>>> lstamp._lstamp

Main Stamp class Usage

The main Stamp class is a timestamp essential, so here is the usage
Arguments: `None`
Description: ``

Importation:
Use:
>>> from stamp.sibling import thing
Don't:
>>> from stamp import thing

Otherwise, it will raise a DeprecatedError.

Stamp was created on the 18th September 2025 at 12 o'clock, in the afternoon, 
but in stamp's lstamp._lstamp time format it was on 920251812. Full date is this:
091253202518. 091253202518 (MONTH-HOUR-MINUTE-YEAR-DAY) format not included in stamp

Stamp is version {STAMP_VERSION_STRING}
"""
#BUG!s reflist
#None
from .__fetch__ import Fetch
import sys
import ast
import base64
import shutil
import random
import datetime
import platform
import subprocess
import socket
import os
import time
import math
import cmath
import json
import requests
import psutil
from rich import print as rp
from playsound import playsound
from rich.text import Text
#globals
global __version__
global __all__
global __allc__
global STAMP_FULL_VSTRING
STAMP_VERSION_STRING = "4.3.2.2"
STAMP_BUILD_STRING = "ST-4-3-2-2-[19-11-2025]"
__version__ = STAMP_VERSION_STRING
__all__ = [
    "ErrorSystem", "__initexec__", "globalsys", "Stamp", "PCStamp",
    "ListDirectory", "CallError", "call", "__cstring__", "__cmd__",
    "_py_classlvl_consts", "superobj", "__jsonconf__", "__msrv__",
    "_history", "_kvstore", "ttransfer", "transfer", "_chunk",
    "Astray", "__cid__", "__calc_hcl__", "adverr", "advout", "advin",
    "__cmp__", "__helpcmd__", "pdec", "__exf__", "__cd__", "tconstant",
    "tlist", "Type", "UnknownAdverrIntError", "Control",
    "Debug", "DirectoryExistsError", "ArgumentError", "_export",
    "_import", "_mkdir", "_mkfile", "_note", "_notes", "_cl", "_lock",
    "S1", "S2", "C1", "C2", "K1", "K2", "T1", "T2", "L1", "L2", "R1",
    "java", "S1", "S2", "C1", "C2", "K1", "K2", "T1", "T2", "L1", "L2", "R1",
    "R2", "temp", "taskmgr", "edit", "Unite", "Kit", "Abomination",
    "Angle", "Alias", "__isin__", "__log__", "Royal", "_count_ds",
    "_count_subds", "_calc", "Frozen", "_seed", "_dynvar", "_link",
    "TimeError", "ixpd", "_uname", "__version__", "exit", "License",
    "OllamaConfig", "OllamaCheck", "GPT2Generator", "Ollama"]
__allc__ = 82
STAMP_FULL_VSTRING = STAMP_BUILD_STRING + " | " + STAMP_VERSION_STRING.replace(".", "-")
global ns
global nsf
global lowercase 
class ErrorSystem:
    ns = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "thirty", "thirty-one", "thirty-two"]
    nsf = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]
    def CustomError(ErrorName=str, errorMessage=str, fileCausedErrorFilePath=str, fileCausedErrorLine=int, fileCausedErrorColumn=int, inModuleIsNone=None, inModuleName=str, fileCausedErrorLineContents=str): 
        ErrorName = ErrorName
        errorMessage = errorMessage
        fileCausedErrorFilePath = fileCausedErrorFilePath
        fileCausedErrorLine = fileCausedErrorLine
        fileCausedErrorColumn = fileCausedErrorColumn
        inModuleName = inModuleName
        inModuleNameIsNone = inModuleNameIsNone
        fileCausedErrorLineContents = fileCausedErrorLineContents
        if inModuleName == "" or " " or " " in inModuleName and inModuleName == str and None and isModuleIsNone == True:
            inModuleName = "<module>"
        elif inModuleName != "" or " " and " " not in inModuleName and inModuleName == str and not None:
            inModuleName = inModuleName
        rp(f"Traceback (most recent call last)\n File [magenta]\"{fileCausedErrorFilePath}\"[/], line [magenta]{fileCausedErrorLine}[/], col [magenta]{fileCausedErrorColumn}[/], in [magenta]{inModuleName}[/]\n  {fileCausedErrorLineContents}")
        rp(f"[magenta bold]{ErrorName}[/]: [magenta]{errorMessage}[/]")
    def NotEnoughArgumentsProvidedError(argumentNeedCount=None, argumentGivenCount=None, classOrDefName=None, classOrDefIsClass=None, classOrDefIsDef=None, anthingInputed=None, classOrDefIsMethod=None):
        error = ""
        log_path = "/raise/log/raises.stamp.log"
        argumentNeedCount = argumentNeedCount
        argumentGivenCount = argumentGivenCount
        classOrDefName = classOrDefName
        classOrDefIsClass = classOrDefIsClass
        classOrDefIsDef = classOrDefIsDef
        classOrDefIsMethod = classOrDefIsMethod
        anythingInputed = anthingInputed
        nsIndexNumber = f"{argumentNeedCount - 1}"
        nsfIndexNumber = f"{argumentNeedCount - 1}"
        nsix = nsIndexNumber
        nsfi = nsfIndexNumber
        if classOrDefIsClass == True and classOrDefIsDef == False or None and classOrDefIsMethod == False or True:
            msg = f"[red bold][/]: class{classOrDefName}takes two ([bold]{argumentNeedCount}[/]) arguments,  but{argumentGivenCount}"
            rp(msg)
            error += msg + "\n"
            if argumentGivenCount > 1:
                msg = "were given\nstderr at" + f" [{Stamp.stamp_()}" + "]"
                rp(msg)
                error += msg + "\n"
                if argumentNeedCount > 1:
                    msg = f"reg.[magenta]stdout[/] class {classOrDefName} takes  {ns[int(nsix)]} ({nsf[int(nsfi)]}) arguments, but None were given\nreg.stdin ;\"None\": stdin.[magenta]regform[/]:"
                    rp(msg)
                    error += msg + "\n"
            else:
                msg1 = "was given\nstderr at" + f" [{Stamp.stamp_()}" + "]"
                msg2 = f"reg.[magenta]stdout[/] class {classOrDefName} takes {ns[int(nsix)]} ({nsf[int(nsfi)]}) arguments, but None was given\nreg.stdin ;\"None\": stdin.[magenta]regform[/]:"
                rp(msg1 + msg2)
                error += msg1 + msg2 + "\n"
            if anythingInputed == True:
                rp("True")
                error += "True\n"
            elif anythingInputed == False:
                rp("False")
                error += "False\n"
            else:
                rp("Unknown")
                error += "Unknown\n"
        elif (
            (classOrDefIsClass == False or None) and 
            (classOrDefIsMethod == False or None) and 
            (classOrDefIsDef == True)
        ):
            msg = f"[red bold][/]: function{classOrDefName}takes two ([bold]{argumentNeedCount}[/]) arguments, but"
            rp(msg)
            error += msg + "\n"
            if argumentGivenCount > 1:
                msg = "were given\nstderr at" + f" [{Stamp.stamp_()}" + "]"
                rp(msg)
                error += msg + "\n"
                if argumentNeedCount > 1:
                    msg = f"reg.[magenta]stdout[/] class {classOrDefName} takes  {ns[int(nsix)]} ({nsf[int(nsfi)]}) arguments, but None were given\nreg.stdin ;\"None\": stdin.[magenta]regform[/]:"
                    rp(msg)
                    error += msg + "\n"
            else:
                msg1 = "was given\nstderr at" + f" [{Stamp.stamp_()}" + "]"
                msg2 = f"reg.[magenta]stdout[/] class {classOrDefName} takes {ns[int(nsix)]} ({nsf[int(nsfi)]}) arguments, but None was given\nreg.stdin ;\"None\": stdin.[magenta]regform[/]:"
                rp(msg1 + msg2)
                error += msg1 + msg2 + "\n"
            if anythingInputed == True:
                rp("True")
                error += "True\n"
            elif anythingInputed == False:
                rp("False")
                error += "False\n"
            else:
                rp("Unknown")
                error += "Unknown\n"
        elif (
                (classOrDefIsClass == False or None) and
                (classOrDefIsMethod == True) and
                (classOrDefIsDef == False or None)
        ):
            msg = f"[red bold][/]: function{classOrDefName}takes two ([bold]{argumentNeedCount}[/]) arguments, but"
            rp(msg)
            error += msg + "\n"
            if argumentGivenCount > 1:
                msg = "were given\nstderr at" + f" [{Stamp.stamp_()}" + "]"
                rp(msg)
                error += msg + "\n"
                if argumentNeedCount > 1:
                    msg = f"reg.[magenta]stdout[/] class {classOrDefName} takes  {ns[int(nsix)]} ({nsf[int(nsfi)]}) arguments, but None were given\nreg.stdin ;\"None\": stdin.[magenta]regform[/]:"
                    rp(msg)
                    error += msg + "\n"
            else:
                msg1 = "was given\nstderr at" + f" [{Stamp.stamp_()}" + "]"
                msg2 = f"reg.[magenta]stdout[/] class {classOrDefName} takes {ns[int(nsix)]} ({nsf[int(nsfi)]}) arguments, but None was given\nreg.stdin ;\"None\": stdin.[magenta]regform[/]:"
                rp(msg1 + msg2)
                error += msg1 + msg2 + "\n"
            if anythingInputed == True:
                rp("True")
                error += "True\n"
            elif anythingInputed == False:
                rp("False")
                error += "False\n"
            else:
                rp("Unknown")
                error += "Unknown\n"
        
    def raising_error():
        rp(f"[bold magenta]stamp[/]: unexpected error occurred")
        rp(f"[[bold red]{Stamp.stamp_()}[/]]")
class __initexec__:
        __execution_timerate__ = ["0.556s"]
        __classes_n__ = 7
        __classes_names__ = ["classcount:7", "errornames", "errorsys", "__initexec__", "globalsys", "Stamp", "PCStamp", "ListDirectory"]
        __init_file__ = "__init__.py"
        __error_handler__ = """
        {
            [
                "class": "errorsys" 
                "raise": "__raise_exec__.class"
            ]
        }
        """
        __var_levels__ = ["__classlevel__", "funclevel", "Classlevel2", "CONST_LEVEL", "__INITEXEC_LEVEL__", "__Stamp_Level__", "nested_funct"]
        __with_open_levels__ = ["a;append", "w;write", "w;overwrite"]
        __initilization_error_raise__ = ["class", "errorsys", "nested_funct", "raising_error"]
class globalsys: # REFUSE to be changed
    global errorsys
    global dt
    global lri
    global sysinfo
    global fromRoot
    dt = None#datetime
    lri = None#location related info
    dt = None  # datetime
    lri = None  # location related info

class Stamp:
    @staticmethod
    def stamp_():
        dt_obj = datetime.datetime.now()
        Fetch.update(dt_obj)
        return (
            f"ML{Fetch.millennia}-CT{Fetch.century}-ST{Fetch.sub_year_tens}{Fetch.sub_year_ones}-M{Fetch.month}-D{Fetch.day}-H{Fetch.hour}-MI{Fetch.minute}-{Fetch.am_pm.lower()}-S{Fetch.second}"
        )
class PCStamp:
    def __init__(self, lri=None, sysinfo=None):
        self.lri = lri#lri is location related info
        self.sysinfo = sysinfo#system info
    @staticmethod
    def __get_hardware_stats__(lri=None, sysinfo=None):
        def get_public_ip():
            try:
                response = requests.get('https://api.ipify.org', timeout=5)
                response.raise_for_status()  
                return response.text
            except requests.exceptions.RequestException as e:
                pass
        public_ip = get_public_ip()
        def private_ip_get():
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            return ip_address
        def sysinfo():
            mem_total_gb = round(virtual_memory.total / (1024**3), 2)#mem.totalgb var
            mem_available_gb = round(virtual_memory.available / (1024**3), 2)#mem.availgb var
            usage_disk = psutil.usage_disk('/' if os.name != 'nt' else '\\')#diskusage var
            disk_total_gb = round(usage_disk.total / (1024**3), 2)#disk.totalgb var
            disk_used_gb = round(usage_disk.used / (1024**3), 2)#disk.usedgb var
            virtual_memory = psutil.virtual_memory()#virt.mem var
            disk_total_gb = round(virtual_memory.total / (1024**3), 2)#disk.total var
            disk_available_gb = round(virtual_memory.available / (1024**3), 2)#diskavail var
            rp(f"cores.physical:{psutil.cpu_count(logical=False)}")#cores that are physical
            rp(f"cores.total:{psutil.cpu_count(logical=True)}")#cores total
            rp(f"cpu.usagepercent:{psutil.cpu_percent(interval=1)}%")#cpu usage percent (%)
            rp(f"mem.total.gb:{mem_total_gb}GB")#memory total (current disk you're in, in your terminal/console)
            rp(f"mem.avail.gb:{mem_available_gb}GB")#memory available (current disk you're in, in your terminal/console)
            rp(f"virtual.mempercent:{virtual_memory.percent}%")#virt.mem percent (%)
            rp(f"disk.total.gb:{disk_total_gb}GB")#disk total (current disk you're in, in your terminal/console)
            rp(f"disk.used.gb:{disk_used_gb}GB")#disk (current disk you're in, in your terminal/console) space used
            rp(f"disk.usagepercent:{usage_disk.percent}%")#disk usage percent (%)
            rp(f"[magenta]system[/].[bold]platform[/]:{sys.platform}")#system platform
            rp(f"[magenta]system[/].executable:{sys.executable}")#python executable
            rp(f"[magenta]system[/].[bold]$PATH[/]:{sys.path}")#system $PATH envvar
            rp(f"[magenta]system[/].argv:{sys.argv}")#python:lib sys.exit
            rp(f"[magenta]system[/].[bold]modules[/]:\n{sys.modules}")#python modules (venv or not)
            rp(f"[magenta]system[/].[bold]stdin[/]:{sys.stdin}")#std input
            rp(f"[magenta]system[/].[bold]stdout[/]:{sys.stdout}")#std output
            rp(f"[magenta]system[/].[bold]stderr[/]:{sys.stderr}")#std error
            rp(f"[magenta]system[/].exit:{sys.exit}")#python:lib sys.exit
            rp(f"[magenta]system[/].[bold]pyver[/]:{sys.version}")#system python version, when executed in any terminal/console (venv or not), it will display the python version
            rp(f"timestamp:{Stamp.stamp_()}")#current timestamp
        if sysinfo and lri == True:
            sysinfo()
            get_public_ip()
            private_ip_get()
        elif sysinfo == True and lri == None or False:
            sysinfo()
        elif sysinfo == False and lri == True:
            get_public_ip()
            private_ip_get()
        elif sysinfo == None or False and lri == None or False:
            rp(
                "[red bold]SyntaxError[/]: class PCStamp takes two ([bold]2[/]) arguments, but None was given\npcstamp.stderr at" + f" [{Stamp.stamp_()}" + "]"
                + "reg.[magenta]stdout[/] class PCStamp takes two (2) arguments, but None was given\nreg.stdin ;\"None\": stdin.[magenta]regform[/]: None")
            pass
        else:
            rp(
                "[red bold]Error[/]: an unexpected error occured at" +
                f"{Stamp.stamp_()}")
class ListDirectory:
    def listdir(fromRoot=None, openInSeperateCMD=None):
        #when using ListDirectory, first import it like: 
        #from stamp import ListDirectory. 
        #then use ListDirectory.listdir to list it.
        #remember to add your options (fromRoot: True/False. if True, it will list from root (C:\ & /)),
        #or it will raise a SyntaxError (custom, using the library rich)
        #if you are on Darwin (macOS/Linux), you cannot yet use openInSeperateCMD=True
        os_name = platform.system()
        command = None
        if fromRoot == True and openInSeperateCMD == True:
            if os_name == "Windows":
                command = ["start", "cmd", "/k", "dir", "/A", "C:\\"]
            else:
                command = ["ls", "-la", "/"]
            if command:
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                    rp(result.stdout)
                except subprocess.CalledProcessError as e:
                    pass
            elif os_name == "Darwin": 
                command = ["ls", "-l"] 
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                    rp(result.stdout)
                except subprocess.CalledProcessError as e:
                    pass
            else:
                pass
        elif fromRoot == False and openInSeperateCMD == True:
            if os_name == "Windows":
                command = ["start", "cmd", "/k", "dir", "/A", "C:\\"]
            else:
                command = ["ls", "-la"]
            if command:
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                    rp(result.stdout)
                except subprocess.CalledProcessError as e:
                    pass
            elif os_name == "Darwin": 
                command = ["ls", "-l"] 
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                    rp(result.stdout)
                except subprocess.CalledProcessError as e:
                    pass
            else:
                pass
        elif fromRoot == False and openInSeperateCMD == False:
            if os_name == "Windows":
                command =  ["dir", "/A", ""]
            else:
                command = ["ls", "-la"]
            if command:
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                    rp(result.stdout)
                except subprocess.CalledProcessError as e:
                    pass
            elif os_name == "Darwin": 
                command = ["ls", "-l"] 
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                    rp(result.stdout)
                except subprocess.CalledProcessError as e:
                    pass
            else:
                pass
        elif fromRoot == True and openInSeperateCMD == False:
            if os_name == "Windows":
                command = ["dir", "/A", "C:\\"]
            else:
                command = ["ls", "-la"]
            if command:
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                    rp(result.stdout)
                except subprocess.CalledProcessError as e:
                    pass
            elif os_name == "Darwin": 
                command = ["ls", "-l"] 
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                    rp(result.stdout)
                except subprocess.CalledProcessError as e:
                    pass
            else:
                pass
        else:
            pass
class CallError(Exception): pass
class call():
    def caller_internal_f(targetName=str, *args, **kwargs):
        targetName = targetName
        target = globals().get(targetName)
        if target is None:
            raise CallError(f"Target '{targetName}' not found.")
        try:
            if callable(target):
                result = target(*args, **kwargs)
            else:
                pass
        except TypeError:
            pass
        except Exception:
            pass
class __cstring__:
    def _cstring_lib(): rp(f"cstring {sys.version} on {sys.platform} ([{platform.platform}, {platform.python_build}:{platform.python_implementation}]) (cstring/lib/extrainfo)\nlibrary\npython/rich\npython library rich integeration\npylib richinteg\ncstring rich edition \n(free, {platform.system().lower()})")
    def _cstring(textInput=str): 
        global text
        text = textInput
    def proccess():
        global text 
        if 'text' not in globals() or not isinstance(text, str):
            raise NameError("global text variable not initialized or is not a string before __cstring__.proccess() call")
        richFText = Text(f"{text}")
        if "[italic/True]" in richFText.plain and "[/reset]" in richFText.plain:
            richFText = richFText.replace("[italic/True]", "[i]")
            richFText = richFText.replace("[/reset]", "[/]")
        if "[strike/True]" in richFText.plain and "[/reset]" in richFText.plain:
            richFText = richFText.replace("[strike/True]", "[strike]")
            richFText = richFText.replace("[/reset]", "[/]")
        if "[bold/True]" in richFText.plain and "[/reset]" in richFText.plain:
            richFText = richFText.replace("[bold/True]", "[bold]")
            richFText = richFText.replace("[/reset]", "[/]")
        if "cstring/lib" in richFText.plain and "[/reset]" in richFText.plain:
            richFText.append(f"\ncstring {sys.version}\nlibrary\npython/rich\npython library rich integeration\npylib richinteg")
            richFText = richFText.replace("cstring/lib", "")
            richFText = richFText.replace("[/reset]", "")
        text = richFText 
        rp(richFText)
class __cmd__:
    def _cmd_run(command=str, timeoutSeconds=int):
        commandStarter = "start cmd /k "
        command = command
        command = commandStarter + command
        timeoutSeconds = timeoutSeconds
        try:
            time.sleep({__cmd__.timeout})
        except Exception as e:
            pass
        subprocess.run(command, shell=True)
class _py_classlvl_consts:
    global STAMP_INIT_CLASSNAME
    STAMP_INIT_CLASSNAME = ["""data:json
    {                        
        [
            "file": "__init.py"
            "class": None:boolnqt
            ]
    }
    """]
class superobj():
    global text
    def digitFalseTextOutput():
        try:
            rp(f"{(text)}")
            rp(f"{chr(text)}")
            rp(f"{id(text)}")
            rp(f"{hash(text)}")
            rp(f"{ascii(text)}")
            rp(f"{repr(text)}")
            rp(f"{dict(text)}")
            rp(f"{list(text)}")
            rp(f"{tuple(text)}")
            rp(f"{ord(text)}")
            rp(f"{callable(text)}")
            rp(f"{type(text)}")
            rp(f"{str(text)}")
        except Exception:
            pass
    def superobj(text=str):
        text = text
        if text.isdigit() == True:
            try:
                rp(f"{len(text)}")
                rp(f"{float(text)}")
                rp(f"{bin(text)}")
                rp(f"{oct(text)}")
                rp(f"{hex(text)}")            
                rp(f"{abs(text)}")
                rp(f"{complex(text)}")
                rp(f"{divmod(text)}")
                rp(f"{math.cos(text)}")
                rp(f"{math.cosh(text)}")
                rp(f"{math.sin(text)}")
                rp(f"{math.sinh(text)}")
                rp(f"{math.ceil(text)}")
                rp(f"{math.floor(text)}")
                rp(f"{math.tan(text)}")
                rp(f"{math.atan(text)}")
                rp(f"{math.atanh(text)}")
                rp(f"{math.acos(text)}")
                rp(f"{math.acosh(text)}")
                rp(f"{math.asin(text)}")
                rp(f"{math.asinh(text)}")
                rp(f"{math.sqrt(text)}")
                rp(f"{math.isnan(text)}")
                rp(f"{math.isfinite(text)}")
                rp(f"{math.isinf(text)}")
                rp(f"{math.exp(text)}")
                rp(f"{math.log(text)}")
                rp(f"{math.log10(text)}")
                rp(f"{math.log2(text)}")
                rp(f"{cmath.phase(text)}")
                rp(f"{math.degrees(text)}")
                rp(f"{math.radians(text)}")
                rp(f"{math.fabs(text)}")
                rp(f"{math.ulp(text)}")
                rp(f"{math.modf(text)}")
                rp(f"{math.trunc(text)}")
                digitFalseTextOutput()
            except KeyboardInterrupt:
                pass
            finally:
                pass
        elif text.isdigit() == False:
            digitFalseTextOutput()
        else:
            pass
        def digitFalseTextOutput():
            try:
                int(text)
                float(text)
                rp(f"{(text)}")
                rp(f"{chr(text)}")
                rp(f"{id(text)}")
                rp(f"{hash(text)}")
                rp(f"{ascii(text)}")
                rp(f"{repr(text)}")
                rp(f"{dict(text)}")
                rp(f"{list(text)}")
                rp(f"{tuple(text)}")
                rp(f"{ord(text)}")
                rp(f"{callable(text)}")
                rp(f"{type(text)}")
                rp(f"{str(text)}")
            except Exception:
                pass
class __jsonconf__:
    @staticmethod
    def jsonconf(filepath=None, data=None, key=None, default=None):
        if filepath is None or not isinstance(filepath, str) or not filepath.lower().endswith(".conf.json"):
            raise ValueError("File must use the '.conf.json' format and a valid filepath.")
        if data is not None and isinstance(data, dict):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            return
        _D = {}
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    _D = json.load(f)
            except json.JSONDecodeError:
                _D = {}
        data = _D
        if key is not None and isinstance(key, str):
            return data.get(key, default)
        rp(data)
    mlock = []
    @staticmethod
    def addMem(mem):
        mem = mem
        __msrv__.mlock.append(str(mem))
    @staticmethod
    def delMem(index):
        index = index
        identifier = identifier
        identifier = index
        identifier = identifier
        if isinstance(identifier, int) and 0 <= identifier < len(__msrv__.mlock):
            del __msrv__.mlock[identifier]
            rp(f"memsrv: msrv: success deleting index {identifier}")
        else:
            try:
                __msrv__.mlock.remove(str(identifier))
                rp(f"memsrv: msrv: success deleting item by value: {identifier}")
            except ValueError:
                rp(f"memsrv: msrv: error: Item '{identifier}' not found. .stderr")
    @staticmethod
    def resetMem():
        __msrv__.mlock = []
    @staticmethod
    def srv():
        if not __msrv__.mlock:
            rp("memsrv: msrv: server mlock empty.")
            return
        for index, item in enumerate(__msrv__.mlock):
            rp(f"[{index}]/{item}")#idx/itmname
class __msrv__:
    mlock = []
    @staticmethod
    def addMem(mem):
        mem = mem
        __msrv__.mlock.append(str(mem))
    @staticmethod
    def delMem(index):
        index = index
        identifier = identifier
        identifier = index
        identifier = identifier
        if isinstance(identifier, int) and 0 <= identifier < len(__msrv__.mlock):
            del __msrv__.mlock[identifier]
            rp(f"memsrv: msrv: success deleting index {identifier}")
        else:
            try:
                __msrv__.mlock.remove(str(identifier))
                rp(f"memsrv: msrv: success deleting item by value: {identifier}")
            except ValueError:
                rp(f"memsrv: msrv: error: Item '{identifier}' not found. .stderr")
    @staticmethod
    def resetMem():
        __msrv__.mlock = []
    @staticmethod
    def srv():
        if not __msrv__.mlock:
            rp("memsrv: msrv: server mlock empty.")
            return
        for index, item in enumerate(__msrv__.mlock):
            rp(f"[{index}]/{item}")#idx/itmname
class TimestampError(Exception): pass
class Tara:
    def tara(year=2025, month=1, day=1, hour=0):
        return join3.join3(month, year, edit.join(day, hour))
    def rtara(year=2025, month=1, day=1, hour=1):
        _RT = join3.join3(month, year, edit.join(day, hour))
class _history:
    history = []
    def add(cmd=str):
        _history.history += [str(cmd)]
    def show():
        if not _history.history:
            rp("history: empty")
            return
        for i, item in enumerate(_history.history):
            rp(f"[{i}] {item}")
    def get(index=int):
        if 0 <= index < len(_history.history):
            return _history.history[index]
        rp(f"history: invalid index {index}")
    def export(file=str, end="\n", endOnNewline=True):
        if not _history.history:
            rp("history: nothing to export")
            return
        _export._export(data="\n".join(_history.history), file=file, end=end, endOnNewline=endOnNewline)
        rp(f"history: exported {len(_history.history)} items to {file}")
class _kvstore:
    store = {}
    def set(key=str, value=str):
        _kvstore.store[str(key)] = str(value)
        rp(f"kvstore: set {key}={value}")
    def get(key=str):
        if key in _kvstore.store:
            return _kvstore.store[key]
        rp(f"kvstore: {key} not found")
    def delete(key=str):
        if key in _kvstore.store:
            del _kvstore.store[key]
            rp(f"kvstore: deleted {key}")
        else:
            rp(f"kvstore: {key} not found")
    def list():
        if not _kvstore.store:
            rp("kvstore: empty")
            return
        for k, v in _kvstore.store.items():
            rp(f"{k}: {v}")
    def export(file=str, end="\n", endOnNewline=True):
        lines = [f"{k}={v}" for k, v in _kvstore.store.items()]
        _export._export(data="\n".join(lines), file=file, end=end, endOnNewline=endOnNewline)
        rp(f"kvstore: exported {len(lines)} items to {file}")
class _transfer:
    def _transfer(item, source, target):
        if item in source:
            target.append(item)
            source.remove(item)
            rp(f"transferred {item} from source -> target")
        else:
            rp(f"error: {item} not found in source")
class _ttransfer:
    def _mv(src, dest):
        shutil.move(src, dest)
        rp(f"moved {src} -> {dest}")
    def _cp(src, dest):
        shutil.copy(src, dest)
        rp(f"copied {src} -> {dest}")
    def _dupl_file_wprefix(file, prefix):
        dirname, basename = os.path.split(file)
        newname = os.path.join(dirname, prefix + basename)
        shutil.copy(file, newname)
        rp(f"duplicated {file} -> {newname}")
    def _dupl_file_wsuffix(file, suffix):
        dirname, basename = os.path.split(file)
        name, ext = os.path.splitext(basename)
        newname = os.path.join(dirname, name + suffix + ext)
        shutil.copy(file, newname)
        rp(f"duplicated {file} -> {newname}")
class _chunk:
    def chunk(text=str, chunksize=int):
        text = str(text)
        chunksize = int(chunksize)
        total_len = len(text)
        total_chunks = (total_len + chunksize - 1) // chunksize
        start = 0
        current_chunk = 1
        while start < total_len:
            end = start + chunksize
            rp(f"[{current_chunk}/{total_chunks}]\n {text[start:end]}")
            start += chunksize
            current_chunk += 1
            if start < total_len:
                f = input("-- More? --")
                if f != "":
                    break
class Astray:
    astraylock = []
    def _astray(x, y):
        atx = str(x)
        aty = str(y)
        atz = x + y
        atw = int(atz) + int(x) + int(y)
        Astray.astraylock.append(atw)
        return atw
    def _show_astray():
        for i, val in enumerate(Astray.astraylock):
            rp(f"[{i}] {val}")
#helperclass::__calc_hcl__//next
class __calc_hcl__:
    @staticmethod
    def calc_hfc(number, number2, operatorIsPlus=None, operatorIsSubtract=None, operatorIsTimes=None, operatorIsDivide=None, operatorIsExponent=None, operatorIsFloorDivision=None):
        number = number
        number2 = number2
        operatorIsPlus = operatorIsPlus
        operatorIsSubtract = operatorIsSubtract
        operatorIsTimes = operatorIsTimes
        operatorIsDivide = operatorIsDivide
        operatorIsExponent = operatorIsExponent
        operatorIsFloorDivision = operatorIsFloorDivision
        if number2 == 0 and (operatorIsDivide or operatorIsFloorDivision):
            raise ZeroDivisionError("Cannot divide by zero.")
        if operatorIsPlus:
            return number + number2
        elif operatorIsSubtract:
            return number - number2
        elif operatorIsTimes:
            return number * number2
        elif operatorIsDivide:
            return number / number2
        elif operatorIsExponent:
            return number ** number2
        elif operatorIsFloorDivision:
            return number // number2
        else:
            rp("Error: No valid operator flag was set.")
            return None
class adverr:
    #adverr.palette
    #36 errors for advanced error (adverr)
    def e0(self): rp("\nadvout::errcode 0::KeyboardInterrupt")
    def e1(self): rp("\nadvout::errcode 1::NotADirectoryError")
    def e2(self): rp("\nadvout::errcode 2::FileNotFoundError")
    def e3(self): rp("\nadvout::errcode 3::PermissionError")
    def e4(self): rp("\nadvout::warncode 4::DeprecationWarning")
    def e5(self): rp("\nadvout::errcode 5::NotImplementedError")
    def e6(self): rp("\nadvout::errcode 6::LookupError")
    def e7(self): rp("\nadvout::errcode 7::ValueError")
    def e8(self): rp("\nadvout::errcode 8::TypeError")
    def e9(self): rp("\nadvout::errcode 9::OSError")
    def e10(self): rp("\nadvout::errcode 10::IOError")
    def e11(self, e): rp(f"\nadvout::errcode 11::ImportError//Import::{e}")
    def e12(self, e): rp(f"\nadvout::errcode 12:CalledProcessError//{e}")
    def e13(self): rp(f"\nadvout::errcode 13::SystemError")
    def e14(self): rp(f"\nadvout::errcode 14::SyntaxError")
    def e15(self): rp(f"\nadvout::errcode 15::MemoryError")
    def e16(self): rp(f"\nadvout::errcode 16::OverflowError")
    def e17(self): rp(f"\nadvout::warncode 17::SyntaxWarning")
    def e18(self): rp(f"\nadvout::errcode 18::TimestampError")
    def e19(self): rp(f"\nadvout::errcode 19:AttributeError")
    def e20(self): rp(f"\nadvout::errcode 20::WindowsError")
    def e21(self): rp(f"\nadvout::errcode 21::IndexError")
    def e22(self): rp(f"\nadvout::errcode 22::IndentationError")
    def e23(self): rp(f"\nadvout::errcode 23::KeyError")
    def e24(self): rp("\nadvout::errcode 24::UnicodeError")
    def e25(self): rp("\nadvout::errcode 25::UnicodeEncodeError")
    def e26(self): rp("\nadvout::errcode 26::UnicodeDecodeError")
    def e27(self): rp("\nadvout::errcode 27::UnicodeTranslateError")
    def e28(self): rp("\nadvout::warncode 28::UnicodeWarning")
    def e29(self): rp("\nadvout::errcode 29::EnvironmentError")
    def e30(self): rp("\nadvout::errcode 30::ConnectionResetError")
    def e31(self): rp("\nadvout::errcode 31::ConnectionError")
    def e32(self): rp("\nadvout::errcode 32::ConnectionAbortedError")
    def e33(self): rp("\nadvout::errcode 33::ConnectionRefusedError")
    def e34(self): rp("\nadvout::errcode 34::TimeoutError")
    def e35(self, e): rp(f"\nadvout::errcode 35:Exception//{e}")

class advout:
    def advout(cmd=str, dir=str):
        dir = dir
        cmd = cmd
        cmdstarter = f"start cmd /k cd /d {dir} && "
        fcmd = cmdstarter + cmd
        try: subprocess.run(fcmd, shell=True)
        except KeyboardInterrupt: adverr.e0()
        except NotADirectoryError: adverr.e1()
        except FileNotFoundError: adverr.e2()
        except PermissionError: adverr.e3
        except DeprecationWarning: adverr.e4()
        except NotImplementedError: adverr.e5()
        except LookupError: adverr.e6()
        except ValueError: adverr.e7()
        except TypeError: adverr.e8()
        except OSError: adverr.e9()
        except IOError: adverr.e10()
        except ImportError as e: adverr.e11(e)
        except subprocess.CalledProcessError as e: adverr.e12()
        except SystemError: adverr.e13()
        except SyntaxError: adverr.e14()
        except MemoryError: adverr.e15()
        except OverflowError: adverr.e16()
        except SyntaxWarning: adverr.e17()
        except TimestampError: adverr.e18()
        except AttributeError: adverr.e19()
        except WindowsError: adverr.e20()
        except IndexError: adverr.e21()
        except IndentationError: adverr.e22()
        except KeyError: adverr.e23()
        except UnicodeError: adverr.e24()
        except UnicodeEncodeError: adverr.e25()
        except UnicodeDecodeError: adverr.e26()
        except UnicodeTranslateError: adverr.e27()
        except UnicodeWarning: adverr.e28()
        except EnvironmentError: adverr.e29()
        except ConnectionResetError: adverr.e30()
        except ConnectionError: adverr.e31()
        except ConnectionAbortedError: adverr.e32()
        except ConnectionRefusedError: adverr.e33()
        except TimeoutError: adverr.e34()
        except Exception as e: adverr.e35(e)
class advin:
    def input(input=str, prompt=str, newline=None, exit=None):
        advinlock = []
        exit = exit
        newline = newline
        prompt = prompt
        advinlock.append(f"{advin.prompt}\n{advin.input}")
        input = input(f"{advin.prompt}")
        try:
            if newline == True:
                rp(f"advin.input::{advin.input}")
                if exit == True:
                    sys.exit()
                else:
                    pass
            elif newline == False:
                rp(f"advin.input::{advin.input}\n")
                if exit == True:
                    sys.exit()
                else:
                    pass
        except KeyboardInterrupt:
            adverr.e0()
        finally:
            sys.exit()
class __cmp__:
    def compare(printCompareOperatorNames=None, operator=str, N1=int, N2=int):
        operator = operator
        N1 = N1
        N2 = N2
        N1 = int(N1)
        N2 = int(N2)#BUGFIX: t was incorrectly set to int(N1)
        if printCompareOperatorNames == True:
            rp(
                f"stamp __cmp__.compare() --help"
                f"operators: lt, gt, loe, goe, eq, ne, rq, aq, se, te, de, xe, fe, or"
                f"operators: <, >, >=, <=, ==, !=, ~=, =+, =-, =*, =/, =^, =//, ||"
                f"lt(<): less than"
                f"gt(>): greater than"
                f"loe(<=): less than or equal to"
                f"goe(>=): greater than or equal to"
                f"eq(==): equal to"
                f"ne(!=): not equal to"
                f"rq(~=): nearly equal to"
                f"aq(=+): is True to when by self and when N1 + N2 both are equal"
                f"se(=-): is True to when by self and when N1 - N2 both are equal" 
                f"te(=*): is True to when by self and when N1 * N2 both are equal"
                f"de(=/): is True to when by self and when N1 / N2 both are equal"
                f"xe(^=): is True to when by self and when N1 ^ N2 both are equal"
                f"xe(=^): is True to when by self and when N1 ^ N2 both are equal"
                f"fe(=//): is True to when by self and when N1 // N2 both are equal"
                f"or(||): is True to when by self and when N1 & N2 both are different"
            )
            if operator == "lt" or "<":
                if N1 < N2:
                    return True
                else:
                    return False
            elif operator == "gt" or ">":
                if N1 > N2:
                    return True
                else:
                    return False
            elif operator == "loe" or "<=":
                if N1 <= N2:
                    return True
                else:
                    return False
            elif operator == "goe" or ">=":
                if N1 >= N2:
                    return True
                else:
                    return False
            elif operator == "eq" or "==":
                if N1 == N2:
                    return True
                else:
                    return False
            elif operator == "ne" or "!=":
                if N1 != N2:
                    return True
                else:
                    return False
            elif operator == "rq" or "~=":
                if N1 == N2:
                    return True
                else:
                    return False
            elif operator == "aq" or "+=":
                if N1 + N2 == N2:
                    return True
                else:
                    return False
            elif operator == "se" or "-=":
                if N1 - N2 == N2:
                    return True
                else:
                    return False
            elif operator == "te" or "*=":
                if N1 * N2 == N2:
                    return True
                else:
                    return False
            elif operator == "de" or "/=":
                if N1 / N2 == N2:
                    return True
                else:
                    return False
            elif operator == "xe" or "^=":
                if N1 ^ N2 == N2:
                    return True
                else:
                    return False
            elif operator == "fe" or "//=":
                if N1 // N2 == N2:
                    return True
                else:
                    return False
            elif operator == "or" or "||":
                if N1 & N2 != N2:
                    return True
                else:
                    return False
            else:
                return False
        if printCompareOperatorNames == True:
            rp(
                f"stamp __cmp__.compare() --help"
                f"operators: lt, gt, loe, goe, eq, ne, rq, aq, se, te, de, xe, fe, or"
                f"operators: <, >, >=, <=, ==, !=, ~=, =+, =-, =*, =/, =^, =//, ||"
                f"lt(<): less than"
                f"gt(>): greater than"
                f"le(<=): less than or equal to"
                f"ge(>=): greater than or equal to"
                f"eq(==): equal to"
                f"ne(!=): not equal to"
                f"rq(~=): nearly equal to"
                f"aq(=+): is True to when by self and when N1 + N2 both are equal"
                f"se(=-): is True to when by self and when N1 - N2 both are equal" 
                f"te(=*): is True to when by self and when N1 * N2 both are equal"
                f"de(=/): is True to when by self and when N1 / N2 both are equal"
                f"xe(^=): is True to when by self and when N1 ^ N2 both are equal"
                f"fe(=//): is True to when by self and when N1 // N2 both are equal"
                f"or(||): is True to when by self and when N1 & N2 both are different"
                f"gne(!>): greater or not equal"
                f"lne(!<): less or not equal"
                f"kne(>!): backwards greater or not equal"
                f"dne(<!): backwards less or not equal"
            )
            if operator == "lt" or "<":
                if N1 < N2:
                    return True
                else:
                    return False
            elif operator == "gt" or ">":
                if N1 > N2:
                    return True
                else:
                    return False
            elif operator == "le" or "<=":
                if N1 <= N2:
                    return True
                else:
                    return False
            elif operator == "ge" or ">=":
                if N1 >= N2:
                    return True
                else:
                    return False
            elif operator == "eq" or "==":
                if N1 == N2:
                    return True
                else:
                    return False
            elif operator == "ne" or "!=":
                if N1 != N2:
                    return True
                else:
                    return False
            elif operator == "rq" or "~=":
                if N1 == N2:
                    return True
                else:
                    return False
            elif operator == "aq" or "+=":
                if N1 + N2 == N2:
                    return True
                else:
                    return False
            elif operator == "se" or "-=":
                if N1 - N2 == N2:
                    return True
                else:
                    return False
            elif operator == "te" or "*=":
                if N1 * N2 == N2:
                    return True
                else:
                    return False
            elif operator == "de" or "/=":
                if N1 / N2 == N2:
                    return True
                else:
                    return False
            elif operator == "xe" or "^=":
                if N1 ^ N2 == N2:
                    return True
                else:
                    return False
            elif operator == "fe" or "//=":
                if N1 // N2 == N2:
                    return True
                else:
                    return False
            elif operator == "or" or "||":
                if N1 & N2 != N2:
                    return True
                else:
                    return False
            elif operator == "gne" or "!>":
                if N1 > N2 and N1 != N2:
                    return True
                else:
                    return False
            elif operator == "lne" or "!<":
                if N1 < N2 and not f"{N2}":
                    return True
                else:
                    return False
            elif operator == "kne" or ">!":
                if N1 != N2 and N2 > N1:
                    return True
                else:
                    return False
            elif operator == "dne" or "<!":
                if N1 != N2 and N2 < N1:
                    return True
                else:
                    return False
            else:
                return False
        elif printCompareOperatorNames not in (False or True or None):
            if operator in ("lt", "<"): 
                return N1 < N2
            elif operator in ("gt", ">"): 
                return N1 > N2
            elif operator in ("le", "<=", "loe"): 
                return N1 <= N2
            elif operator in ("ge", ">=", "goe"): 
                return N1 >= N2
            elif operator in ("eq", "=="): 
                return N1 == N2
            elif operator in ("ne", "!="): 
                return N1 != N2
            elif operator in ("rq", "~="):
                return N1 == N2 
            elif operator in ("aq", "+="):
                return (N1 + N2) == N2
            elif operator in ("se", "-="):
                return (N1 - N2) == N2
            elif operator in ("te", "*="):
                return (N1 * N2) == N2
            elif operator in ("de", "/="):
                return (N1 / N2) == N2
            elif operator in ("xe", "^=", "e^"):
                return (N1 ^ N2) == N2
            elif operator in ("fe", "//="):
                return (N1 // N2) == N2
            elif operator in ("or", "||"):
                return (N1 & N2) != N2
            elif operator in ("gne", "!>"):
                return N1 > N2 and N1 != N2
            elif operator in ("lne", "!<"):
                return N1 < N2 and N1 != N2#BUGFIX: Original logic was complex, simplified to be less than and not equal
            elif operator in ("kne", ">!"):
                return N1 != N2 and N2 > N1
            elif operator in ("dne", "<!"):
                return N1 != N2 and N2 < N1
        else:
            return False
        
        # REFACTOR: Simplified boolean check
        if printCompareOperatorNames not in (False, True, None):
            rp("[bold red]compare: [/][bold]argholder: [/]rpCompareOperatorNames is not False, True, or None")
class pdec:
    def pdec(i1, i2, returnOutput=None):
        if returnOutput == True:
            i1 = str(i1)
            i2 = str(i2)
            if not i1.isdigit(): raise ValueError(f"Integer part (i1) must contain only non-negative digits and non-alpha or symbol/s/both, got: '{i1}'")
            if not i2.isdigit(): raise ValueError(f"Fractional part (i2) must contain only non-negative digits and non-alpha or symbol/s/both, got: '{i2}'")
            fconstructor = f"{i1}.{i2}"
            return float(fconstructor)#NOTE: REFU to use try-except(-finally)
        elif returnOutput == False:
            i1 = str(i1)
            i2 = str(i2)
            if not i1.isdigit(): raise ValueError(f"Integer part (i1) must contain only non-negative digits and non-alpha or symbol/s/both, got: '{i1}'")
            if not i2.isdigit(): raise ValueError(f"Fractional part (i2) must contain only non-negative digits and non-alpha or symbol/s/both, got: '{i2}'")
            fconstructor = f"{i1}.{i2}"
            return float(fconstructor)#NOTE: REFU to use try-except(-finally)
        elif returnOutput == None: raise SyntaxError("expected True-False, got None")
        else: raise SyntaxError(f"expected bool, got non-bool/None")#NOTE: non-reg
class __exf__:
    def expython(file=str):
        file = file
        if sys.platform.startswith("win"):
            try:
                cmdstring = ["start", "cmd", "/k", sys.executable, f"{file}"]
                subproccess.run(cmdstring, shell=True, check=True)
            except KeyboardInterrupt: adverr.e0()
            except NotADirectoryError: adverr.e1()
            except FileNotFoundError: adverr.e2()#IMPORTANT for not found errors
            except PermissionError: adverr.e3
            except DeprecationWarning: adverr.e4()
            except NotImplementedError: adverr.e5()
            except LookupError: adverr.e6()
            except ValueError: adverr.e7()
            except TypeError: adverr.e8()
            except OSError: adverr.e9()
            except IOError: adverr.e10()
            except ImportError as e: adverr.e11(e)
            except subprocess.CalledProcessError as e: adverr.e12()
            except SystemError: adverr.e13()
            except SyntaxError: adverr.e14()
            except MemoryError: adverr.e15()
            except OverflowError: adverr.e16()
            except SyntaxWarning: adverr.e17()
            except TimestampError: adverr.e18()
            except AttributeError: adverr.e19()
            except WindowsError: adverr.e20()
            except IndexError: adverr.e21()
            except IndentationError: adverr.e22()
            except KeyError: adverr.e23()
            except UnicodeError: adverr.e24()
            except UnicodeEncodeError: adverr.e25()
            except UnicodeDecodeError: adverr.e26()
            except UnicodeTranslateError: adverr.e27()
            except UnicodeWarning: adverr.e28()
            except EnvironmentError: adverr.e29()
            except ConnectionResetError: adverr.e30()
            except ConnectionError: adverr.e31()
            except ConnectionAbortedError: adverr.e32()
            except ConnectionRefusedError: adverr.e33()
            except TimeoutError: adverr.e34()
            except Exception as e: adverr.e35(e)
class __cd__:
    def cd(path=str):
        path = path
        try:
            os.chdir(path)
            rp(f"__cd__.cd()::{os.getcwd()}:Change|Directory")
        except FileNotFoundError:
            adverr.e2()
        except NotADirectoryError:
            adverr.e1()
        except PermissionError:
            adverr.e3()
        except Exception as e:
            adverr.e35(e)
class tconstant:
    def typeToConstant(name=str):
        name = str(name)
        return name.upper()
class tlist:
    def typeToList(name=str):
        name = list(name)
        return name
class Type:
    def constant(name=str):
        tconstant.typeToConstant(name)
    def list(name=str):
        tlist.typeToList(name)
    def type(tstr=str):
        tstr = str(tstr)
        if tconstant.typeToConstant(tstr) == tstr:
            rp("constant")
        elif tlist.typeToList(tstr) == tstr:
            rp("list")
        else:
            rp("unknown")
    def flt(file=str):
        file = file
        if os.path.exists(file):
            if os.path.isfile(file):
                rp(f"file: {file}")
            elif os.path.isdir(file):
                rp(f"directory: {file}")
            else:
                rp(f"unknown: {file}")
        else:
            rp(f"not found: {file}")
    def btype(name=str, useDoubleQuotes=None):
        name = name
        useDoubleQuotes = useDoubleQuotes
        if name == str(name):
            if useDoubleQuotes == True:
                return f"String\"{name}\""
            else:
                return f"String'{name}'"
        try:
            if name == int(name):
                if useDoubleQuotes == True:
                    return f"Integer\"{name}\""
                else:
                    return f"Integer'{name}'"
        except ValueError:
            adverr.e7()
        if name == list(name):
            if useDoubleQuotes == True:
                return f"List\"{name}\""
            else:
                return f"List'{name}'"
        if name == tuple(name):
            if useDoubleQuotes == True:
                return f"List\"{name}\""
            else:
                return f"List'{name}'"
        if name == name:
            if useDoubleQuotes == True:
                return f"Self\"{name}\""
            else:
                return f"Self'{name}'"
class UnknownAdverrIntError(Exception): pass#GENERAL
class Control:
    def ct(adverrErrorInt=int, e=str):
        if adverrErrorInt == 0: adverr.e0()        
        elif adverrErrorInt == 1: adverr.e1()
        elif adverrErrorInt == 2: adverr.e2()
        elif adverrErrorInt == 3: adverr.e3()
        elif adverrErrorInt == 4: adverr.e4()
        elif adverrErrorInt == 5: adverr.e5()
        elif adverrErrorInt == 6: adverr.e6()
        elif adverrErrorInt == 7: adverr.e7()
        elif adverrErrorInt == 8: adverr.e8()
        elif adverrErrorInt == 9: adverr.e9()
        elif adverrErrorInt == 10: adverr.e10()
        elif adverrErrorInt == 11: adverr.e11(f"{e}")
        elif adverrErrorInt == 12: adverr.e12(f"{e}")
        elif adverrErrorInt == 13: adverr.e13()
        elif adverrErrorInt == 14: adverr.e14()
        elif adverrErrorInt == 15: adverr.e15()
        elif adverrErrorInt == 16: adverr.e16()
        elif adverrErrorInt == 17: adverr.e17()
        elif adverrErrorInt == 18: adverr.e18()
        elif adverrErrorInt == 19: adverr.e19()
        elif adverrErrorInt == 20: adverr.e20()
        elif adverrErrorInt == 21: adverr.e21()
        elif adverrErrorInt == 22: adverr.e22()
        elif adverrErrorInt == 23: adverr.e23()
        elif adverrErrorInt == 24: adverr.e24()
        elif adverrErrorInt == 25: adverr.e25()
        elif adverrErrorInt == 26: adverr.e26()
        elif adverrErrorInt == 27: adverr.e27()
        elif adverrErrorInt == 28: adverr.e28()
        elif adverrErrorInt == 29: adverr.e29()
        elif adverrErrorInt == 30: adverr.e30()
        elif adverrErrorInt == 31: adverr.e31()
        elif adverrErrorInt == 32: adverr.e32()
        elif adverrErrorInt == 33: adverr.e33()
        elif adverrErrorInt == 34: adverr.e34()
        elif adverrErrorInt == 35: adverr.e35(f"{e}")
        else:
            raise UnknownAdverrIntError(f"ct adverrint {adverrErrorInt} unknown. Errors range from 0 to 35 (total 36).")
class Debug:
    def debug(dbgmsg=str, lower=None):
        if lower == True:
            odmsg = dbgmsg
            dgbmsg = f"DEBUG {odmsg}".lower()
            rp(dgbmsg)
        elif lower == (
            False or None
            ):
            odmsg = dbgmsg
            dgbmsg = f"DEBUG {odmsg}"
            rp(dgbmsg)
    def info(infomsg=str, lower=None):
        if lower == True:
            odmsg = infomsg
            infomsg = f"INFO {odmsg}".lower()
        elif lower == (
            False or None
            ):
            odmsg = infomsg
            infomsg = f"INFO {odmsg}"
            rp(infomsg)
    def warn(warnmsg=str, lower=None):
        if lower == True:
            odmsg = warnmsg
            warnmsg = f"WARN {odmsg}".lower()            
            rp(warnmsg)
        elif lower == (
            False or None
            ):
            odmsg = warnmsg
            warnmsg = f"WARN {odmsg}"
            rp(warnmsg)
    def error(errmsg=str, lower=None):
        if lower == True:
            odmsg = errmsg
            errmsg = f"ERROR {odmsg}".lower()
            rp(errmsg)
        elif lower == (
            False or None
            ):
            odmsg = errmsg
            errmsg = f"ERROR {odmsg}"
            rp(errmsg)
    def critical(critmsg=str, lower=None):
        if lower == True:
            odmsg = critmsg
            critmsg = f"CRITICAL {odmsg}".lower()
            rp(critmsg)
        elif lower == (
            False or None
            ):
            odmsg = critmsg
            critmsg = f"CRITICAL {odmsg}"
            rp(critmsg)
    def custom(errname=str, errmsg=str, capital=None):
        if capital == True:
            odmsg = errmsg
            errmsg = f"{errname} {odmsg}".upper()
        elif capital == False:
            odmsg = errmsg
            errmsg = f"{errname} {odmsg}".lower()
        else:
            odmsg = errmsg
            errmsg = f"{errname} {odmsg}"
        rp(errmsg)
class DirectoryExistsError(Exception): pass#GENERAL, not in adverr yet
class ArgumentError(Exception): pass#GENERAL, not in adverr yet
class _export:
    def _export(data=str, end=str, file=str, endOnNewline=None):
        try:
            with open(file, "x", encoding="utf-8") as f:
                if endOnNewline == True:
                    f.write(data + f"\n{end}")
                else:
                    f.write(data + end)
        except OSError:
            adverr.e9()
        except IsADirectoryError:
            raise IsADirectoryError("_export: isdir")#TODO: no custom IsADirectoryError in adverr yet
class _import:
    def _import(file=str):
        file = file
        try: 
            with open(file, "r", encoding="utf-8") as f: return f.read()
        except FileNotFoundError: adverr.e2()
        except IsADirectoryError: raise IsADirectoryError(f"IsADirectory: {str(file)}")#TODO: no custom IsADirectoryError in adverr yet
class _mkdir:
    def _mkdir(path=str):#no combining modes
        try:
            os.mkdir(path)
        except DirectoryExistsError:
            rp(f"directory already exists: {str(path)}")
class _mkfile():
    def _mkfile(path=str, text=str, xmode=None, amode=str, wmode=str, end=str, endOnNewline=None):
        if (
            xmode == True,
            amode == False or None,
            wmode == False or None
            ):
            try:
                with open(path, "x") as f:
                    if endOnNewline == True:
                        f.write(text + f"\n{end}")
                    else:
                        f.write(text + end)
            except OSError:
                adverr.e9()
        elif (
                xmode == False or None,
                amode == True,
                wmode == False or None
            ):
            try:
                with open(path, "a") as f:
                    if endOnNewline == True:
                        f.write(text + f"\n{end}")
                    else:
                        f.write(text + end)
            except OSError:
                adverr.e9()
        elif (
                xmode == False or None,
                amode == False or None,
                wmode == True
            ):
            try:
                with open(path, "w") as f:
                    if endOnNewline == True:
                        f.write(text + f"\n{end}")
                    else:
                        f.write(text + end)
            except OSError:
                adverr.e9()
        else: raise ArgumentError("expected 7 (7) arguments (non-optional)")#not in adverr yet
class _note:
    def _note(note=str):
        notelock += [f"{note}"]
        return note
class _notes:
    notelock = []
    def _get_notes():
        return _note.notelock
class _cl:
    def _cl():
        if sys.platform.startswith('win'):
            os.system('cls')
        else:
            os.system('clear')
global lock
class _lock:
    def _add(item=str):
        lock = []
        lock += [f"{item}"]
    def _delindex(index=int, balanceIndex=None):
        index = int(index)
        balanceIndex = balanceIndex
        lock = []
        if balenceIndex == True:
            balanceIndex = balanceIndex
            del lock[index - 1]
        else:
            del lock[index]
# section: cmgr
class _ConfigValue:
    def __init__(self, value=None):
        self.value = value
    def set(self, value):
        self.value = value
    def get(self):
        return self.value
    def __str__(self):
        return str(self.value)
#create instances of the config value holder.
#this achieves the goal of having simple, named value containers.
S1, S2 = _ConfigValue(), _ConfigValue()
C1, C2 = _ConfigValue(), _ConfigValue()
K1, K2 = _ConfigValue(), _ConfigValue()
T1, T2 = _ConfigValue(), _ConfigValue()
L1, L2 = _ConfigValue(), _ConfigValue()
R1, R2 = _ConfigValue(), _ConfigValue()
temp = _ConfigValue()
# sectend: cmgr
class taskmgr:
    def _launch():
        if sys.platform.startswith("win"): subprocess.run("start taskmgr.exe", shell=True)
        else: print("unavail for non-windows systems")
class edit:
    def join(W1=str, W2=str):
        W1 = str(W1)
        W2 = str(W2)
        return f"{W1}" + f"{W2}"
    def rjoin(W1=str, W2=str):
        W1 = str(W1)
        W2 = str(W2)
        return f"{W1}" + f"{W2}"
    def split(text=str, splitby=str):
        text = text
        splitby = splitby
        return text.split(splitby)
    def upper(text=str):
        text = text
        return text.upper()
    def lower(text=str):
        text = text
        return text.lower()
    def replace(text=str, old=str, new=str):
        text = text
        old = old
        new = new
        return text.replace(old, new)
    def find(text=str, find=str):
        text = text
        find = find
        return text.find(find)
    def count(text=str, count=str):
        text = text
        count = count
        return text.count(count)
    def startswith(text=str, startswith=str):
        text = text
        startswith = startswith
        return text.startswith(startswith)
    def endswith(text=str, endswith=str):
        text = text
        endswith = endswith
        return text.endswith(endswith)
    def isalpha(text=str):
        text = text
        return text.isalpha()
    def isdigit(text=str):
        text = text
        return text.isdigit()
    def isalnum(text=str):
        text = text
        return text.isalnum()
    def isspace(text=str):
        text = text
        return text.isspace()
    def islower(text=str):
        text = text
        return text.islower()
    def isupper(text=str):
        text = text
        return text.isupper()
    def title(text=str):
        text = text
        return text.title()
    def capitalize(text=str):
        text = text
        return text.capitalize()
    def swapcase(text=str):
        text = text
        return text.swapcase()
    def zfill(text=str, width=int):
        text = text
        width = width
        return text.zfill(width)
    def strip(text=str, chars=None):
        text = text
        chars = chars
        return text.strip(chars)
    def reverse(text=str):
        return text[::-1]

    def camel_case(text=str):
        words = text.split()
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    def snake_case(text=str):
        words = text.split()
        return '_'.join(word.lower() for word in words)
class Unite:
    def unite(O1=str, O2=str):
        return f"{O1}::{O2}"
class Kit:
    def kit(U1=str, U2=str):
        return f"{U1}:{U2}"
class Abomination:
    def abomb(P1, P2):
        return f"{P1}//{P2}"
class Angle:
    def angle(I1, I2):
        return f"{I1}={I2}"
class Alias:
    def _new(fullname=str, capital=None, returnOutput=None):
        global _ExportHelper
        fullname = fullname
        fchar = fullname[0]
        lchar = fullname[-1]
        rlock = []
        if capital == True:
            rlock += [f"{fchar + lchar}".upper()]
            if returnOutput == True:
                _ExportHelper = fchar.upper() + lchar.upper()
                return fchar.upper() + lchar.upper()
            elif returnOutput == False:
                _ExportHelper = fchar.upper() + lchar.upper()
        else:
            rlock += [f"{fchar + lchar}"]
            if returnOutput == True:
                _ExportHelper = fchar.upper() + lchar.upper()
                return fchar + lchar
            elif returnOutput == False:
                _ExportHelper = fchar.upper() + lchar.upper()
    def _export(file=str):
        _ExportHelper = _ExportHelper
        file = file
        _export._export(file=f"{file}", data=f"{_ExportHelper}", end="\n", endOnNewline=False)
class __isin__:
    def isin(inwhat=str, whatToSearch=str):
        inwhat = []
        inwhat = [inwhat]
        if whatToSearch in inwhat[0]:
            return True
        else:
            return False
class __log__:
    def log(text=str, file=str, end=str):
        try:
            with open(f"{file}", "x") as f:
                f.write(f"{text}" + f"{end}")
        except IsADirectoryError:
            raise IsADirectoryError("log: isdir")
        except OSError:
            adverr.e9()
        except KeyboardInterrupt:
            raise KeyboardInterrupt(f"{Unite.unite(O1="log", O2="logwriter")}: KeyboardInterrupt[LogwriteCorruption]")
class Royal:
    def _royal(w=int, x=int, y=int, z=str):
        e = math.e
        w = int(w)
        x = int(x)
        y = int(y)
        z = str(z)
        val = (len(z) * (x + y) + int(e * w)) / (w or 1)
        f = (math.pi / (val or 1)) + (e * random.randint(3, 21))
        return f
    def _royalc(w=int, x=int, y=int, z=str):
        x = int(x)
        y = int(y)
        z = str(z)
        t = math.sin(w) + math.cos(x) + math.tan(y)
        c = abs(t * len(z) + random.randint(1, 50) / (w or 1))
        f = (math.pi * c) - (math.e * random.randint(2, 9))
        return f
    def _royalq(w=int, x=int, y=int, z=str):
        w = int(w)
        x = int(x)
        y = int(y)
        z = str(z)
        a = abs(math.log(abs((x + 1) * (y + 1))) + (len(z) or 1))
        b = pow(a, random.randint(2, 5)) / (w or 1)
        f = (b * math.e) + math.sqrt(abs(x * y)) + random.uniform(1.1, 9.9)
        return f
class _count_ds:
    def _count_ds(path):
        path = str(path)
        return len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
class _count_subds:
    def _count_subds(path):
        path = str(path)
        return len([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
class _calc:
    def _calc(a,b,op):
        a = float(a)
        b = float(b)
        op = str(op)
        if op == "+": return a+b
        elif op == "-": return a-b
        elif op == "*": return a*b
        elif op == "/": return a/b
        elif op == "%": return a%b
        elif op == "**" or "^": return a**b
        else: raise SyntaxError("operator must be +, -, *, /, %, or (**, ^)")
# section: frozen
class Frozen:
    def __init__(self, name=str, data=None):
        self.name = str(name)
        self._data = data
        self._locked = True
    def get(self):
        return self._data
    def set(self, value):
        if self._locked:
            raise RuntimeError(f"Frozen {self.name}: cannot modify, object is frozen")
        self._data = value
    def unlock(self):
        self._locked = False
    def lock(self):
        self._locked = True
    def is_locked(self):
        return self._locked
    def info(self):
        lock_status = "locked" if self._locked else "unlocked"
        return f"<frozen {self.name}> data: {self._data} ({lock_status})"
    def __repr__(self):
        return f"<frozen {self.name}>"
    def __rld__(self):
        if self._locked == False:
            Frozen.lock()
            Frozen.unlock()
            Frozen.set(f"{Frozen.get()}")
        elif self._locked == True:
            Frozen.unlock()
            Frozen.set(f"{Frozen.get()}")
            Frozen.lock()
        else: raise SyntaxError("expected True-False, got not True-False")
    def __getattr__():
        Frozen.get()
    def __getlen__():
        len(f"{Frozen.get()}")
    def __setattr__(value=str):
        value = str(value)
        Frozen.unlock()
        Frozen.set(value)
    def __ref__(self):
        ref = f"<frozen {self.name}><"
        if bool(Frozen.is_locked._locked) == True: ref += "locked>"
        elif bool(Frozen.is_locked._locked) == False: ref += "unlocked>"
        ref = ref + f"<data {Frozen.get()}><python {platform.python_version}><time {datetime.datetime()}>"
        return ref
# sectend: frozen
class _seed:
    def _seed(seed_value=int):
        random.seed(int(seed_value))
    def _randint(a=int, b=int):
        return random.randint(a, b)
    def _randfloat(a=float, b=float):
        return random.uniform(a, b)
    def _choice(seq=list):
        return random.choice(seq)
    def _shuffle(seq=list):
        seq = list(seq)
        random.shuffle(seq)
        return seq
class _dynvar:
    dynstore = {}
    def _set(name=str, value=str):
        _dynvar.dynstore[str(name)] = value
    def _get(name=str):
        return _dynvar.dynstore.get(str(name))
    def _del(name=str):
        if str(name) in _dynvar.dynstore:
            del _dynvar.dynstore[str(name)]
    def _list():
        return list(_dynvar.dynstore.keys())
    def _reset():
        _dynvar.dynstore = {}
class _link:
    def _link(Path1=str, Path2=str):
        with open(Path2, "a") as f:
            f.write(f"{edit.join(edit.join("", ""))}")
class TimeError(Exception): pass
class ixpd:
    def _exit_on_inactivity_peroid(ttime=int):
            eltime = 0
            for i in range(ttime):
                eltime += 1
                time.sleep(1)
                if eltime == time:
                    sys.exit()
    def _do_on_inactivity_peroid(ttime=int, pyshell=None, cmd=str):
            eltime = 0
            if str(ttime).startswith("-"):
                raise TimeError("time peroid must not be negative")
            for i in time:
                time.sleep(1)
                eltime += 1
                if eltime == range(ttime):
                    if pyshell == True:
                        if sys.platform.startswith("win"):
                            subprocess.run([sys.executable, "-c", cmd], shell=True)
                        else:
                            subprocess.run([sys.executable, "-c", cmd], shell=True)
                    elif pyshell == False:
                        if sys.platform.startswith("win"):
                           subprocess.run(["start", "cmd.exe", "/k", [cmd]], shell=True)
                        else:
                            subprocess.run([cmd], shell=True)
class _uname:
    global ulock
    ulock = []
    def _uname(Z1=str):
        f = "_" + Z1.lower()
        ulock += [f]
        return f
class strint:
    def strint(E1=str, E2=int, sep=str):
        return str(E1) + sep + str(E2)
    def intstr(M1=int, M2=str, sep=str):
        return str(M1) + sep + str(M2)
class _:
	subprocess.run([sys.executable, "_.py"], shell=True)
class __uspcname__:
    def uspc(name=str):
        spi = "__"
        return edit.join(edit.join(name, spi), spi)
class PyInstaller:
    script = ""
    def PyInstaller(script="script.py", onedir=False, onefile=False, icon="icon.ico", name=script, specpath=""):
        command = [sys.executable, "-m", "PyInstaller", "-D", "-F", "icon", icon, script]
        if onedir == False:
            del command[4]
            if onefile == False:
                del command[4]
        else:
            if onefile == False:
                del command[5]
class RangeError(Exception): pass
class join3():
    def join3(I1="item1", I2="item2", I3="item3"):
        return I1 + I2 + I3
class rj3():
    def rj3(J1="item1", J2="item2", J3="item3"):
        _J = J1 + J2 + J3
class HTML:
    def __reset__():
        HTML = ""
    def __run__(htmlfile="new.html", browser="chrome.exe" if os.name == "nt" else "chrome"):
        if os.name == "nt":
            if browser.endswith(".exe") == True:
                subprocess.run([edit.join(browser, edit.join(" ", edit.join("\"", edit.join(htmlfile, "\""))))], shell=True)
            else:
                subprocess.run([edit.join(browser, edit.join(".exe", edit.join(" ", edit.join("\"", edit.join(htmlfile, "\"")))))], shell=True)
        else:
            subprocess.run(f"{browser} \"{htmlfile}\"")
    def __crthtml__(file="new.html", content="""
    <!DOCTYPE html>
    <html>
        <head>
            <title>New Page<title>
        </head>
        <body>
            <p>New Paragraph</p>
        </body>
    </html>
    """
                    ):
        with open(file, "x") as f:
            f.write(HTML)
    def addpar(text="text"):
        HTML += edit.join(edit.join("<p>", text), "</p>")
    def addhead(size=1, text="text"):
        if size == 1:
            HTML += edit.join(edit.join("<h1>", text), "</h1>\n")
        elif size == 2:
            HTML += edit.join(edit.join("<h2>", text), "</h2>\n")
        elif size == 3:
            HTML += edit.join(edit.join("<h3>", text), "</h3>\n")
        elif size == 4:
            HTML += edit.join(edit.join("<h4>", text), "</h4>\n")
        elif size == 5:
            HTML += edit.join(edit.join("<h5>", text), "</h5>\n")
        elif size == 6:
            HTML += edit.join(edit.join("<h6>", text), "</h6>\n")
        else:
            raise RangeError("header range must be from 1 to 6")
    def addtxa(text="textarea", w=20, h=20):
        HTML += edit.join("<textarea width=", edit.join(edit.join(w, " "), edit.join("height=", edit.join(h, edit.join(edit.join(">", text), "</textarea>")))))
    def addelm(name="body", tags="class=\"newclass\"", text="my text"):
        HTML += edit.join("<", edit.join(edit.join(name, edit.join(" ", edit.join(tags, edit.join(">", edit.join(text, edit.join("</", edit.join(name, ">")))))))))
    def addbtn(text="button", onclick=""):
        HTML += join3.join3("<button onclick=\"", onclick, join3.join3("\">", text, "</button>"))
    def addlbl(text="label", forid=""):
        HTML += join3.join3("<label for=\"", forid, join3.join3("\">", text, "</label>"))
    def addipt(type="text", id="", name="", value="", placeholder=""):
        HTML += join3.join3("<input type=\"", type, join3.join3("\" id=\"", id, join3.join3("\" name=\"", name, join3.join3("\" value=\"", value, join3.join3("\" placeholder=\"", placeholder, "\">")))))
    def addlink(href="", text="link"):
        HTML += join3.join3("<a href=\"", href, join3.join3("\">", text, "</a>"))
    def addimg(src="", alt="", width="", height=""):
        HTML += join3.join3("<img src=\"", src, join3.join3("\" alt=\"", alt, join3.join3("\" width=\"", width, join3.join3("\" height=\"", height, "\">"))))
    def addlist(items=[], ordered=False):
        list_tag = "ol" if ordered else "ul"
        list_content = "".join([join3.join3("<li>", item, "</li>") for item in items])
        HTML += join3.join3("<", list_tag, join3.join3(">", list_content, join3.join3("</", list_tag, ">")))
    def adddiv(id="", class_name="", text=""):
        HTML += join3.join3("<div", join3.join3(" id=\"", id, "") if id else "", join3.join3(join3.join3(" class=\"", class_name, "") if class_name else "", ">", join3.join3(text, "</div>", "")))
    def addspan(text="", class_name=""):
        HTML += join3.join3("<span", join3.join3(" class=\"", class_name, "") if class_name else "", join3.join3(">", text, "</span>"))
    def addtable(headers=[], rows=[]):
        header_row = "".join([join3.join3("<th>", header, "</th>") for header in headers])
        table_rows = ""
        for row in rows:
            table_rows += join3.join3("<tr>", "".join([join3.join3("<td>", item, "</td>") for item in row]), "</tr>")
        HTML += join3.join3("<table>", join3.join3("<thead>", join3.join3("<tr>", header_row, "</tr>"), "</thead>"), join3.join3("<tbody>", table_rows, "</tbody>")) + "</table>"
    def addstyle(css=""):
        HTML += join3.join3("<style>\n", css, "</style>\n")
    def addscript(js=""):
        HTML += join3.join3("<script>\n", js, "</script>\n")
    def addmetacset(charset="utf-8"):
        HTML += join3.join3("<meta charset=\"", charset, "\">\n")
    def addlinkcss(href=""):
        HTML += join3.join3("<link rel=\"stylesheet\" href=\"", href, "\">")
    def addtitle(title=""):
        HTML += join3.join3("<title>", title, "</title>")
    def addbody(content=""):
        HTML += join3.join3("<body>", content, "</body>")
    def adddphtml(content=""):
        HTML += join3.join3("<!DOCTYPE html>\n<html>", content, "</html>")
    def addhtml(content=""):
        HTML += join3.join3("<html>", content, "</html>")
class _ShortType:
    def shorttype(name="item", lento=5):
        for i in range(lento):
            _NS += name[:lento]
        return _NS
    def rsht(name="item", lento=5):
        for i in range(lento):
            _PT += name[:lento]
class Error501(Exception):
    """501 ServerError"""
    pass
class Error502(Exception):
    """502 ServerDown"""
    pass
class Error503(Exception):
    """503 ServerDeniedAcess"""
    pass
class Error504(Exception):
    """504 ServerNotFound"""
    pass
class Error505(Exception):
    """505 ServerCodeError"""
    pass
class Error506(Exception):
    """506 ServerReturnedZero"""
    pass
class Error507(Exception):
    """507 ServerTimeout"""
    pass
class Error508(Exception):
    """508 ServerCalledError"""
    pass
class UseDifferentClassError(Exception):
    pass
class Server:
    @staticmethod
    def srv():
        raise UseDifferentClassError("use import stamp.server or from stamp import server, don't use the main file's Server, as is now deprectated.")
class textprocesser:
    def process(text=""):
        text.replace(r"\A", "[")
        text.replace(r"\B", "]")
        text.replace(r"\C", "{")
        text.replace(r"\D", "}")
        text.replace(r"\E", "!")
        text.replace(r"\F", "@")
        text.replace(r"\G", "#")
        text.replace(r"\H", "$")
        text.replace(r"\I", "%")
        text.replace(r"\J", "^")
        text.replace(r"\K", "&")
        text.replace(r"\L", "*")
        text.replace(r"\M", "(")
        text.replace(r"\N", ")")
        text.replace(r"\O", "\\")
        text.replace(r"\P", "|")
        text.replace(r"\Q", "~")
        text.replace(r"\R", "`")
        text.replace(r"\S", ";")
        text.replace(r"\T", ":")
        text.replace(r"\U", "\"")
        text.replace(r"\V", "'")
        text.replace(r"\W", ",")
        text.replace(r"\X", ".")
        text.replace(r"\Y", "<")
        text.replace(r"\Z", ">")
        text.replace(r"/A", "/")
        text.replace(r"/B", "?")
        text.replace(r"/C", "=")
        text.replace(r"/D", "-")
        text.replace(r"/E", "\t")
        text.replace(r"/F", "\n")
        text.replace(r"/G", "\a")
        text.replace(r"/H", "\0")
        text.replace(r"/I", "\\")
        text.replace(r"/J", "\1")
        text.replace(r"/K", "\1")
        text.replace(r"/L", "\2")
        text.replace(r"/M", "\3")
        text.replace(r"/N", "\4")
        text.replace(r"/O", "\5")
        text.replace(r"/P", "\6")
        text.replace(r"/Q", "\7")
        text.replace(r"/R", "")
        return text
class lstamp:
    def _lstamp(month=datetime.datetime.now().strftime("%m"), year=datetime.datetime.now().strftime("%Y"), day=datetime.datetime.now().strftime("%d"), hour=datetime.datetime.now().strftime("%h")): return edit.join(edit.join(month, year), edit.join(day, hour))
    def _rstamp(month=datetime.datetime.now().strftime("%m"), year=datetime.datetime.now().strftime("%Y"), day=datetime.datetime.now().strftime("%d"), hour=datetime.datetime.now().strftime("%h")): _Y = edit.join(edit.join(month, year), edit.join(day, hour))
class specmtdta:
    def mkspec(pub="Publisher", ver="0.1.0", sfname="Software", specf="myproject.st.spec", lang="python", addSpecPrefix=False):
        with open(specf + ".st.spec" if addSpecPrefix == True else specf, "x") as f:
            f.write("[spec]")
            f.write(f"{edit.join("publisher: ", pub)}")
            f.write(f"{edit.join("version: ", ver)}")
            f.write(f"{edit.join("name: ", sfname)}")
            f.write(f"{edit.join("language: ", lang)}")
            f.write(f"[timestamp]\n{lstamp._lstamp}") 
class DeprectatedError(Exception):
    pass
class _rsfd:
    def main(filepath, target):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                source_code = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"file not found: {filepath}")
        tree = ast.parse(source_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == target:
                        return True
            if isinstance(node, ast.ImportFrom):
                if node.module == target:
                    return True
        return False
class tools:
    def A(data={}):
        return data
    def B(data={}):
        _K_AW = data
    def C(data={}, length=10):
        return data[:length]
    def D(data={}, length=10):
        return data[:-length]
    def E(data={}, length=10):
        _K_BW = data[:-length]
    def F(data={}, length=10):
        _K_CW = data[:-length]
    def G(data={}, itemcount=10):
        for i in range(itemcount):
            if i == itemcount:
                break
            else:
                return data[i]
    def H(data={}, itemcount=10):
        _K_DW = {}
        for i in range(itemcount):
            if i == itemcount:
                break
            else:
                _K_DW += data[i]
class repeat:
    def repeat(times=4, code=print("")):
        if callable(code):
            if not int(times) == times:
                raise SyntaxError("number must be int, got other")
            for i in range(times):
                code()
        else:
            raise SyntaxError("code must be callable")
class java:
    """A class to emulate some basic Java syntax and functionality in Python."""
    class System:
        """Emulates the Java System class."""
        class out:
            """Emulates the Java System.out object."""
            @staticmethod
            def println(text=""):
                """Prints the given text followed by a newline, like Java's System.out.println()."""
                print(text)
            @staticmethod
            def print(text=""):
                """Prints the given text without a newline, like Java's System.out.print()."""
                print(text, end="")

    # --- Emulated java.lang Exceptions ---
    class NullPointerException(Exception): pass
    class IllegalArgumentException(Exception): pass
    class IOException(Exception): pass
    class IndexOutOfBoundsException(Exception): pass
    class NumberFormatException(ValueError): pass
    class ParseException(ValueError): pass
    class UnsupportedOperationException(NotImplementedError): pass

    # --- More Emulated java.lang Exceptions ---
    class ArithmeticException(ArithmeticError): pass
    class ClassCastException(TypeError): pass
    class IllegalStateException(Exception): pass
    class SecurityException(Exception): pass
    class NoSuchElementException(KeyError): pass

    # --- Emulated java.util.Calendar ---
    class Calendar:
        """Emulates the Java Calendar class for date/time manipulation."""
        # Constants
        YEAR = 1
        MONTH = 2
        DAY_OF_MONTH = 5
        HOUR_OF_DAY = 11
        MINUTE = 12
        SECOND = 13

        def __init__(self):
            self._dt = datetime.datetime.now()

        @staticmethod
        def getInstance():
            return java.Calendar()

        def get(self, field):
            if field == java.Calendar.YEAR: return self._dt.year
            if field == java.Calendar.MONTH: return self._dt.month - 1 # Java months are 0-11
            if field == java.Calendar.DAY_OF_MONTH: return self._dt.day
            if field == java.Calendar.HOUR_OF_DAY: return self._dt.hour
            if field == java.Calendar.MINUTE: return self._dt.minute
            if field == java.Calendar.SECOND: return self._dt.second
            raise java.IllegalArgumentException("Unsupported field")

        def set(self, *args):
            if len(args) == 2:
                field, value = args
                # This is a simplified version
                if field == java.Calendar.YEAR: self._dt = self._dt.replace(year=value)
                elif field == java.Calendar.MONTH: self._dt = self._dt.replace(month=value + 1)
                elif field == java.Calendar.DAY_OF_MONTH: self._dt = self._dt.replace(day=value)
                else: raise java.IllegalArgumentException("Unsupported field for set")
            elif len(args) == 3:
                self._dt = self._dt.replace(year=args[0], month=args[1]+1, day=args[2])

        def getTime(self):
            return java.Date(self._dt.timestamp() * 1000)

    # --- Emulated java.util.Properties ---
    class Properties:
        """Emulates Java's Properties class for .properties files."""
        def __init__(self):
            self._props = {}

        def getProperty(self, key, defaultValue=None):
            return self._props.get(key, defaultValue)

        def setProperty(self, key, value):
            self._props[key] = value

        def load(self, reader): # reader is a file-like object
            for line in reader:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    self._props[key.strip()] = value.strip()

        def store(self, writer, comments=""): # writer is a file-like object
            if comments:
                writer.write(f"# {comments}\n")
            for key, value in self._props.items():
                writer.write(f"{key}={value}\n")

        def stringPropertyNames(self):
            return set(self._props.keys())

    # --- Emulated java.util.Base64 ---
    class Base64:
        """Emulates Java's Base64 encoder and decoder."""
        @staticmethod
        def getEncoder():
            class Encoder:
                def encodeToString(self, src_bytes):
                    return base64.b64encode(src_bytes).decode('ascii')
            return Encoder()

        @staticmethod
        def getDecoder():
            class Decoder:
                def decode(self, src_str):
                    return base64.b64decode(src_str)
            return Decoder()

    # --- Emulated java.net.URL ---
    class URL:
        """Emulates Java's URL class."""
        def __init__(self, spec):
            from urllib.parse import urlparse
            self._parsed = urlparse(spec)
        def getProtocol(self): return self._parsed.scheme
        def getHost(self): return self._parsed.hostname
        def getPort(self): return self._parsed.port or -1
        def getPath(self): return self._parsed.path
        def getFile(self): return self._parsed.path
        def getQuery(self): return self._parsed.query
        def toExternalForm(self): return self._parsed.geturl()
        def __str__(self): return self.toExternalForm()

    # --- Emulated java.io Streams ---
    class InputStream:
        def read(self): raise java.UnsupportedOperationException()
        def close(self): pass
    class OutputStream:
        def write(self, b): raise java.UnsupportedOperationException()
        def close(self): pass
    class FileInputStream(InputStream):
        def __init__(self, file_obj): # Takes a java.File object
            self._file = open(file_obj.getPath(), 'rb')
        def read(self, b=None): return self._file.read(b)
        def close(self): self._file.close()
    class FileOutputStream(OutputStream):
        def __init__(self, file_obj):
            self._file = open(file_obj.getPath(), 'wb')
        def write(self, b): self._file.write(b)
        def close(self): self._file.close()

    # --- Emulated java.util.Date and java.text.SimpleDateFormat ---
    class Date:
        """Emulates the Java Date class."""
        def __init__(self, millis=None):
            if millis is None:
                self._time = time.time()
            else:
                self._time = millis / 1000.0

        def getTime(self):
            """Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT."""
            return int(self._time * 1000)

        def setTime(self, millis):
            """Sets this Date object to represent a point in time that is time milliseconds after January 1, 1970, 00:00:00 GMT."""
            self._time = millis / 1000.0

        def after(self, when):
            return self.getTime() > when.getTime()

        def before(self, when):
            return self.getTime() < when.getTime()

        def toString(self):
            """Returns a string representation of this date."""
            return time.strftime("%a %b %d %H:%M:%S %Z %Y", time.localtime(self._time))

        def __str__(self):
            return self.toString()
    class SimpleDateFormat:
        """Emulates the Java SimpleDateFormat class for formatting and parsing dates."""
        def __init__(self, pattern):
            self._pattern = pattern
            self._py_pattern = self._to_python_format(pattern)

        def _to_python_format(self, pattern):
            # A simple translation from Java's format to Python's strftime format
            replacements = {
                "yyyy": "%Y", "yy": "%y", "MM": "%m", "dd": "%d",
                "HH": "%H", "mm": "%M", "ss": "%S", "E": "%a", "a": "%p"
            }
            for j, p in replacements.items():
                pattern = pattern.replace(j, p)
            return pattern

        def format(self, date_obj):
            """Formats a Date object into a date/time string."""
            return time.strftime(self._py_pattern, time.localtime(date_obj._time))

        def parse(self, source):
            """Parses text from a string to produce a Date."""
            try:
                dt = datetime.datetime.strptime(source, self._py_pattern)
                return java.Date(dt.timestamp() * 1000)
            except ValueError as e:
                raise java.ParseException(f"Unparseable date: \"{source}\"") from e

        def toPattern(self):
            return self._pattern

    # --- Emulated java.lang.String (as a wrapper) ---
    class String:
        """A wrapper class to emulate Java's String methods."""
        def __init__(self, value=""):
            self._value = str(value)
        def length(self): return len(self._value)
        def charAt(self, index):
            if 0 <= index < len(self._value): return self._value[index]
            raise java.IndexOutOfBoundsException()
        def substring(self, beginIndex, endIndex=None):
            if endIndex is None: return self._value[beginIndex:]
            return self._value[beginIndex:endIndex]
        def toUpperCase(self): return self._value.upper()
        def toLowerCase(self): return self._value.lower()
        def startsWith(self, prefix): return self._value.startswith(prefix)
        def endsWith(self, suffix): return self._value.endswith(suffix)
        def indexOf(self, s): return self._value.find(s)
        def lastIndexOf(self, s): return self._value.rfind(s)
        def equals(self, other): return self._value == str(other)
        def equalsIgnoreCase(self, other): return self._value.lower() == str(other).lower()
        def trim(self): return self._value.strip()
        def split(self, regex): return self._value.split(regex)
        def isEmpty(self): return len(self._value) == 0
        def __str__(self): return self._value
        def __repr__(self): return f'java.String("{self._value}")'

    # --- Emulated java.lang.StringBuilder ---
    class StringBuilder:
        """Emulates Java's StringBuilder for mutable strings."""
        def __init__(self, initial_str=""):
            self._list = list(str(initial_str))
        def append(self, s):
            self._list.extend(list(str(s)))
            return self
        def insert(self, offset, s):
            self._list[offset:offset] = list(str(s))
            return self
        def delete(self, start, end):
            del self._list[start:end]
            return self
        def reverse(self):
            self._list.reverse()
            return self
        def toString(self): return "".join(self._list)
        def __str__(self): return self.toString()

    # --- Emulated java.util.UUID ---
    class UUID:
        """Emulates Java's UUID class."""
        @staticmethod
        def randomUUID(): return str(random.uuid4())
        @staticmethod
        def fromString(name): return str(random.UUID(name))
        @staticmethod
        def nameUUIDFromBytes(name_bytes): return str(random.uuid3(random.NAMESPACE_DNS, name_bytes))

    # --- Emulated java.io.File ---
    class File:
        """Emulates Java's File class for path manipulation."""
        def __init__(self, pathname):
            self.path = str(pathname)
        def exists(self): return os.path.exists(self.path)
        def isFile(self): return os.path.isfile(self.path)
        def isDirectory(self): return os.path.isdir(self.path)
        def getName(self): return os.path.basename(self.path)
        def getParent(self): return os.path.dirname(self.path)
        def getPath(self): return self.path
        def length(self): return os.path.getsize(self.path) if self.exists() else 0
        def delete(self):
            if self.isFile(): os.remove(self.path)
            elif self.isDirectory(): os.rmdir(self.path) # Only removes empty dirs
            return not self.exists()
        def mkdir(self): return os.mkdir(self.path)
        def mkdirs(self): return os.makedirs(self.path, exist_ok=True)
        def list(self): return os.listdir(self.path) if self.isDirectory() else None
        def __str__(self): return self.path

    # --- Emulated java.util.Arrays ---
    class Arrays:
        """A utility class for operating on arrays (Python lists)."""
        @staticmethod
        def sort(a): a.sort()
        @staticmethod
        def toString(a): return str(a)
        @staticmethod
        def equals(a, b): return a == b
        @staticmethod
        def binarySearch(a, key):
            # Assumes 'a' is sorted
            try: return a.index(key)
            except ValueError: return -1

    # --- Emulated java.lang.Math ---
    class Math:
        """Emulates the Java Math class with static methods."""
        PI = math.pi
        E = math.e

        @staticmethod
        def abs(a): return abs(a)
        @staticmethod
        def sqrt(a): return math.sqrt(a)
        @staticmethod
        def pow(base, exp): return math.pow(base, exp)
        @staticmethod
        def max(a, b): return max(a, b)
        @staticmethod
        def min(a, b): return min(a, b)
        @staticmethod
        def random(): return random.random() # Returns a double between 0.0 and 1.0
        @staticmethod
        def round(a): return round(a)
        @staticmethod
        def ceil(a): return math.ceil(a)
        @staticmethod
        def floor(a): return math.floor(a)

    # --- Emulated java.util.Random ---
    class Random:
        """Emulates the Java Random class."""
        def __init__(self, seed=None):
            if seed is not None:
                random.seed(seed)

        def nextInt(self, bound=None):
            """Returns a random int. If bound is provided, returns 0 to bound-1."""
            if bound is None:
                return random.randint(-2**31, 2**31 - 1)
            if bound <= 0:
                raise java.IllegalArgumentException("bound must be positive")
            return random.randint(0, bound - 1)

        def nextDouble(self):
            """Returns a random float (double) between 0.0 and 1.0."""
            return random.random()

        def nextBoolean(self):
            """Returns a random boolean."""
            return random.choice([True, False])

    # --- Emulated java.util.ArrayList ---
    class ArrayList:
        """Emulates the Java ArrayList."""
        def __init__(self):
            self._list = []

        def add(self, *args):
            if len(args) == 1:
                self._list.append(args[0])
            elif len(args) == 2:
                self._list.insert(args[0], args[1])
            else:
                raise java.IllegalArgumentException("add method takes 1 or 2 arguments")

        def get(self, index):
            if 0 <= index < len(self._list):
                return self._list[index]
            raise java.IndexOutOfBoundsException(f"Index: {index}, Size: {self.size()}")

        def size(self):
            return len(self._list)

        def isEmpty(self):
            return self.size() == 0

        def clear(self):
            self._list.clear()

        def remove(self, index):
            if 0 <= index < len(self._list):
                return self._list.pop(index)
            raise java.IndexOutOfBoundsException(f"Index: {index}, Size: {self.size()}")

        def __str__(self):
            return str(self._list)

    # --- Emulated java.util.HashMap ---
    class HashMap:
        """Emulates the Java HashMap."""
        def __init__(self):
            self._dict = {}
        def put(self, key, value): self._dict[key] = value
        def get(self, key): return self._dict.get(key)
        def containsKey(self, key): return key in self._dict
        def remove(self, key): return self._dict.pop(key, None)
        def size(self): return len(self._dict)
        def isEmpty(self): return self.size() == 0
        def clear(self): self._dict.clear()
        def keySet(self): return set(self._dict.keys())
        def __str__(self):
            return "{" + ", ".join([f"{k}={v}" for k, v in self._dict.items()]) + "}"

    # --- More Emulated java.util Collections ---
    class LinkedList(ArrayList): # Inherits from ArrayList for simplicity
        """Emulates Java's LinkedList, inheriting from our ArrayList."""
        def addFirst(self, e): self.add(0, e)
        def addLast(self, e): self.add(e)
        def getFirst(self): return self.get(0)
        def getLast(self): return self.get(self.size() - 1)
        def removeFirst(self): return self.remove(0)
        def removeLast(self): return self.remove(self.size() - 1)
        def peek(self): return self.get(0) if not self.isEmpty() else None
        def poll(self): return self.remove(0) if not self.isEmpty() else None
        def push(self, e): self.addFirst(e)
        def pop(self): return self.removeFirst()

    class HashSet:
        """Emulates Java's HashSet."""
        def __init__(self): self._set = set()
        def add(self, e): return self._set.add(e)
        def contains(self, o): return o in self._set
        def isEmpty(self): return len(self._set) == 0
        def remove(self, o):
            try:
                self._set.remove(o)
                return True
            except KeyError:
                return False
        def size(self): return len(self._set)
        def clear(self): self._set.clear()
        def __str__(self): return str(self._set)

    class Stack:
        """Emulates Java's Stack."""
        def __init__(self): self._list = []
        def push(self, item): self._list.append(item)
        def pop(self):
            if self.empty(): raise java.NoSuchElementException("Stack is empty")
            return self._list.pop()
        def peek(self):
            if self.empty(): raise java.NoSuchElementException("Stack is empty")
            return self._list[-1]
        def empty(self): return len(self._list) == 0
        def search(self, o):
            try:
                # Java's search is 1-based from the top of the stack
                return len(self._list) - self._list.index(o)
            except ValueError:
                return -1

    class Queue(LinkedList):
        """Emulates a Queue interface using LinkedList."""
        def offer(self, e):
            self.addLast(e)
            return True
        # peek() and poll() are already in LinkedList

    # --- Emulated java.util.Collections utility class ---
    class Collections:
        """A utility class for operating on collections."""
        @staticmethod
        def sort(list_obj): list_obj._list.sort()
        @staticmethod
        def reverse(list_obj): list_obj._list.reverse()
        @staticmethod
        def shuffle(list_obj): random.shuffle(list_obj._list)
        @staticmethod
        def max(coll): return max(coll._list)
        @staticmethod
        def min(coll): return min(coll._list)
        @staticmethod
        def frequency(coll, o): return coll._list.count(o)
        @staticmethod
        def disjoint(c1, c2):
            return set(c1._list).isdisjoint(set(c2._list))
        @staticmethod
        def emptyList(): return java.ArrayList()
        @staticmethod
        def emptySet(): return java.HashSet()

    class Scanner:
        """
        Emulates the Java Scanner class for reading user input.
        To use, create an instance like: `scanner = java.Scanner(java.System.in)`
        """
        def __init__(self, input_stream):
            # The input_stream is for mimicry of 'System.in', but we just use Python's input().
            self._buffer = []

        def _get_token(self):
            """Internal helper to get the next word (token) from the console."""
            while not self._buffer:
                line = input()
                self._buffer = line.split()
            return self._buffer.pop(0)

        def nextLine(self):
            """Reads the entire next line of input."""
            self._buffer = [] # A new line read invalidates the old buffer
            return input()

        def next(self):
            """Reads the next word (token) from the input."""
            return self._get_token()

        def nextInt(self):
            """Reads the next word and converts it to an integer."""
            token = self._get_token()
            try:
                return int(token)
            except ValueError:
                raise ValueError(f"InputMismatchException: '{token}' is not an integer.")

        def nextDouble(self):
            """Reads the next word and converts it to a float (double)."""
            token = self._get_token()
            try:
                return float(token)
            except ValueError:
                raise ValueError(f"InputMismatchException: '{token}' is not a double.")

        def close(self):
            """In Java, this closes the stream. Here, it's a no-op but good for mimicry."""
            pass
class __version__:
    def version():
        rp(f"stamp {STAMP_VERSION_STRING}")
class exit:
    def cexit(code=0):
        sys.exit(code)
    def exit():
        sys.exit()
class mfc:
    """
    Math alternative functions for:
    +-*/^==!=

    Also includes negative function for those:
    -+---*-/-^-==-!=
    """
    def add(a=1,b=1): return a+b
    def sbt(c=1,d=1): return c-d
    def tms(e=1,f=1): return e*f
    def div(g=1,h=1): return g/h
    def exp(i=1,j=1): return i**j
    def eql(k=1,l=1): return k==l
    def nql(m=1,n=1): return m!=n
    def ndd(o=1,p=1): return -o+-p
    def nsb(q=1,r=1): return -q - -r
    def nms(s=1,t=1): return -s*-t
    def ndv(u=1,v=1): return -u/-v
    def nxp(w=1,x=1): return -w**-x
    def nql(y=1,z=1): return -y==-z
    def nnl(a1=1,b1=1): return -a1!=-b1
class Color:
    def colors():
        _COLORS = {
            "red":       "\033[38;2;209;105;105m",
            "orange":    "\033[38;2;206;145;120m",
            "yellow":    "\033[38;2;220;220;170m",
            "green":     "\033[38;2;106;153;85m",
            "teal":      "\033[38;2;78;201;176m",
            "cyan":      "\033[38;2;79;193;255m",
            "blue":      "\033[38;2;86;156;214m",
            "purple":    "\033[38;2;197;134;192m",
            "white":     "\033[38;2;212;212;212m",
            "bold":      "\033[1m",
            "italic":    "\033[3m",
            "underline": "\033[4m",
            "strike":    "\033[9m",
            "reset":     "\033[0m"
        }
    def colornos():
        _COLOR_NOS = {
            "1":   "\033[38;2;209;105;105m",
            "2":   "\033[38;2;206;145;120m",
            "3":   "\033[38;2;220;220;170m",
            "4":   "\033[38;2;106;153;85m",
            "5":   "\033[38;2;78;201;176m",
            "6":   "\033[38;2;79;193;255m",
            "7":   "\033[38;2;86;156;214m",
            "8":   "\033[38;2;197;134;192m",
            "9":   "\033[38;2;212;212;212m",
            "10":  "\033[1m",
            "11":  "\033[3m",
            "12":  "\033[4m",
            "13":  "\033[9m",
            "14":  "\033[0m"
        }
    def colorwnos():
        _COLOR_W_NOS = {
            "one":         "\033[38;2;209;105;105m",
            "two":         "\033[38;2;206;145;120m",
            "three":       "\033[38;2;220;220;170m",
            "four":        "\033[38;2;106;153;85m",
            "five":        "\033[38;2;78;201;176m",
            "six":         "\033[38;2;79;193;255m",
            "seven":       "\033[38;2;86;156;214m",
            "eight":       "\033[38;2;197;134;192m",
            "nine":        "\033[38;2;212;212;212m",
            "ten":         "\033[1m",
            "eleven":      "\033[3m",
            "twelve":      "\033[4m",
            "thirteen":    "\033[9m",
            "fourteen":    "\033[0m"
        }
class Calculator:
    def pcalculate(a,b):
        if not int(a) == a:
            raise TypeError("a and b must be int")
        elif not int(b) == b:
            raise TypeError("a and b must be int")
        return a+b
    def mcalculate(a,b):
        if not int(a) == a:
            raise TypeError("a and b must be int")
        elif not int(b) == b:
            raise TypeError("a and b must be int")
        return a*b
    def dcalculate(a,b):
        if not int(a) == a:
            raise TypeError("a and b must be int")
        elif not int(b) == b:
            raise TypeError("a and b must be int")
        return a/b
    def ecalculate(a,b):
        if not int(a) == a:
            raise TypeError("a and b must be int")
        elif not int(b) == b:
            raise TypeError("a and b must be int")
        return a**b
    def scalculate(a,b):
        if not int(a) == a:
            raise TypeError("a and b must be int")
        elif not int(b) == b:
            raise TypeError("a and b must be int")
        return a-b
    def ucalculate(a,b):
        if not int(a) == a:
            raise TypeError("a and b must be int")
        elif not int(b) == b:
            raise TypeError("a and b must be int")
        return a%b
class AddImportantError(Exception):
    pass
class __store__:
    def __storeinit__():
        global STORE
        STORE = []
    __storeinit__()
    def __store__(): return STORE
    def __add__(var): STORE += var
    def __del__(var): STORE -= var
class store:
    def __add__(var): __store__.__add__(var) 
    def __del__(var): __store__.__del__(var)
    def __viewstore__(): __store__.__store__()
class Methods:
    def __storeadd__(var): store.__add__(var)
    def __storedel__(var): store.__del__(var)
    def __storeview__(): store.__viewstore__()
    def __listadd__(thing): 
        if callable(list(thing)): thing.append(thing)
    def __listcls__(thing): 
        if callable(list(thing)): thing.clear()
    def __listshw__(thing):
        if callable(list(thing)): return list(thing)
    def __listcot__(thing):
        if callable(list(thing)): return thing.count()
    def __listext__(origin, extender):
        if callable(list(origin)): ORG_IS_LIST = True; 
        else: ORG_IS_LIST = False
        if ORG_IS_LIST == False: sys.exit()
        else: 
            if callable(list(extender)): EXT_IS_LIST = True
            else: EXT_IS_LIST = False
            if EXT_IS_LIST == False: sys.exit()
            else:
                origin.extend(extender)
    def __listbxt__(origin, extender):
        if callable(list(origin)): ORG_IS_LIST = True; 
        else: ORG_IS_LIST = False
        if ORG_IS_LIST == False: sys.exit()
        else: 
            if callable(list(extender)): EXT_IS_LIST = True
            else: EXT_IS_LIST = False
            if EXT_IS_LIST == False: sys.exit()
            else:
                extender.extend(origin)
class istrue:
    def istrue(val):
        if val == True:
            return True
        if val == False:
            return False
        return False
class isfalse:
    def isfalse(val):
        if val == True:
            return False
        if val == False:
            return True
        return False
class License(): #INTENDED to be HERE and existing
    @staticmethod
    def show():
        rp(f"licenses:\napache\n\t2.0\nBSD 3-Clause\nMIT\nPSF\ntype: tree\npython: {platform.python_version()}")
if __name__ == "__main__": 
	_rsfd.main()

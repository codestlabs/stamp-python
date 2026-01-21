#rulefollow: sdd8
#main module imports
class DeprectatedError(Exception):pass
class _rsfd: main=lambda f:(__import__("inspect"),__import__("os")) and [(_ for _ in ()).throw(DeprectatedError("Direct 'import stamp' is forbidden. Use submodules.")) for _f in __import__("inspect").stack()[1:] if _f.filename and not __import__("os").path.abspath(_f.filename).startswith(__import__("os").path.dirname(__import__("os").path.abspath(f)))] and None
RSFDFILE = __file__
_rsfd.main(RSFDFILE)
from .main import (
    ErrorSystem,
    __initexec__,
    globalsys,
    Stamp,
    PCStamp,
    ListDirectory,
    CallError,
    call,
    __cstring__,
    __cmd__,
    _py_classlvl_consts,
    superobj,
    __jsonconf__,
    __calc_hcl__,
    adverr,
    advout,
    advin,
    __cmp__,
    __helpcmd__,
    pdec,
    __exf__,
    __cd__,
    tconstant,
    tlist,
    Type,
    UnknownAdverrIntError,
    Control,
    Debug,
    DirectoryExistsError,
    ArgumentError,
    _export,
    _import,
    _mkdir,
    _mkfile,
    _note,
    _notes,
    _cl,
    _lock,
    _ConfigValue,
    S1,
    S2,
    C1,
    C2,
    K1,
    K2,
    T1,
    T2,
    L1,
    L2,
    R1,
    R2,
    temp,
    taskmgr,
    edit,
    Unite,
    Kit,
    Abombination,
    Angle,
    Alias,
    __isin__,
    __log__,
    Frozen,
    _seed,
    _dynvar,
    _link,
    _uname,
    __version__,
    exit,
    License,
    Error501,
    Error502,
    Error503,
    Error504,
    Error505,
    Error506,
    Error507,
    Error508,
    UseDifferentClassError,
    Server,
    textprocesser,
    Tara,
    RTara,
    _history,
    _kvstore,
    _transfer,
    _ttransfer,
    _chunk,
    Astray,
    Calculator,
    DeprectatedError,
    _rsfd,
    lstamp,
    specmtdta,
    tools,
    repeat,
    java,
    Color,
    istrue,
    isfalse,
    AddImportantError,
    __store__,
    store,
    Methods,
    mfc,
)
#fetch module imports
from .__fetch__ import Fetch  
#doc module imports
from .__doc__ import (
    __crt_doc__,
    __add_todoc__,
    __del_fromdoc__,
    __del_doc__,
    __doc_links__,
)
#rxyz module imports
from ._rxyz import (
    _rxyz,
)
#spare init code
from ._ import *
#regex utils
from ._regex import (
    rgx,
)
#event log util
from ._evlog import (
    uevlog,
)
#shortcut util 
from ._shcut import (
    ushcut,
)

#ai module imports
from .llm import (
    OllamaConfig,
    OllamaCheck,
    GPT2Generator,
    Ollama,
    LLMBatchGenerator,
    LLMEmbeddings,
    LLMModelComparer,
    LLMTokenizer,
    PromptTemplate,
    ResponseFilter,
    FileProcessor,
    WebScraper,
    LLMAPIServer,
    LLMMemory,
    ToolCaller,
    ConversationManager,
    PromptAssistant,
    ModelBenchmarker,
    ResponseAnalyzer,
    EventStreamer,
    PromptChainer,
    ConcurrentGenerator,
    ResponseFormatter,
    ToolSelector,
)

#ai features module imports
from .lib.ai.oaiftrs.ptr.ptai import PatternAI
from .lib.ai.oaiftrs.cdi.coai import CodeAI
from .lib.ai.oaiftrs.daz.daai import DataAnalyzer
from .lib.ai.oaiftrs.prd.prai import PredictSystem
from .lib.ai.oaiftrs.sec.scai import SecurityAI
from .lib.ai.oaiftrs.img.imai import ImageAI
from .lib.ai.oaiftrs.aud.adai import AudioAI
from .lib.ai.oaiftrs.dpl.dlai import DeepLearningAI
from .lib.ai.oaiftrs.fct.fcai import ForecastAI
from .lib.ai.oaiftrs.kga.kgai import KnowledgeGraphAI
from .lib.ai.oaiftrs.rec.rcai import RecommendationAI
from .lib.ai.oaiftrs.vis.viai import VisionAI
from .lib.ai.oaiftrs.qzr.quzr import QuantizerAI
from .lib.ai.oaiftrs.oaiftrs import NLPText,SmartSearch,OptimizationAI
from .api import AI
from .validation import ValidationError,Validator,Require,TypeCheck,NonEmpty,InRange
class __getversion__:
    def get():
        main.__version__.version()
class __lib__:
    def __getlib__():
        import subprocess
        subprocess.run("")
class __uninstall__:
    def __uninstall__():
        import subprocess
        import sys
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "stamp"])
class __upgrade__:
    def __upgrade__():
        import subprocess
        import sys
        subprocess.run([sys.executable, "-m", "pip", "install", "stamp", "--upgrade"])
import platform
import socket
import psutil
import uuid
import sys
import os
import re
#init constants
STPVER = main.__version__.version()
SYSTEM = platform.uname()
OSNAME = os.name
FIRMWR = SYSTEM
FIRMVR = SYSTEM.version
FIRMRL = SYSTEM.release
FIRMSY = SYSTEM.system
FIRMPR = SYSTEM.processor
FIRMND = SYSTEM.node
FIRMPC = SYSTEM.machine
FIRMRM = str(round(psutil.virtual_memory().total/(1024.0**3)))+" GB"
FIRMRN = str(round(psutil.virtual_memory().total/(1024.0**3)))+"GB"
FIRMMA = ':'.join(re.findall('..','%012x'%uuid.getnode()))
FIRMIP = socket.gethostbyname(socket.gethostname())
FIRMHN = socket.gethostname()
FIRMPT = os.environ["PATH"]
FIRMAL = f"{FIRMWR}:{FIRMVR}:{FIRMRL}:{FIRMSY}:{FIRMPR}:{FIRMND}:{FIRMPC}:{FIRMRM}:{FIRMRN}:{FIRMMA}:{FIRMIP}:{FIRMHN}:{FIRMPT}"
FIRMAB = f"{FIRMHN}:{FIRMIP}:{FIRMMA}:{FIRMND}:{FIRMPC}:{FIRMPR}:{FIRMPT}:{FIRMRL}:{FIRMRM}:{FIRMRN}:{FIRMSY}:{FIRMVR}:{FIRMWR}"
FIRMAR = f"{FIRMWR}:{FIRMVR}:{FIRMSY}:{FIRMRN}:{FIRMRM}:{FIRMRL}:{FIRMPT}:{FIRMPR}:{FIRMPC}:{FIRMND}:{FIRMMA}:{FIRMIP}:{FIRMHN}"
FIRMLT = {
    "stamp.version": STPVER,
    "system.hostname":FIRMHN,
    "system.ipaddress":FIRMIP,
    "system.macaddress":FIRMMA,
    "system.node":FIRMND,
    "system.machine":FIRMPC,
    "system.cpu":FIRMPR,
    "system.path":FIRMPT,
    "system.release":FIRMRL,
    "system.ram":FIRMRM,
    "system.ram":FIRMRN,
    "system.system":FIRMSY,
    "system.version":FIRMVR,
    "system.uname":FIRMWR
}
FIRMST = {
    "stpver":STPVER,
    "syshsn":FIRMHN,
    "sysipa":FIRMIP,
    "sysmca":FIRMMA,
    "sysnde":FIRMND,
    "systpc":FIRMPC,
    "syscpu":FIRMPR,
    "syspth":FIRMPT,
    "sysrls":FIRMRL,
    "sysram":FIRMRM,
    "sysram":FIRMRN,
    "system":FIRMSY,
    "sysver":FIRMVR,
    "sysunm":FIRMWR
}
FIRMTT = {
    "stv":STPVER,
    "hsn":FIRMHN,
    "ipa":FIRMIP,
    "mca":FIRMMA,
    "nde":FIRMND,
    "spc":FIRMPC,
    "cpu":FIRMPR,
    "pth":FIRMPT,
    "rls":FIRMRL,
    "ram":FIRMRM,
    "ram":FIRMRN,
    "sys":FIRMSY,
    "svr":FIRMVR,
    "unm":FIRMWR
}
class getinfo:
    def get():
        for item in list(os.environ):
            print(item + f" : {os.environ[item]}")        
        print(FIRMAL)
    def get_a1(): return FIRMLT
    def get_a2(): return FIRMST
    def get_a3(): return FIRMTT
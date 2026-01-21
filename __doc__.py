from rich import print
from rich.text import Text
import datetime
import sys
import os
__all__ = ["__crt_doc__", "__add_todoc__", "__del_fromdoc__", "__del_doc__", "__doc_links__"]
class __del_fromdoc__:
    def del_fromdoc(oldText=str, deleteFromOldDocText=str, transferFromDefualtVarToNewVarVarName=str, saveNewTextToFile=None, saveNewTextToFilePath=str):
        deleteFromOldDocText = ""
        deleteFromOldDocText = deleteFromOldDocText
        deleteFromOldDocText = Text(f"{__del_fromdoc__.deleteFromDocText}")
        deleteFromOldDocText.replace(f"{deleteFromOldDocText}", "")
        if saveNewTextToFile == True:
            try:
                with open(f"{saveNewTextToFilePath}", "w") as f:
                    f.write(f"{deleteFromOldDocText}")
                print("withopen: writing success")
            except Exception as e:
                pass
        elif saveNewTextToFile == False or None:
            print(f"{__del_fromdoc__.deleteFromOldDocText}")
            sys.exit()
        print(f"{__del_fromdoc__.deleteFromOldDocText}")
class __del_doc__:
    def del_doc(docPath=str):
        if os.path.exists(__del_doc__.docPath):
            os.remove(__del_doc__.docPath)
        else:
            pass
class __add_todoc__:
    def add_todoc(oldText=str, addToOldDocText=str, addFromStart=None, addFromEnd=None, saveNewTextToFile=None, saveNewTextToFilePath=str):
        oldText = oldText
        addToOldDocText = addToOldDocText
        addFromStart = addFromStart
        addFromEnd = addFromEnd
        saveNewTextToFile = saveNewTextToFile
        saveNewTextToFilePath = saveNewTextToFilePath
        if addFromStart == True and addFromEnd == False: addToOldDocText = addToOldDocText + oldText
        elif addFromStart == False and addFromEnd == True: addToOldDocText = oldText + addToOldDocText
        else: pass
        if saveNewTextToFile == True:
            try:
                with open(f"{saveNewTextToFilePath}", "w") as f:
                    f.write(f"{addToOldDocText}")
                print("withopen: writing success")
            except Exception as e:
                pass
        elif saveNewTextToFile == False or None:
            print(f"{__add_todoc__.addToOldDocText}")
            sys.exit()
        print(f"{__add_todoc__.addToOldDocText}")
class __crt_doc__:
    def crt_doc(docPath=str, docContents=str, docName=str, includeDocNameAtStart=None, includeDateAtStart=None, docFileType=str):
        docPath = docPath
        docContents = docContents
        includeDocNameAtStart = includeDocNameAtStart
        includeDateAtStart = includeDateAtStart
        docFileType = docFileType
        if os.path.exists(__crt_doc__.docPath):
            os.remove(__crt_doc__.docPath)
        if includeDocNameAtStart == True and includeDateAtStart == True:
            docContents = f"{__crt_doc__.docName} at {datetime.datetime.now()}\n" + f"{__crt_doc__.docContents}"
        elif includeDocNameAtStart == True and includeDateAtStart == False:
            docContents = f"{__crt_doc__.docName}\n" + f"{__crt_doc__.docContents}"
        elif includeDocNameAtStart == False and includeDateAtStart == True:
            docContents = f"{datetime.datetime.now()}\n{__crt_doc__.docContents}"
        elif includeDocNameAtStart == False and includeDateAtStart == False:
            docContents = f"{__crt_doc__.docContents}"
        else:
            pass
        try:
            with open(f"{__crt_doc__.docPath}", "x") as f:
                f.write(f"{docContents}")
                print("withopen: writing success")
                sys.exit()
        except Exception as e:
            pass
class __doc_links__:#INTENDED to be HERE and existing
    f"""
    __crt_doc__
    __add_todoc__
    __del_fromdoc__
    __del_doc__
    """
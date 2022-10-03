from win32.lib.pywintypes import error as error

def ChangeClipboardChain(hWndRemove: int, hWndNewNext: int): ...
def CloseClipboard(): ...
def CountClipboardFormats(): ...
def EmptyClipboard(): ...
def EnumClipboardFormats(_format: int = ...): ...
def GetClipboardData(_format) -> str: ...
def GetClipboardDataHandle(_format): ...
def GetClipboardFormatName(_format) -> str: ...
def GetClipboardOwner(): ...
def GetClipboardSequenceNumber(): ...
def GetClipboardViewer(): ...
def GetGlobalMemory(hglobal: int) -> str: ...
def GetOpenClipboardWindow(): ...
def GetPriorityClipboardFormat(formats): ...
def IsClipboardFormatAvailable(_format) -> bool: ...
def OpenClipboard(hWnd: int | None = ...): ...
def RegisterClipboardFormat(name: str): ...
def SetClipboardData(_format, hMem): ...
def SetClipboardText(text, _format): ...
def SetClipboardViewer(hWndNewViewer: int) -> int: ...

CF_BITMAP: int
CF_DIB: int
CF_DIBV5: int
CF_DIF: int
CF_DSPBITMAP: int
CF_DSPENHMETAFILE: int
CF_DSPMETAFILEPICT: int
CF_DSPTEXT: int
CF_ENHMETAFILE: int
CF_HDROP: int
CF_LOCALE: int
CF_MAX: int
CF_METAFILEPICT: int
CF_OEMTEXT: int
CF_OWNERDISPLAY: int
CF_PALETTE: int
CF_PENDATA: int
CF_RIFF: int
CF_SYLK: int
CF_TEXT: int
CF_TIFF: int
CF_UNICODETEXT: int
CF_WAVE: int
UNICODE: bool

from _winreg import *

def korzinka_users(sid):
    try:
        kalit = OpenKey(HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"+'\\'+sid)
        (value,type) = QueryValueEx(kalit,'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid
korzinka_users("you can put here arg")

# git commands -->gcls

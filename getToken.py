import win32cred
creds = win32cred.CredEnumerate(None, 0)
for cred in creds:
    target = cred['TargetName']

import win32cred
creds = win32cred.CredEnumerate(None, 0)
for cred in creds:
    target = cred['TargetName']

    if 'github' in target.lower() or 'git:' in target.lower():
        print("=" * 50)
        print("Target:", target)

        blob = cred.get('CredentialBlob')

        if blob:
            try:
                if isinstance(blob, bytes):
                    print("Secret:", blob.decode('utf-16'))
                else:
                    print("Secret:", blob)
            except:
                print("Raw:", blob)

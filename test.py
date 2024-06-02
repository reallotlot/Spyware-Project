from Spyware_Manager import Manager


analyze = Manager.Analysis(r'malware')
for i in range(3):
    result = analyze.run_analysis()
    print(result)
analyze.load_data()

########################ENCRYPT API KEYS##########################
#key = os.getenv('API_ENCRYPTION_KEY')
#if key is None:
#    raise ValueError("No API_ENCRYPTION_KEY found in environment variables")
#
#encrypt = fernet.Fernet(key)
#
#vt = b''
#hybrid = b''
#
#evt = encrypt.encrypt(vt)
#ehybrid = encrypt.encrypt(hybrid)
#
#with open(r'Spyware_Manager\api_keys.txt', 'wb') as file:
#    file.write(evt + b'\n' + ehybrid)
########################ENCRYPT API KEYS##########################

#        _sopen = cdll.msvcrt._sopen
#        _close = cdll.msvcrt._close
#        _SH_DENYRW = 0x10
#
#        if not os.access(self.quarantine_file, os.F_OK):
#            return None # file doesn't exist
#        h = _sopen(self.quarantine_file, 0, _SH_DENYRW, 0)
#        if h == 3:
#            _close(h)
#            return False # file is not opened by anyone else
#        _close(h)
#        return True # file is already open
        
        
        
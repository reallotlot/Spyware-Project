from Spyware_Manager import manager


analyze = manager.Analysis()

for i in range(1):
    result = analyze.run_analysis(r'C:\Users\lotan\project\Spyware-Project\malware\update.exe')
    print(result)
    
#print(analyze.load_data())

#try:
#    print(analyze.__load_key())
#except Exception as e:
#    print(e)

        
        
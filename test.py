from Spyware_Manager import Manager


analyze = Manager.Analysis(r'malware')
#for i in range(1):
#    result = analyze.run_analysis()
#    print(result)
print(analyze.load_data())


        
        
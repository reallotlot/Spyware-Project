import re

text =  'The quick brown fox jumps over 13 lazy dogs! Did it? #Yes, @5:00PM, $20.99 for 2 (two) "cups" of coffee, & 1/2 a donut; was it worth it? :) <html> <body> </body> </html> [Use this text, extract: dates, times, prices, words, etc.]'
abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

extracted = re.findall('[!-3]{6,}', abc)
print(extracted)



#from Spyware_Manager import manager
#
#
#analyze = manager.Analysis()
#
#for i in range(1):
#    result = analyze.run_analysis(r'C:\Users\lotan\project\Spyware-Project\malware\update.exe')
#    print(result)
    
#print(analyze.load_data())

#try:
#    print(analyze.__load_key())
#except Exception as e:
#    print(e)

        
        
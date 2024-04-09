text = list(open("Spyware_Manager\hashfiles\sha256.txt", 'r').read().split('\n'))
hashes = open('Spyware_Manager\hashfiles\sha256hashes.txt','w')
info = open('Spyware_Manager\hashfiles\sha256info.txt','w')
count = 0
for i in text:
    count += 1
    hashes.write(i[:64] + "\n")
    info.write(i[65:] + "\n")
    print(f"{int(count/len(text)*100)}")
    

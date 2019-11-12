# def segitigakata(kata):
kalimat = ("Purwadhika Startup and Coding School @BSD").replace (' ', '')
kalList = list(kalimat)

aturan = []
for a in range(len(kalList)):
    X = int((a*(a+1))/2)
    aturan.append (X)

n=0
if len(kalList) not in aturan:
    print ('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
else:
    n= aturan.index(len(kalList))
def maju(n):   
    num = 0
    for i in range(0, n): 
        for j in range(0, i+1): 
            print(kalList[num], end=" ")  
            num = num + 1
        print("\r") 
def mundur(n):   
    num = 0
    for i in range(n, 0, -1): 
        for j in range(1, i+1): 
            print(kalList[num], end=" ")  
            num = num + 1
        print("\r") 
       
maju(n)
mundur(n)

def checkPrime(x):
    if (x >99 and x<1000):
        for i in range (2,x):
            if (x%i)==0:
                return False
            else:
                return True
    else:
        return False

def Modulus(p,q):
    return p*q

def ET(p,q):
    return (p-1)*(q-1)

def factors(x,list):
    for i in range (1,x+1):
        if x%i == 0:
            list.append(i)

def checkpublicKey(e,N,ET):
    Liste = []
    ListN = []
    ListET = []
    List1 = []
    factors(e,Liste)
    factors(N,ListN)
    factors(ET,ListET)

    for x in Liste:
        if x in ListN or x in ListET:
            List1.append(x)

    if len(List1)==1 and List1[0]==1 and e > 1 and e<ET:
        return True

#Extended Euclidean Algorithm

def EED(x,y):
    if (y>x):
        temp = x
        x=y
        y=temp

    listQ=  []
    listA = []
    listB = []
    listR = []
    listT1 = []
    listT2 = []
    listT = []

    listA.append(x)
    listB.append(y)
    listT1.append(0)
    listT2.append(1)

    while (listB[-1] != 0):
        listQ.append(int(listA[-1]/listB[-1]))
        listR.append(listA[-1]%listB[-1])
        listT.append(listT1[-1]-listT2[-1]*listQ[-1])
        listA.append(listB[-1])
        listB.append(listR[-1])
        listT1.append(listT2[-1])
        listT2.append(listT[-1])
    listQ.append("-")
    listR.append("-")
    listT.append("-")
    print("\nEuclidean algorithm for Generating Private Key")
    print("Q\t\t\tA\t\t\tB\t\t\tR\t\t\t\tT1\t\t\t\tT2\t\t\t\tT")

    for i in range(0, len(listT1)):
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s"
              %(str(listQ[i]),str(listA[i]),str(listB[i]),str(listR[i]),str(listT1[i]),str(listT2[i]),str(listT[i])))

    if (listT1[-1]>0):
        return(listT1[-1])
    else:
        return(listT1[-1]+listT2[-1])

#Trigraph Processing
def TriGraph(x):
    n=3
    output = [(x[i:i + n]) for i in range(0, len(x), n)]
    return output

def splitWord(x):
    letterlist = list(x)
    return letterlist

def LetterCode(x):
    return ord(x)-65

def TrigraphCode(x):
    CodeList =[]
    letterlist= splitWord(x)
    print ("Characters", letterlist)
    for i in letterlist:
        CodeList.append(LetterCode(i))
    print("Letter Code",CodeList)
    sum =0
    CodeList.reverse()
    for i in range(0,len(letterlist)):
        sum = sum+ ((26**(i))*CodeList[i])
    print("TriGraphCode: ", sum)
    return sum

#Encryption:
def encryption(TriCode,e,n):
    return((TriCode**e)%n)

def Cyphertext(x):
    return(chr(x))

#QUADGRAPH
def QuadGraph(x):
    n=4
    output = [(x[i:i + n]) for i in range(0, len(x), n)]
    return output

#DECRYPTION
def Decryption(code,d,n):
    return(code**d)%n

# RUNNING CODE
p=0
while(checkPrime(p)!=True):
    p = int(input("Enter first 3 digit prime number: "))
    checkPrime(p)
    if checkPrime(p)==True:
        print ("OK")
    else:
        print("Try Again!")
q=0
while(checkPrime(q)!=True):
    q = int(input("Enter second 3 digit prime number: "))
    checkPrime(q)
    if checkPrime(q)==True:
        print ("OK")
    else:
        print("Try Again!")

N=Modulus(p,q)
ET=ET(p,q)

e=0
while checkpublicKey(e,N,ET) != True:
    e = int(input("Enter public key: "))
    checkpublicKey(e,N,ET)
    if checkpublicKey(e,N,ET) == True:
        print("OK")
    else:
        print("Try Again")

d = EED(e,ET)

print("First Prime number: ",p)
print("Second Prime Number: ",q)
print("Modulus",N)
print("Euler Totient", ET)
print("Public Key: (%d,%d)"%(e,N))
print("Private Key: (%d,%d)"%(d,N))

message=input("\nEnter message: ")
messagemod = len(message)%3
if(messagemod==1):
    message = message + "AA"
elif(messagemod==2):
    message = message + "A"
Req = input("Encrypt Message? Y/N: ")
if Req == "Y":
    List1=TriGraph(message)
    print("\nTrigraph:", List1)
    TriCodeList=[]
    for i in List1:
        print("\n")
        TriCodeList.append(TrigraphCode(i))
    print (TriCodeList)
    CipherNumList = []
    for i in range(0,len(TriCodeList)):
        m = TriCodeList[i]
        CipherNumList.append(encryption(m,e,N))
    print("CipherText Numbers: ", CipherNumList)
    Listx = []
    for i in CipherNumList:
        x=3
        for j in range (0,4):
            Listx.append(int((i/(26**x)%26)+65))
            x=x-1
    CiphertextList = []
    for i in Listx:
        CiphertextList.append(Cyphertext(i))
    print ("\nYOUR ENCRYPTED TEXT IS:")
    ciphertext = ''.join(CiphertextList)
    print(ciphertext)

Req2 = input("Decrypt this message? Y/N: ")
if Req2 == "Y":
    ListQuadText = QuadGraph(ciphertext)
    print("Cipher QuadTexts : ",ListQuadText)
    ListNumCode = []
    for i in ListQuadText:
        x=0
        sum = 0
        for j in range (3,-1,-1):
            sum = sum + (LetterCode(i[x])*(26**j))
            x=x+1
        ListNumCode.append(sum)
    print("Numeric Codes for Quadgraphs: ",ListNumCode)

    decryptQuad = []
    for i in ListNumCode:
        decryptQuad.append(Decryption(i,d,N))
    print("Decrypted Quad Codes", decryptQuad)

    decryptTrigraph = []
    for i in decryptQuad:
        for j in range (2,-1,-1):
            if j == 2:
                decryptTrigraph.append(chr((int(i/(26**j))+65)))
            else:
                decryptTrigraph.append(chr(int((i/(26**j)%26)+65)))

    print("\nDECRYPTED MESSAGE: ")
    decryptMessage = (''.join(decryptTrigraph))
    if (messagemod == 1):
        print(decryptMessage[:-2])
    elif (messagemod == 2):
        print(decryptMessage[:-1])
    else:
        print(decryptMessage)
















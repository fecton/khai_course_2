from random import randint

def gen(l: int) -> str:
    res = ""

    a = "qwertyuiopasdfghjklzxcvbnm"
    a += a.upper()
    word = "hello"

    for i in range(l):
        res += a[randint(0, len(a)-1)]
    
    k = randint(6, l-6)
    res = res[:k] + word + res[k+5:]

    return res
    
"""
for i in [50,100,150,200,250,300,400,500]:
    t = gen(i)
    # print(len(t))
    print(t)
"""

# print(gen(1000))

cutit = \
"AAAAVtCnDpwjuaKWdjSTSOhPHTEYoNmgwCgFotEqhRdCwpiPlDnPMPRnoqUCNJbXUCUFzUHzGIPGyphMPfBJbiiRIsvsEeaUBbDYCFZvZQPHuPvUntQzenJWvdmUsEdwjjUceiMGgHOnxnQEUgyiBjRkqWYZeJSJjBLWkTLzqDIFGKoAJTrMxFtaRmBgKttVUMqGYFELSxahppYGoSEBlnLdrHoacATAXfoneJzXHSiGzUqfodipFvLIRGhqNElhTkuPzRFSENtQVtxBhXFbgolPaFhuhENkWFAtSSIPLlJKfhDJibmsMGOUWVkARfjftqmSwSsbNkIYOijVgbjewQshqpOWyjSyoZtphelloBbtCyeSsJIuoFhpbfcMTOWzPjbYimzrZIYVYIdksFuRcAkehAzTOZLjzJekavIxrQwKrAdtkJjsOXMQienGJeXMKjCVDfNcrAUngZfMIrMzDBjTQdtbPzDTigPraWNxGAGWNLksqVRO"

print(cutit[:50])
print(cutit[:100])
print(cutit[:150])
print(cutit[:200])
print(cutit[:250])
print(cutit[:300])
print(cutit[:400])
print(cutit)


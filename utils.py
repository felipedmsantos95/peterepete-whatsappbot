from unicodedata import normalize

#Cath body and ignore graphics accents
def normalizeWords(msg):
    msg = msg.lower()
    return normalize('NFKD', msg).encode('ASCII', 'ignore').decode('ASCII')
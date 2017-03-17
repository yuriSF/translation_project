import nltk
from nltk import CFG
grammar = CFG.fromstring("""
    
    Sent -> SAdv Clause | Clause
    
    Clause -> Pred | Pred AdvP
    
    Pred -> NP V NP NP | NP V NP | NP V NP | NP V
    
    NP -> Det N | Det AP N | AP N | NP PP | N 

    PP -> P NP
    
    AP -> A AP | A
    A -> 'xoroshij' | 'interesnaja' | 'ploxaja' | 'chernyj'
    Det -> 'etot' | 'kakoj-to'
    N -> 'koshka' | 'chelovek' | 'ulitse'| 'sobaka' | 'muzhchina' | 'zhenshina' | 'kniga'
    V -> 'videt' | 'davat'| 'bezhat' | 'daet'
    P -> 'na' | 'v' | 'posle' | 's'
    AdvP -> Deg Adv | Adv
    Adv -> 'bistro' | 'izdaleka'
    SAdv -> 'k-sozhaleniju' | 'k-schastju'
    """)

sent = 'k-schastju ploxaja koshka videt xoroshij chernyj sobaka izdaleka'
#sent = 'muzhchina s sobaka daet zhenshina xoroshij interesnaja kniga bistro'


sent = sent.split()
#print grammar.start()
#print grammar.productions()
parser = nltk.ChartParser(grammar)
for tree in parser.parse(sent):
    print(tree)
    tree.draw()
    

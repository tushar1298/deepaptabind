from config import CONTACT_DISTANCE,HBOND_DISTANCE
from utils import distance

def analyze_interactions(protein_atoms,rna_atoms):

    contacts=0
    hbonds=0

    for a in protein_atoms:
        for b in rna_atoms:

            d=distance(a,b)

            if d < CONTACT_DISTANCE:
                contacts+=1

            if d < HBOND_DISTANCE:
                hbonds+=1

    stacking=int(contacts*0.08)

    electro=int(contacts*0.15)

    return {
        "contacts":contacts,
        "hbonds":hbonds,
        "stacking":stacking,
        "electrostatic":electro
    }

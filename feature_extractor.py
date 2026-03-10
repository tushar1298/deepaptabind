import numpy as np
from config import CONTACT_DISTANCE
from utils import distance

def extract_features(protein_atoms,rna_atoms):

    contacts=0
    distances=[]

    for a in protein_atoms:
        for b in rna_atoms:

            d=distance(a,b)

            if d < CONTACT_DISTANCE:

                contacts+=1
                distances.append(d)

    interface_density=len(distances)

    avg_dist=np.mean(distances) if distances else 0

    features={
        "contacts":contacts,
        "avg_distance":avg_dist,
        "interface_density":interface_density
    }

    return features

from config import RNA_RES, PROTEIN_RES

def detect_chains(structure):

    protein=set()
    rna=set()

    for model in structure:
        for chain in model:
            for res in chain:

                r=res.get_resname().strip()

                if r in RNA_RES:
                    rna.add(chain.id)

                if r in PROTEIN_RES:
                    protein.add(chain.id)

    return list(protein), list(rna)

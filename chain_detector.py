from config import RNA_RES, DNA_RES, PROTEIN_RES

def detect_chains(structure):

    protein=set()
    aptamer=set()

    for model in structure:
        for chain in model:
            for res in chain:

                name=res.get_resname().strip()

                if name in PROTEIN_RES:
                    protein.add(chain.id)

                if name in RNA_RES or name in DNA_RES:
                    aptamer.add(chain.id)

    return list(protein), list(aptamer)

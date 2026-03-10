import streamlit as st
from Bio.PDB import PDBParser

from chain_detector import detect_chains
from feature_extractor import extract_features
from interaction_analyzer import analyze_interactions
from energy_model import compute_binding_energy
from gnn_model import predict_dl
from visualizer import show_structure
from plots import interaction_barplot

st.title("DeepAptaBind")
st.subheader("Deep Learning Protein–Aptamer Binding Predictor")

uploaded=st.file_uploader("Upload PDB file",type=["pdb"])

parser=PDBParser(QUIET=True)

if uploaded:

    structure=parser.get_structure("complex",uploaded)

    protein_chains,rna_chains=detect_chains(structure)

    st.write("Detected Protein Chains:",protein_chains)
    st.write("Detected Aptamer Chains:",rna_chains)

    p_chain=st.selectbox("Select Protein Chain",protein_chains)
    r_chain=st.selectbox("Select Aptamer Chain",rna_chains)

    protein_atoms=[]
    rna_atoms=[]

    for model in structure:
        for chain in model:

            if chain.id==p_chain:

                for atom in chain.get_atoms():
                    protein_atoms.append(atom.coord)

            if chain.id==r_chain:

                for atom in chain.get_atoms():
                    rna_atoms.append(atom.coord)

    features=extract_features(protein_atoms,rna_atoms)

    interactions=analyze_interactions(protein_atoms,rna_atoms)

    energy=compute_binding_energy(features,interactions)

    dl_score=predict_dl(features)

    st.header("Binding Prediction")

    st.write("Physics based ΔG:",round(energy,2),"kcal/mol")

    st.write("Deep Learning Score:",round(dl_score,2))

    st.header("Interaction Summary")

    st.json(interactions)

    fig=interaction_barplot(interactions)

    st.pyplot(fig)

    pdb_string=uploaded.getvalue().decode()

    st.header("3D Structure")

    show_structure(pdb_string)

import streamlit as st
from Bio.PDB import PDBParser
from io import StringIO

from pdb_fetcher import fetch_pdb
from chain_detector import detect_chains
from feature_extractor import extract_features
from interaction_analyzer import analyze_interactions
from energy_model import compute_binding_energy
from dl_model import predict_dl
from hotspot_detector import detect_hotspots
from visualizer import show_structure
from heatmap_plot import interaction_heatmap

st.title("DeepAptaBind v3")

parser=PDBParser(PERMISSIVE=True,QUIET=True)

st.sidebar.header("Input")

mode=st.sidebar.radio(
"Choose input",
["Upload PDB","Fetch from RCSB"]
)

pdb_string=None

if mode=="Upload PDB":

    file=st.file_uploader("Upload PDB",type=["pdb"])

    if file:
        pdb_string=file.getvalue().decode()

if mode=="Fetch from RCSB":

    pdb_id=st.text_input("Enter PDB ID")

    if pdb_id:

        pdb_string=fetch_pdb(pdb_id)

if pdb_string:

    structure=parser.get_structure(
        "complex",
        StringIO(pdb_string)
    )

    protein,aptamer=detect_chains(structure)

    st.write("Protein chains:",protein)
    st.write("Aptamer chains:",aptamer)

    p_chain=st.selectbox("Protein chain",protein)
    a_chain=st.selectbox("Aptamer chain",aptamer)

    protein_atoms=[]
    aptamer_atoms=[]

    for model in structure:
        for chain in model:

            if chain.id==p_chain:
                for atom in chain.get_atoms():
                    protein_atoms.append(atom.coord)

            if chain.id==a_chain:
                for atom in chain.get_atoms():
                    aptamer_atoms.append(atom.coord)

    features=extract_features(protein_atoms,aptamer_atoms)

    interactions=analyze_interactions(protein_atoms,aptamer_atoms)

    energy=compute_binding_energy(features,interactions)

    dl_score=predict_dl(features)

    hotspots=detect_hotspots(interactions)

    st.header("Binding Prediction")

    col1,col2=st.columns(2)

    col1.metric("Physics ΔG",f"{energy:.2f} kcal/mol")

    col2.metric("DL Score",f"{dl_score:.2f}")

    st.header("Interactions")

    st.json(interactions)

    st.header("Hotspots")

    st.json(hotspots)

    fig=interaction_heatmap(interactions)

    st.pyplot(fig)

    st.header("3D Visualization")

    show_structure(pdb_string,p_chain,a_chain)

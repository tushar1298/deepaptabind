import streamlit as st
from Bio.PDB import PDBParser
from io import StringIO

from chain_detector import detect_chains
from feature_extractor import extract_features
from interaction_analyzer import analyze_interactions
from energy_model import compute_binding_energy
from gnn_model import predict_dl
from visualizer import show_structure
from plots import interaction_barplot
from utils import fetch_pdb

st.title("DeepAptaBind")
st.subheader("Protein–Aptamer Deep Learning Binding Predictor")

parser = PDBParser(PERMISSIVE=True, QUIET=True)

st.sidebar.header("Input Options")

input_method = st.sidebar.radio(
    "Choose input method",
    ["Upload PDB", "Fetch from RCSB"]
)

pdb_string = None

# Upload option
if input_method == "Upload PDB":

    uploaded = st.file_uploader("Upload PDB file", type=["pdb"])

    if uploaded:
        pdb_string = uploaded.getvalue().decode("utf-8")

# Fetch option
if input_method == "Fetch from RCSB":

    pdb_id = st.text_input("Enter PDB ID")

    if pdb_id:

        with st.spinner("Fetching structure from RCSB..."):
            pdb_string = fetch_pdb(pdb_id)

        if pdb_string is None:
            st.error("Could not fetch structure")

# Continue if structure loaded
if pdb_string:

    structure = parser.get_structure(
        "complex",
        StringIO(pdb_string)
    )

    protein_chains, rna_chains = detect_chains(structure)

    st.write("Detected Protein Chains:", protein_chains)
    st.write("Detected Aptamer Chains:", rna_chains)

    if len(protein_chains) == 0 or len(rna_chains) == 0:
        st.error("No protein–RNA complex detected")
        st.stop()

    p_chain = st.selectbox("Select Protein Chain", protein_chains)
    r_chain = st.selectbox("Select Aptamer Chain", rna_chains)

    protein_atoms = []
    rna_atoms = []

    for model in structure:
        for chain in model:

            if chain.id == p_chain:
                for atom in chain.get_atoms():
                    protein_atoms.append(atom.coord)

            if chain.id == r_chain:
                for atom in chain.get_atoms():
                    rna_atoms.append(atom.coord)

    features = extract_features(protein_atoms, rna_atoms)

    interactions = analyze_interactions(protein_atoms, rna_atoms)

    energy = compute_binding_energy(features, interactions)

    dl_score = predict_dl(features)

    st.header("Binding Prediction")

    col1, col2 = st.columns(2)

    col1.metric("Physics ΔG", f"{energy:.2f} kcal/mol")
    col2.metric("Deep Learning Score", f"{dl_score:.2f}")

    st.header("Interaction Summary")

    st.json(interactions)

    fig = interaction_barplot(interactions)

    st.pyplot(fig)

    st.header("3D Structure Visualization")

    show_structure(pdb_string, p_chain, r_chain)

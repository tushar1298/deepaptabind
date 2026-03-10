import py3Dmol
import streamlit as st

def show_structure(pdb_string, protein_chain=None, rna_chain=None):

    view = py3Dmol.view(width=900, height=600)

    view.addModel(pdb_string, "pdb")

    # Protein style
    if protein_chain:
        view.setStyle(
            {"chain": protein_chain},
            {"cartoon": {"color": "blue"}}
        )

    # Aptamer style
    if rna_chain:
        view.setStyle(
            {"chain": rna_chain},
            {"stick": {"colorscheme": "greenCarbon"}}
        )

    # Default style
    view.setStyle(
        {"not": {"chain": [protein_chain, rna_chain]}},
        {"cartoon": {"color": "grey"}}
    )

    view.zoomTo()

    html = view._make_html()

    st.components.v1.html(html, height=600)

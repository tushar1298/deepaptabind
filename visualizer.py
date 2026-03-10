import py3Dmol
import streamlit as st

def show_structure(pdb_string,protein_chain,aptamer_chain):

    view=py3Dmol.view(width=900,height=600)

    view.addModel(pdb_string,"pdb")

    view.setStyle({"chain":protein_chain},
                  {"cartoon":{"color":"blue"}})

    view.setStyle({"chain":aptamer_chain},
                  {"stick":{"colorscheme":"greenCarbon"}})

    view.zoomTo()

    html=view._make_html()

    st.components.v1.html(html,height=600)

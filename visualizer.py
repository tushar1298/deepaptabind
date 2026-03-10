import py3Dmol
import streamlit as st

def show_structure(pdb_string):

    view=py3Dmol.view(width=800,height=500)

    view.addModel(pdb_string,'pdb')

    view.setStyle({'cartoon':{'color':'spectrum'}})

    view.zoomTo()

    view_html=view._make_html()

    st.components.v1.html(view_html,height=500)

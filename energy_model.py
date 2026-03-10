from config import ENERGY_WEIGHTS

def compute_binding_energy(features,interactions):

    contacts=features["contacts"]
    hbonds=interactions["hbonds"]

    vdw = contacts * -0.10
    electro = contacts * -0.05
    hbond = hbonds * -0.50
    stacking = contacts * -0.03
    desolv = contacts * -0.02

    energy = (
        ENERGY_WEIGHTS["vdw"]*vdw+
        ENERGY_WEIGHTS["electro"]*electro+
        ENERGY_WEIGHTS["hbond"]*hbond+
        ENERGY_WEIGHTS["stacking"]*stacking+
        ENERGY_WEIGHTS["desolv"]*desolv
    )

    return energy

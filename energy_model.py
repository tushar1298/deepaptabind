def compute_binding_energy(features,interactions):

    contacts=features["contacts"]
    hbonds=interactions["hbonds"]
    stacking=interactions["stacking"]
    electro=interactions["electrostatic"]

    vdw = contacts * -0.10
    hbond = hbonds * -1.5
    stack = stacking * -0.7
    elec = electro * -0.3

    energy = vdw + hbond + stack + elec

    return energy

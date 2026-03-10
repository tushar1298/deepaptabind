def detect_hotspots(interactions):

    hotspots={}

    for k,v in interactions.items():

        if v>5:
            hotspots[k]="Strong"

        elif v>2:
            hotspots[k]="Moderate"

        else:
            hotspots[k]="Weak"

    return hotspots

import requests

def fetch_pdb(pdb_id):

    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"

    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.text

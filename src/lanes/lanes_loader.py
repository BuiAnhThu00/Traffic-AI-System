import numpy as np, yaml
from typing import List

def load_lanes_from_yaml(path: str) -> tuple[list[np.ndarray], dict]:
    with open(path,'r',encoding='utf-8') as f:
        cfg = yaml.safe_load(f)
    zones=[]
    for poly in cfg['lanes']:
        zones.append(np.array(poly, dtype=np.int32))
    return zones, cfg

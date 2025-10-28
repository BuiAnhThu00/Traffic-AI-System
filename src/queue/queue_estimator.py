import cv2, numpy as np
from typing import List, Dict
from ..core.datatypes import Detection

def estimate_queue(dets: List[Detection], lanes: List[np.ndarray]) -> Dict[str,int]:
    q = {f'lane_{i}':0 for i in range(len(lanes))}
    for d in dets:
        x1,y1,x2,y2 = d.bbox
        cx,cy = (x1+x2)//2, (y1+y2)//2
        for i,zone in enumerate(lanes):
            if cv2.pointPolygonTest(zone, (float(cx),float(cy)), False) >= 0:
                q[f'lane_{i}'] += 1
                break
    return q

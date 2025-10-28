import numpy as np
from typing import List
from ..core.datatypes import Detection

class VehicleDetector:
    CLASSES = ['car','motorbike','bus']
    def __init__(self, roi_mask_path: str | None = None): self.roi_mask_path = roi_mask_path
    def detect(self, frame) -> List[Detection]:
        h,w = frame.shape[:2]
        out=[]
        for _ in range(np.random.randint(6,14)):
            x1,y1 = np.random.randint(0,w//2), np.random.randint(0,h//2)
            x2,y2 = x1 + np.random.randint(26,42), y1 + np.random.randint(26,42)
            cls = np.random.choice(self.CLASSES).item()
            out.append(Detection((int(x1),int(y1),int(x2),int(y2)), cls))
        return out

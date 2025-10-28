from typing import List
from ..core.datatypes import Detection
class SimpleTracker:
    def __init__(self): self._id=1
    def update(self, dets: List[Detection]) -> List[Detection]:
        for d in dets: d.id, self._id = self._id, self._id+1
        return dets

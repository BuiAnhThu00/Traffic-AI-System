import cv2
from typing import List, Dict
from ..core.datatypes import Detection

def draw_overlays(frame, dets: List[Detection], queue: Dict[str,int], phase: str):
    for d in dets:
        x1,y1,x2,y2 = d.bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        label = f"{d.cls}{'#'+str(d.id) if d.id else ''}"
        cv2.putText(frame,label,(x1,max(15,y1-5)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
    cv2.putText(frame, f"Green: {phase}", (20,30), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255),2)
    y=60
    for k,v in queue.items():
        cv2.putText(frame, f"{k}: {v}", (20,y), cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),1)
        y+=20
    return frame

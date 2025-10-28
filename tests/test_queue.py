import numpy as np
from src.queue.queue_estimator import estimate_queue
from src.core.datatypes import Detection

def test_queue_inside():
    lane = np.array([[0,0],[100,0],[100,100],[0,100]], dtype=np.int32)
    dets = [Detection((10,10,20,20),'car'), Detection((150,150,160,160),'car')]
    q = estimate_queue(dets, [lane])
    assert q['lane_0'] == 1

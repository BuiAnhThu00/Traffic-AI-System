from src.control.caps_scheduler import CAPSScheduler
import time

def test_min_green():
    s = CAPSScheduler(['l0','l1'], min_green=5, max_green=30, clock=time.time)
    s.update_queue({'l0':0,'l1':10})
    assert s.decide() == 'l0'

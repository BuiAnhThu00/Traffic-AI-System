import streamlit as st, cv2
from ..lanes.lanes_loader import load_lanes_from_yaml
from ..detect.detector import VehicleDetector
from ..track.tracker import SimpleTracker
from ..queue.queue_estimator import estimate_queue
from ..control.caps_scheduler import CAPSScheduler
from ..visual.overlay import draw_overlays

st.set_page_config(page_title="Traffic AI Dashboard", layout="wide")
cfg_path = st.sidebar.text_input("Config path", "configs/default.yaml")
if st.sidebar.button("Start"):
    lanes, cfg = load_lanes_from_yaml(cfg_path)
    det, trk = VehicleDetector(), SimpleTracker()
    sched = CAPSScheduler([f'lane_{i}' for i in range(len(lanes))],
                          cfg['scheduler']['min_green_s'],
                          cfg['scheduler']['max_green_s'],
                          cfg['scheduler']['alpha_green_age'],
                          cfg['scheduler']['fairness_wait_s'],
                          cfg['scheduler']['switch_margin'])
    cap = cv2.VideoCapture(cfg['video_path'])
    img_slot, q_slot = st.empty(), st.empty()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        dets = trk.update(det.detect(frame))
        q = estimate_queue(dets, lanes)
        sched.update_queue(q); ph = sched.decide()
        vis = draw_overlays(frame.copy(), dets, q, ph)
        img_slot.image(cv2.cvtColor(vis, cv2.COLOR_BGR2RGB), caption=f"Green: {ph}", use_column_width=True)
        q_slot.write(q)
    cap.release()
else:
    st.info("Set config and click Start.")

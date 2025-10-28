import yaml, cv2
from ..io.video_reader import VideoReader
from ..io.video_writer import VideoWriter
from ..detect.detector import VehicleDetector
from ..track.tracker import SimpleTracker
from ..lanes.lanes_loader import load_lanes_from_yaml
from ..queue.queue_estimator import estimate_queue
from ..control.caps_scheduler import CAPSScheduler
from ..visual.overlay import draw_overlays

def run_offline(cfg_path='configs/default.yaml'):
    lanes, cfg = load_lanes_from_yaml(cfg_path)
    vr = VideoReader(cfg['video_path'])
    vw = None
    det = VehicleDetector()
    trk = SimpleTracker()
    sched = CAPSScheduler([f'lane_{i}' for i in range(len(lanes))],
                          cfg['scheduler']['min_green_s'],
                          cfg['scheduler']['max_green_s'],
                          cfg['scheduler']['alpha_green_age'],
                          cfg['scheduler']['fairness_wait_s'],
                          cfg['scheduler']['switch_margin'])
    stats={'frames':0,'switches':0}
    last = sched.phase
    while True:
        ret, frame = vr.read()
        if not ret: break
        if vw is None:
            h,w = frame.shape[:2]
            vw = VideoWriter(cfg['output']['path'], vr.fps, w, h)
        dets = trk.update(det.detect(frame))
        q = estimate_queue(dets, lanes)
        sched.update_queue(q)
        ph = sched.decide()
        if ph != last:
            stats['switches'] += 1
            last = ph
        vis = draw_overlays(frame.copy(), dets, q, ph)
        if cfg['output']['save_video']:
            vw.write(vis)
        stats['frames'] += 1
    if vw: vw.release()
    vr.release()
    return stats

if __name__ == '__main__':
    print(run_offline())

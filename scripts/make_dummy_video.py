import cv2, numpy as np, os
os.makedirs('data', exist_ok=True)
def make(path='data/sample_traffic_video.mp4', W=640, H=360, secs=8, fps=15):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    vw = cv2.VideoWriter(path, fourcc, fps, (W,H))
    objs=[{'x':50,'y':300,'vx':2,'vy':-1,'c':(255,0,0)},
          {'x':100,'y':320,'vx':3,'vy':-2,'c':(0,255,0)},
          {'x':500,'y':60,'vx':-2,'vy':1,'c':(0,0,255)}]
    for _ in range(secs*fps):
        frame = np.zeros((H,W,3), np.uint8)
        cv2.rectangle(frame,(50,50),(150,200),(60,60,60),1)
        cv2.rectangle(frame,(200,50),(300,200),(60,60,60),1)
        for o in objs:
            o['x'] += o['vx']; o['y'] += o['vy']
            x,y = int(o['x']), int(o['y'])
            cv2.rectangle(frame,(x,y),(x+30,y+20), o['c'], -1)
        vw.write(frame)
    vw.release()
    print(f"Wrote {path}")
if __name__ == '__main__': make()

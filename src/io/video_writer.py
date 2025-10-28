import cv2
class VideoWriter:
    def __init__(self, path:str, fps:float, width:int, height:int):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.w = cv2.VideoWriter(path, fourcc, fps, (width, height))
    def write(self, frame): self.w.write(frame)
    def release(self): self.w.release()

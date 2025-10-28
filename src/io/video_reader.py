import cv2
class VideoReader:
    def __init__(self, path:str):
        self.cap = cv2.VideoCapture(path)
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open video: {path}")
        self.fps = self.cap.get(cv2.CAP_PROP_FPS) or 15.0
    def read(self): return self.cap.read()
    def release(self): self.cap.release()

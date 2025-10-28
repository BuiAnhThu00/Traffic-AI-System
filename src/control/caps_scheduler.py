import time
from typing import Dict, List

class CAPSScheduler:
    def __init__(self, lane_ids: List[str], min_green=8, max_green=45, alpha_green_age=0.05, fairness_wait_s=20, switch_margin=0.5, clock=time.time):
        self.lane_ids = lane_ids
        self.min_green, self.max_green = min_green, max_green
        self.alpha_green_age, self.fairness_wait_s = alpha_green_age, fairness_wait_s
        self.switch_margin, self.clock = switch_margin, clock
        self._phase = lane_ids[0]
        self._t_start = clock()
        self._last_served: Dict[str, float] = {lid: (self._t_start if lid==self._phase else 0.0) for lid in lane_ids}
        self._queue: Dict[str,int] = {lid:0 for lid in lane_ids}

    def update_queue(self, q: Dict[str,int]): self._queue.update(q)

    def _score(self, lane: str) -> float:
        now = self.clock()
        q = self._queue.get(lane,0)
        starved = max(0.0, (now - self._last_served.get(lane,0.0) - self.fairness_wait_s)/self.fairness_wait_s)
        fairness = 0.5 * starved
        green_age = now - self._t_start if lane == self._phase else 0.0
        penalty = self.alpha_green_age * green_age
        return q + fairness - penalty

    def decide(self) -> str:
        now = self.clock()
        elapsed = now - self._t_start
        if elapsed < self.min_green:
            return self._phase
        current_score = self._score(self._phase)
        best_lane, best_score = self._phase, current_score
        for lid in self.lane_ids:
            s = self._score(lid)
            if s > best_score: best_lane, best_score = lid, s
        if best_lane != self._phase and (best_score > current_score + self.switch_margin or elapsed >= self.max_green):
            self._phase = best_lane
            self._t_start = now
            self._last_served[best_lane] = now
        return self._phase

    @property
    def phase(self) -> str: return self._phase

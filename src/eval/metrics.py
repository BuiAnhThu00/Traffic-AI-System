def mae(pred, true):
    n = max(1,len(pred))
    return sum(abs(p-t) for p,t in zip(pred,true))/n

def f1(tp,fp,fn):
    d = 2*tp + fp + fn
    return 0.0 if d==0 else (2*tp)/d

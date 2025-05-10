from pypssfss import analyze, atoutputs, extract_result, Layer, mm, ThetaPhi
import numpy
import math
from juliacall import Main as jl

def test_pypssfss():
    steer = ThetaPhi(0,0)
    fghz = 10
    w = 10
    devnull = jl.seval("devnull")
    strata = [Layer(), Layer(epsr=10, width=w*mm, tandel=0.02), Layer()]
    results = analyze(strata, fghz, steer, 
                      logfile = devnull,
                      resultfile = devnull, 
                      showprogress = False)

    outputs = extract_result(results, atoutputs("fghz s11db(te,te) s11ang(te,te)"))
    f, s11db, s11ang = map(numpy.array, zip(*outputs))
    print(type(f), ", ", f[0])
    print(type(s11db), ", ", s11db)
    print(type(s11ang), ", ", s11ang)
    assert f[0] == fghz, "Bad frequency"
    assert math.isclose(s11db[0], -7.92209513, abs_tol=1e-8)
    assert math.isclose(s11ang[0], -131.16817847, abs_tol=1e-8)

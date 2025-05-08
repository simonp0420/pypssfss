from collections import namedtuple

# Definitions for setting up steering
ThetaPhi = namedtuple('ThetaPhi', ['theta', 'phi'])
ThetaPhi.__doc__ = "A namedtuple with fields 'theta' and 'phi' used to specify scan angles in pypssfss"

PhiTheta = namedtuple('PhiTheta', ['phi', 'theta'])
PhiTheta.__doc__ = "A namedtuple with fields 'phi' and 'theta' used to specify scan angles in pypssfss"

Psi1Psi2 = namedtuple('Psi1Psi2', ['psi1', 'psi2'])
Psi1Psi2.__doc__ = "A namedtuple with fields 'psi1' and 'psi2' used to specify incremental phase shifts in pypssfss"

Psi2Psi1 = namedtuple('Psi2Psi1', ['psi2', 'psi1'])
Psi2Psi1.__doc__ = "A namedtuple with fields 'psi2' and 'psi1' used to specify incremental phase shifts in pypssfss"


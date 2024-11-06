import numpy
from qiskit.circuit import QuantumCircuit, ParameterVector

def double_excitation_circuit():
    params = ParameterVector("theta", 1)
    qc = QuantumCircuit(4)
    #qc.x(0)
    #qc.x(2)
    #--
    qc.cx(3, 2)
    #--
    qc.cx(3, 0)
    #--
    qc.rz(-numpy.pi/2, 0), qc.s(2), qc.h(3)
    #--
    qc.cx(2, 0), qc.cx(3, 1)
    #--
    qc.rz(numpy.pi/2, 0), qc.ry(params[0]/8, 1), qc.ry(-params[0]/8, 3)
    #--
    qc.cz(0, 3)
    #--
    qc.cx(0, 1), qc.ry(-params[0]/8, 3)
    #--
    qc.ry(params[0]/8, 1)
    #--
    qc.cx(2, 1)
    #--
    qc.cx(2, 3)
    #--
    qc.rz(numpy.pi/2, 2), qc.ry(-params[0]/8, 1), qc.ry(params[0]/8, 3)
    #--
    qc.cx(0, 1)
    #--
    qc.cz(0, 3)
    #--
    qc.ry(-params[0]/8, 1), qc.ry(params[0]/8, 3)
    #--
    qc.cx(3, 1)
    #--
    qc.h(3)
    #--
    qc.cx(3, 2)
    #--
    qc.s(3)
    #--
    qc.rz(-numpy.pi/2, 2)
    #--
    qc.cx(2, 0)
    return qc
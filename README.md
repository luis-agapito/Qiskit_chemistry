# Ground-state energy of $H_2$ using Qiskit.
<p align="middle">
<img src="figures/pic0.png" width="150" />
</p>
Chemistry methods such as Coupled Cluster, Configuration Interaction, Multi-configuration SCF, etc can yield accurate energies with *chemical accuracy* (errors < 0.1 kcal/mol); however, their computational cost is too expensive so that only small molecules (containing few tens of atoms) can be calculated with classical computers. Fortunately, these chemical calculations have been identified as the type of problem in which Quantum Computing could offer a definite advantage by reaching solutions in polynomial time instead of exponential time.

The notebook linked here [h2.ipynb](http://nbviewer.org/github/luis-agapito/Qiskit_chemistry/blob/main/h2.ipynb?flush_cache=True) shows the workflow for calculating molecular energies with quantum computing using IBM's Qiskit programming framework.

We compare five different ansatzes and highlight the difference in cost and complexity between the popular Coupled-Cluster ansatzes and a simple and intuitive *ad hoc* ansatz. The latter considers one double excitation as the relevant mechanism that captures the chemistry of the system; despite its simplicity it outperforms the others in terms of accuracy, speed, number of layers and parameters in the circuits.

<p align="middle">
<img src="figures/pic1.png" width="200" />
</p>

To construct the *ad hoc* ansatz we implemented the quantum circuit proposed in Ref.[Anselmetti2021].

<p align="middle">
<img src="figures/pic3.png" width="400" />
</p>

 Qiskit is a rapidly evolving codebase; all code presented here has been tested with the last versions available as of November 2024.
```
notebook                          7.2.2
qiskit                            1.2.4
qiskit-aer                        0.15.1
qiskit-algorithms                 0.3.1
qiskit-nature                     0.7.2
Python 3.13.0
```
`
## References

[Anselmetti2021] Local, expressive, quantum-number-preserving VQE ansätze for fermionic systems, New Journal of Physics 23 (11), 2021.

"""Graphical model for Shear

This is created using daft, which can be installed via

>$ pip install daft

Jake Vanderplas <jakevdp@cs.washington.edu>
"""

from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft
import matplotlib.pyplot as plt

# Instantiate the PGM.
pgm = daft.PGM([6.0, 4.5], origin=[1.3, 1.0])

# Physics to matter distribution and atmosphere
pgm.add_node(daft.Node("matter", r"$\Omega$", 2.8, 5.0))

#pgm.add_node(daft.Node("noise model", r'$\Sigma$', 1.0, 4.3))
pgm.add_node(daft.Node("intrinsic shape", r'$\Sigma$', 1.9, 4.1))
pgm.add_node(daft.Node("mass field", r'$M$', 2.8, 4.1))
pgm.add_node(daft.Node("atmosphere", "$A$", 5.0, 4.1))


pgm.add_node(daft.Node('PSFy', r'$PSF^{(i)}$', 6, 3.0,
                       aspect=2.2, observed=True))

#pgm.add_node(daft.Node("noise", r'$\sigma^{(j)}$', 1.0, 3.0))
pgm.add_node(daft.Node("int ellip", r'$\varepsilon_{\rm int}^{(j)}$', 1.9, 3.0))
pgm.add_node(daft.Node("true shear", r'$\gamma_{\rm true}^{(j)}$', 2.8, 3.0))
pgm.add_node(daft.Node("PSFx", r'$PSF^{(j)}$', 4.1, 3.0, aspect=2.2))

pgm.add_node(daft.Node("obs ellip", r'$\varepsilon_{\rm obs}^{(j)}$',
                       3.3, 1.8, observed=True))

pgm.add_edge("matter", "mass field")
#pgm.add_edge("noise model", "noise")
pgm.add_edge("mass field", "true shear")
pgm.add_edge("intrinsic shape", "int ellip")

#pgm.add_edge("noise", "obs ellip")
pgm.add_edge("true shear", "obs ellip")
pgm.add_edge("int ellip", "obs ellip")
pgm.add_edge("true shear", "obs ellip")
pgm.add_edge("PSFx", "obs ellip")

pgm.add_edge('atmosphere', 'PSFy')
pgm.add_edge('atmosphere', 'PSFx')


pgm.add_plate(daft.Plate([1.5, 1.5, 3.4, 2],
                         label=r"$j = 1, \cdots, N_{\rm gal}$",
                         shift=-0.1))

pgm.add_plate(daft.Plate([5.2, 2.5, 1.7, 1],
                         label=r"$i = 1, \cdots, N_{\rm star}$",
                         shift=-0.1))



# Render and save.
pgm.render()
pgm.figure.savefig("figures/lensing_simple.pdf", dpi=150)

#plt.show()

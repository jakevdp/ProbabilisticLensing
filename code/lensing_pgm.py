"""Graphical model for Shear

This is created using daft, which can be installed via

>$ pip install daft

Jake Vanderplas <jakevdp@cs.washington.edu>
"""

#from matplotlib import rc
#rc("font", family="serif", size=12)
#rc("text", usetex=True)

import daft

# Instantiate the PGM.
pgm = daft.PGM([7.4, 4.8], origin=[0.3, 1.2])

# Physics to matter distribution and atmosphere
pgm.add_node(daft.Node("physics", "Physics", 3.7, 5.5, fixed=True))
pgm.add_node(daft.Node("matter", r"$\Omega$", 2.8, 4.8))

pgm.add_node(daft.Node("noise model", r'$\Sigma$', 1.0, 4.0))
pgm.add_node(daft.Node("intrinsic shape", r'$\varepsilon_{\rm int}$', 1.8, 4.0))
pgm.add_node(daft.Node("gal locs", r'$\rho_{\rm gal}$', 2.5, 4.0))
pgm.add_node(daft.Node("shear field", r'$\gamma$', 3.2, 4.0))
pgm.add_node(daft.Node("atmosphere", "atmos", 5.0, 4.3, aspect=2.0))
pgm.add_node(daft.Node("galaxy model", "milky way", 6.5, 4.5, aspect=3.0))

pgm.add_node(daft.Node('PSFy', r'$PSF(y^{(i)})$', 6, 3.0,
                       aspect=2.2, observed=True))
pgm.add_node(daft.Node('y', r'$y^{(i)}$', 7, 3.0, observed=True))

pgm.add_node(daft.Node("noise", r'$\sigma^{(j)}$', 1.0, 3.0))
pgm.add_node(daft.Node("x", r'$x^{(j)}$', 2.5, 3.0, observed=True))
pgm.add_node(daft.Node("int ellip", r'$\varepsilon_{\rm int}^{(j)}$', 1.8, 3.0))
pgm.add_node(daft.Node("true shear", r'$\gamma_{\rm true}^{(j)}$', 3.2, 3.0))
pgm.add_node(daft.Node("PSFx", r'$PSF(x^{(j)})$', 4.1, 3.0, aspect=2.2))

pgm.add_node(daft.Node("obs ellip", r'$\varepsilon_{\rm obs}^{(j)}$',
                       3.3, 1.8, observed=True))

pgm.add_edge("physics", "matter")
pgm.add_edge("physics", "galaxy model")
pgm.add_edge("matter", "gal locs")
pgm.add_edge("matter", "shear field")
pgm.add_edge("noise model", "noise")
pgm.add_edge("shear field", "true shear")
pgm.add_edge("gal locs", "x")
pgm.add_edge("intrinsic shape", "int ellip")

pgm.add_edge("noise", "obs ellip")
pgm.add_edge("true shear", "obs ellip")
pgm.add_edge("int ellip", "obs ellip")
pgm.add_edge("true shear", "obs ellip")
pgm.add_edge("PSFx", "obs ellip")

pgm.add_edge('atmosphere', 'PSFy')
pgm.add_edge('galaxy model', 'y')
pgm.add_edge('atmosphere', 'PSFx')


pgm.add_plate(daft.Plate([0.5, 1.5, 4.5, 2],
                         label=r"$j = 1, \cdots, N_{\rm gal}$",
                         shift=-0.1))

pgm.add_plate(daft.Plate([5.2, 2.5, 2.3, 1],
                         label=r"$i = 1, \cdots, N_{\rm star}$",
                         shift=-0.1))



# Render and save.
pgm.render()
pgm.figure.savefig("lensing.pdf", dpi=150)
#pgm.figure.savefig("lensing.png", dpi=150)
plt.show()

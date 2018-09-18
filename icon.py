import numpy as np
from scipy.special import gamma
from matplotlib import rc
import matplotlib.pyplot as plt
from itertools import cycle

# Use LaTeX throughout the figure for consistency
# rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
# rc('text', usetex=True)

# Set up the figure.
dpi = 480
fig, ax1 = plt.subplots(1, 1, figsize=(512/dpi, 512/dpi), dpi=dpi,
            gridspec_kw=dict(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    )

SIZE = 1.1

def setup():
    ax1.set_xlim(-SIZE, SIZE)
    ax1.set_ylim(-SIZE, SIZE)
    ax1.set_axis_off()

# The parameter t in the parametric description of the superellipse
t = np.linspace(0, 2*np.pi, 500)

# Build an array of values of p up to pmax and assign the corresponding colours




# exponent, width, height
p = 4
w = 1
h = 0.9
linewidth=1
color = 'k'
fill = '#444444'
text='w'

font = 'clear sans'
fy = -6
fsize = 27
fweight = 700
linespacing = .9


tnames = ['', '-transparent']

for transparent, suffix in enumerate(tnames):
    ax1.cla()
    setup()
    # Draw superellipse
    if not transparent:
        kwargs = {'lw': 1, 'alpha': 1}
        c, s = np.cos(t), np.sin(t)
        x = np.abs(c)**(2/p) * np.sign(c) * w
        y = np.abs(s)**(2/p) * np.sign(s) * h

        ax1.fill(x, y, c=fill, **kwargs)
        ax1.plot(x, y, c=color, **kwargs, linewidth=linewidth)

    # Draw text
    ax1.text(0,
        fy/100,
        '0CC\nNSF',

        family=font,
        fontsize=fsize, weight=fweight, linespacing=linespacing,

        color=text,
        horizontalalignment='center',
        verticalalignment='center',
    )
    plt.savefig(f'logo{suffix}.png', transparent=True)
    # plt.show()

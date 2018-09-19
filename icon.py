import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as patches

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
bottom = '#282828'
top = '#383838'

text='0CC'

fcolor='w'
font = 'clear sans'
fy = -6
fsize = 34
fweight = 700
linespacing = .9


tnames = ['', '-transparent']
def main():
    for transparent, suffix in enumerate(tnames):
        ax1.cla()
        setup()
        # Draw superellipse
        if not transparent:
            kwargs = {'alpha': 1}
            c, s = np.cos(t), np.sin(t)
            x = np.abs(c)**(2/p) * np.sign(c) * w
            y = np.abs(s)**(2/p) * np.sign(s) * h

            # ax1.fill(x, y, c=fill, **kwargs)
            gradient_fill(x, y, c=color, **kwargs, bottom=bottom, top=top, linewidth=linewidth,
                ax=ax1)
            # ax1.plot(x, y, c=color, **kwargs, linewidth=linewidth)

        # Draw text
        ax1.text(0,
            fy/100,
            text,

            family=font,
            fontsize=fsize, weight=fweight, linespacing=linespacing,

            color=fcolor,
            horizontalalignment='center',
            verticalalignment='center',
        )
        plt.savefig(f'logo{suffix}.png', transparent=True)
        # plt.show()


def gradient_fill(x, y, top, bottom, ax=None, zfunc=None, **kwargs):
    """based on https://stackoverflow.com/a/29347731/2683842"""
    if ax is None:
        ax = plt.gca()

    line, = ax.plot(x, y, **kwargs)

    zorder = line.get_zorder() - 1
    alpha = line.get_alpha()
    alpha = 1.0 if alpha is None else alpha

    if zfunc is None:
        h, w = 100, 1
        z = np.empty((h, w, 4), dtype=float)
        rgb = mcolors.colorConverter.to_rgb(top)
        z[:,:,:3] = rgb
        z[:,:,-1] = np.linspace(0, alpha, h)[:,None]
    else:
        z = zfunc(x, y, fill_color=top, alpha=alpha)
    xmin, xmax, ymin, ymax = x.min(), x.max(), y.min(), y.max()

    clippy = []

    # Background fill
    bg = ax.fill(x, y, c=bottom, zorder=zorder)
    # clippy.extend(bg)

    # Gradient fill
    im = ax.imshow(z, aspect='auto', extent=[xmin, xmax, ymin, ymax],
                   origin='lower', zorder=zorder)
    clippy.append(im)

    xy = np.column_stack([x, y])
    # xy = np.vstack([[xmin, ymin], xy, [xmax, ymin], [xmin, ymin]])
    clip_path = patches.Polygon(xy, facecolor='none', edgecolor='none', closed=True)
    ax.add_patch(clip_path)

    for clip in clippy:
        clip.set_clip_path(clip_path)
    return line, im


main()

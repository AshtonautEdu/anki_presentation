import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.linspace(-3, 3, 100)
    y = np.exp(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlabel('$x$', fontsize='xx-large')
    ax.set_ylabel('$e^x$', fontsize='xx-large')

    plt.savefig('./img/e.svg', format='svg', bbox_inches='tight')

    plt.show()
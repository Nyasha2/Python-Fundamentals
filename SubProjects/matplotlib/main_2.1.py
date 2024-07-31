from lab06 import plot_spurious_correlation

if __name__ == "__main__":
    years = [i for i in range(2000, 2010)]
    revenue = [1.196, 1.176, 1.269, 1.24, 1.307, 1.435, 1.601, 1.654, 1.803, 1.734]
    doctorates = [861, 830, 809, 867, 848, 1129, 1453, 1656, 1787, 1611]
    plot_spurious_correlation(years, revenue, doctorates)
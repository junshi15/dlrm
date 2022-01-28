import matplotlib.pyplot as plt

infile = 'feat_14'
counts = []
freqs = []

def plot_hist(infile):
    with open(infile) as f:
        for l in f:
            count, freq = l.split(',')
            counts.append(int(count))
            freqs.append(int(freq))

    plt.bar(counts, freqs, color='black')
    plt.xscale("log")
    plt.xlabel('example count per feature value')
    plt.ylabel('number of feature values')
    plt.title('categorical feature #1')
    plt.show()

plot_hist(infile)
    

from scipy import signal
from pylab import *
from scipy import linalg
from numpy.linalg import lstsq


def ma(x, n = 5):
    b = repeat(1.0/n, n) #Create impulse response
    xf = signal.lfilter(b, 1, x) #Filter the signal
    return(xf)

def plot_freqz(b,a=1):
    w,h = signal.freqz(b,a)
    h_dB = 20 * log10 (abs(h))
    plot(w/pi, h_dB)
    ylim([max(min(h_dB), -100) , 5])
    ylabel('Magnitude (db)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Amplitude response')

def plot_phasez(b, a=1):
    w,h = signal.freqz(b,a)
    h_Phase = unwrap(arctan2(imag(h),real(h)))
    plot(w/pi, h_Phase)
    ylabel('Phase (radians)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Phase response')

def plot_impz(b, a = 1):
    if type(a)== int: #FIR
        l = len(b)
    else: # IIR
        l = 100
    impulse = repeat(0.,l); impulse[0] =1.
    x = arange(0,l)
    response = signal.lfilter(b, a, impulse)
    stem(x, response, linefmt='k-', basefmt='k-', markerfmt='ko')
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Impulse response')

def plot_stepz(b, a = 1):
    if type(a)== int: #FIR
        l = len(b)
    else: # IIR
        l = 100
    impulse = repeat(0.,l); impulse[0] =1.
    x = arange(0,l)
    response = signal.lfilter(b,a,impulse)
    step = cumsum(response)
    plot(x, step)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Step response')


def plot_filterz(b, a=1):
    subplot(221)
    plot_freqz(b, a)
    subplot(222)
    plot_phasez(b, a)
    subplot(223)
    plot_impz(b, a)
    subplot(224)
    plot_stepz(b, a)
    subplots_adjust(hspace=0.3, wspace = 0.3)

def periodogram(x, Fs = 1.0, scale="linear"):
    N = len(x)
    k = N/2+1
    P = fft(x)[:k]
    M = 2*np.abs(P)/N
    Sj = M**2/2
    f =  Fs*linspace(0, 0.5, k) #Scale by sample rate
    if scale = "linear":
        plot(f, Sj)
        ylabel('Power/frequency (dB/rad/sample)')
    else:
        Sj_db = 20*log10(2*(np.abs(h)/len(h)))
        plot(f, Sj_db)
        ylabel('Power / frequency ')
    xlabel('Frequency')
    

def autocorr(x, lag=10):
    c = correlate(x, x, 'full')
    mid = floor(len(c)/2)
    acov = c[mid:mid+lag]
    acor = acov/acov[0]
    return(acor)
    
def arcov(x, p = 5):
    n = len(x) - p
    X = zeros((n, p))
    y = x[p:]
    for i in range(p, n+p):
        ind = range(i-1, i-p-1, -1)
        #X[i-p, 0] = 1        
        X[i-p, ] = x[ind]
    phi =  lstsq(X, y)[0]
    return(phi)
    
def aryw(x, p=5):
    x = x - mean(x)
    ac = autocorr(x, p+1)
    R = linalg.toeplitz(ac[:p])
    r = ac[1:p+1]
    params = inv(R).dot(r)
    return(params)
    
def pyulear(x, p=5):
    params = aryw(x, p)
    a = concatenate([ones(1), -params])
    w, h = signal.freqz(1, a)
    h_db = 20*log10(2*(np.abs(h)/len(h)))
    plot(w/pi, h_db)
    xlabel(r'Normalized Frequency ($\times \pi$rad/sample)')
    ylabel(r'Power/frequency (dB/rad/sample)')
    title(r'Yule-Walker AR Spectral Density Estimate')

def pcov(x, p=5):
    params = arcov(x, p)
    a = concatenate([ones(1), -params])
    w, h = signal.freqz(1, a)
    h_db = 20*log10(2*(np.abs(h)/len(h)))
    plot(w/pi, h_db)
    xlabel(r'Normalized Frequency ($\times \pi$rad/sample)')
    ylabel(r'Power/frequency (dB/rad/sample)')
    title(r'Least Squares AR Spectral Density Estimate')

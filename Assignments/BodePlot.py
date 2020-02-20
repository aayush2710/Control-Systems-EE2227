from scipy import signal
import matplotlib.pyplot as plt
s1 = signal.lti([1], [1,202, 400]) 
#Transfer function is(1/(s^2+ 202s + 400))
w, mag, phase = signal.bode(s1)
plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.show()
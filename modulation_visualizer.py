import numpy as np
import matplotlib.pyplot as plt

# 1. Setup the Signals
t = np.arange(0, 1, 0.001)  # Time axis: 0 to 1 second
f_carrier = 10              # Carrier frequency: 10 Hz (Low for visualization)
f_bit = 2                   # Bit frequency: 2 Hz (2 bits per second)

# Generate Random Binary Data (Square Wave)
# We create a pattern: 1, 0, 1, 0 for clear visualization
data_signal = np.array([])
for i in range(len(t)//500): # Split into 2 halves
    data_signal = np.concatenate((data_signal, np.ones(250)))  # Logic 1
    data_signal = np.concatenate((data_signal, np.zeros(250))) # Logic 0
# Resize to match 't' exactly if needed
if len(data_signal) < len(t):
    data_signal = np.append(data_signal, np.zeros(len(t)-len(data_signal)))

# Carrier Signal (Sine Wave)
carrier_signal = np.sin(2 * np.pi * f_carrier * t)

# 2. Modulation Logic
# ASK: Amplitude Shift Keying (Data * Carrier)
ask_signal = data_signal * carrier_signal

# FSK: Frequency Shift Keying
# High Freq for '1', Low Freq for '0'
f_high = f_carrier * 2
f_low = f_carrier
fsk_signal = []
for i in range(len(t)):
    if data_signal[i] == 1:
        fsk_signal.append(np.sin(2 * np.pi * f_high * t[i]))
    else:
        fsk_signal.append(np.sin(2 * np.pi * f_low * t[i]))
fsk_signal = np.array(fsk_signal)

# PSK: Phase Shift Keying
# Normal Phase for '1', Inverted Phase for '0'
psk_signal = []
for i in range(len(t)):
    if data_signal[i] == 1:
        psk_signal.append(np.sin(2 * np.pi * f_carrier * t[i]))
    else:
        psk_signal.append(np.sin(2 * np.pi * f_carrier * t[i] + np.pi)) # 180 deg shift
psk_signal = np.array(psk_signal)

# 3. Plotting the Results
plt.figure(figsize=(10, 8))

plt.subplot(5, 1, 1)
plt.title('Binary Data Signal')
plt.plot(t, data_signal, color='black')
plt.grid(True)

plt.subplot(5, 1, 2)
plt.title('Carrier Signal')
plt.plot(t, carrier_signal, color='gray')
plt.grid(True)

plt.subplot(5, 1, 3)
plt.title('ASK (Amplitude Shift Keying)')
plt.plot(t, ask_signal, color='blue')
plt.grid(True)

plt.subplot(5, 1, 4)
plt.title('FSK (Frequency Shift Keying)')
plt.plot(t, fsk_signal, color='green')
plt.grid(True)

plt.subplot(5, 1, 5)
plt.title('PSK (Phase Shift Keying)')
plt.plot(t, psk_signal, color='red')
plt.grid(True)

plt.tight_layout()
plt.show()
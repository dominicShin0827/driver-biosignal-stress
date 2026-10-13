
import matplotlib.pyplot as plt
import numpy as np
from src.data_loader import load_driver_data

def plot_driver_signals(record_name, view_seconds=600):
    record = load_driver_data(record_name)
    m_idx = record.sig_name.index('marker')
    e_idx = record.sig_name.index('ECG')
    g_idx = record.sig_name.index('foot GSR')
    
    fs = record.fs
    n_samples = int(view_seconds * fs)
    time = np.arange(n_samples) / fs
    
    plt.figure(figsize=(15, 10))
    
    # ECG 차트 (스크린샷 2번 상단)
    plt.subplot(3, 1, 1)
    plt.plot(time, record.p_signal[:n_samples, e_idx])
    plt.title(f'{record_name} - ECG Signal (First {view_seconds/60} min)')
    
    # GSR 차트 (스크린샷 3번 중간)
    plt.subplot(3, 1, 2)
    plt.plot(time, record.p_signal[:n_samples, g_idx], color='green')
    plt.title(f'{record_name} - GSR Signal')
    
    # Marker 차트 (스크린샷 2번 하단)
    plt.subplot(3, 1, 3)
    plt.plot(time, record.p_signal[:n_samples, m_idx], color='red')
    plt.title(f'{record_name} - Marker Value')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_driver_signals('drive02')


import wfdb
import numpy as np

def load_driver_data(record_name):
    """PhysioNet DriveDB에서 특정 레코드를 읽어옵니다."""
    record = wfdb.rdrecord(record_name, pn_dir='drivedb')
    return record

def get_marker_info(record):
    """마커 채널에서 스파이크 시점과 값을 추출합니다."""
    if 'marker' not in record.sig_name:
        return None
    
    m_idx = record.sig_name.index('marker')
    m_signal = record.p_signal[:, m_idx]
    
    spike_indices = np.where(m_signal > 30)[0]
    
    clean_spikes = []
    if len(spike_indices) > 0:
        clean_spikes.append(spike_indices[0])
        for i in range(1, len(spike_indices)):
            if spike_indices[i] - spike_indices[i-1] > record.fs * 5:
                clean_spikes.append(spike_indices[i])
                
    return [(idx / record.fs / 60, m_signal[idx]) for idx in clean_spikes]

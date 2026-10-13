
# Phase 1: Data Exploration & Marker Analysis
import wfdb
import matplotlib.pyplot as plt
from src.data_loader import load_driver_data, get_marker_info

record = load_driver_data('drive02')
spikes = get_marker_info(record)

print("--- drive02 마커 분석 결과 ---")
if spikes:
    for t, val in spikes:
        print(f"Time: {t:.2f} min | Marker: {val:.2f}")

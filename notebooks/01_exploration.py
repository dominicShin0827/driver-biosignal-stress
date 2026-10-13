
# Phase 1: Data Exploration & Marker Analysis

import wfdb
import matplotlib.pyplot as plt
from src.data_loader import load_driver_data, get_marker_info

# 1. 전체 데이터셋 채널 및 길이 확인 (오늘의 첫 번째 공부)
print("--- DriveDB 전체 레코드 채널 확인 ---")
record_list = wfdb.get_record_list('drivedb')
for n in record_list:
    h = wfdb.rdheader(n, pn_dir='drivedb')
    print(f"Record: {n} | Channels: {h.sig_name} | Length: {round(h.sig_len/h.fs/60,1)} min")

print("\n" + "="*50 + "\n")

# 2. 특정 레코드(drive02) 상세 분석 (오늘의 두 번째 공부)
record = load_driver_data('drive02')
spikes = get_marker_info(record)

print("--- drive02 마커 상세 분석 결과 ---")
if spikes:
    for t, val in spikes:
        print(f"Time: {t:.2f} min | Marker: {val:.2f}")

# 3. 결론
# - drive01, 03 등 일부 레코드에는 'marker' 채널이 없음 (분석 제외 필요)
# - marker의 spike(값 > 30)를 기준으로 구간(Rest, City, Highway) 라벨링 가능성 확인

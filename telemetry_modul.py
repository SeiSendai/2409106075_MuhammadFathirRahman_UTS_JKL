#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : telemetry_modul.py
Tujuan    : Mengklasifikasikan sampel data telemetry cpuUsage (in-uti)
Pembuat   : Muhammad Fathir Rahman - NIM: 2409106075
"""

# Sampel telemetry diturunkan dari digit NIM (2409106075)
sampel_telemetry = {
    "sample_1": 75,  # Diambil dari digit NIM '75'
    "sample_2": 90,  # Nilai variasi tinggi
    "sample_3": 40   # Nilai variasi rendah
}

def klasifikasi_telemetry(data_dict):
    hasil_klasifikasi = {}
    for key, val in data_dict.items():
        if val > 80:
            status = "KRITIS"
        elif 50 <= val <= 80:
            status = "WASPADA"
        else:
            status = "NORMAL"
        hasil_klasifikasi[key] = {"usage": val, "status": status}
    return hasil_klasifikasi

if __name__ == "__main__":
    print(klasifikasi_telemetry(sampel_telemetry))
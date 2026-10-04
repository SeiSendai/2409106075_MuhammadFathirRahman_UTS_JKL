#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : identitas.py
Tujuan    : Menyimpan data identitas cabang dan pembuat ID perangkat
Pembuat   : Muhammad Fathir Rahman - NIM: 2409106075
"""

nim = "2409106075"
nama = "Muhammad Fathir Rahman"
kode_cabang = "075"

def buat_id_perangkat(jenis, nomor):
    return f"{jenis.upper()}-{kode_cabang}-{nomor:02d}"

if __name__ == "__main__":
    print(f"NIM: {nim}, Nama: {nama}, Kode Cabang: {kode_cabang}")
    print("Contoh ID Perangkat:", buat_id_perangkat("router", 1))
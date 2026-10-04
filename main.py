#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : main.py
Tujuan    : Modul utama integrasi dan pembuatan laporan akhir gabungan
Pembuat   : Muhammad Fathir Rahman - NIM: 2409106075
"""

import identitas
import ssh_modul
import snmp_modul
import netconf_modul
import telemetry_modul

class LaporanCabang:
    def __init__(self, nim, nama, kode_cabang):
        self.nim = nim
        self.nama = nama
        self.kode_cabang = kode_cabang

    def tampilkan_laporan(self, res_ssh, res_snmp, res_netconf, res_telemetry):
        print("=" * 60)
        print(f"      LAPORAN OTOMATISASI CABANG VIRTUAL {self.kode_cabang}")
        print("=" * 60)
        print(f"Identitas Pembuat : {self.nama} ({self.nim})")
        print(f"Kode Cabang       : {self.kode_cabang}")
        print("-" * 60)
        
        print("\n1. HASIL AKSES SSH (Paramiko):")
        print(f"   Status: {res_ssh.get('status')}")
        if res_ssh.get('status') == "Sukses":
            for cmd, out in res_ssh['data'].items():
                print(f"   [{cmd}] -> {out}")
        else:
            print(f"   Error: {res_ssh.get('error')}")

        print("\n2. HASIL MONITORING SNMP (PySNMP):")
        print(f"   Status: {res_snmp.get('status')}")
        if res_snmp.get('status') == "Sukses":
            print(f"   sysName: {res_snmp.get('sysName')}")
        else:
            print(f"   Error: {res_snmp.get('error')}")

        print("\n3. HASIL PEMBUATAN PESAN NETCONF:")
        print(res_netconf)

        print("\n4. HASIL KLASIFIKASI TELEMETRY:")
        for k, v in res_telemetry.items():
            print(f"   - {k}: Usage = {v['usage']}% | Status = {v['status']}")
            
        print("=" * 60)

def main():
    res_ssh = ssh_modul.cek_ssh()
    res_snmp = snmp_modul.cek_snmp()
    res_netconf = netconf_modul.buat_pesan_netconf()
    res_telemetry = telemetry_modul.klasifikasi_telemetry(telemetry_modul.sampel_telemetry)

    laporan = LaporanCabang(identitas.nim, identitas.nama, identitas.kode_cabang)
    laporan.tampilkan_laporan(res_ssh, res_snmp, res_netconf, res_telemetry)

if __name__ == "__main__":
    main()
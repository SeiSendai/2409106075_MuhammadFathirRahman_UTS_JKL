#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : ssh_modul.py
Tujuan    : Melakukan koneksi SSH ke VM/Laptop dan mengeksekusi perintah diagnostik
Pembuat   : Muhammad Fathir Rahman - NIM: 2409106075
"""

import paramiko
from identitas import kode_cabang

def cek_ssh(hostname="127.0.0.1", port=22, password="password_vm"):
    username = f"admin_{kode_cabang}"
    perintah_list = ["uname -a", "uptime"]
    hasil = {}
    
    print(f"[*] Menghubungi SSH ke {hostname} dengan user '{username}'...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(hostname=hostname, port=port, username=username, password=password, timeout=5)
        for cmd in perintah_list:
            stdin, stdout, stderr = client.exec_command(cmd)
            hasil[cmd] = stdout.read().decode('utf-8').strip()
        client.close()
        return {"status": "Sukses", "data": hasil}
    except Exception as e:
        return {"status": "Gagal", "error": str(e)}

if __name__ == "__main__":
    print(cek_ssh())
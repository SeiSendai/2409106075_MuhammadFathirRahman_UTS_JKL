#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : snmp_modul.py
Tujuan    : Mengambil sysName perangkat dengan SNMPv2c
Pembuat   : Muhammad Fathir Rahman - NIM: 2409106075
"""

from pysnmp.hlapi import *
from identitas import kode_cabang

def cek_snmp(target_ip="127.0.0.1"):
    community_string = f"comm_{kode_cabang}"
    sys_name_oid = '1.3.6.1.2.1.1.5.0'
    
    print(f"[*] Mengambil sysName SNMP dari {target_ip} (Community: {community_string})...")
    
    try:
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(community_string, mpModel=1),
                   UdpTransportTarget((target_ip, 161), timeout=2, retries=1),
                   ContextData(),
                   ObjectType(ObjectIdentity(sys_name_oid)))
        )

        if errorIndication:
            return {"status": "Gagal", "error": str(errorIndication)}
        elif errorStatus:
            return {"status": "Gagal", "error": errorStatus.prettyPrint()}
        else:
            for varBind in varBinds:
                return {"status": "Sukses", "sysName": str(varBind[1])}
    except Exception as e:
        return {"status": "Gagal", "error": str(e)}

if __name__ == "__main__":
    print(cek_snmp())
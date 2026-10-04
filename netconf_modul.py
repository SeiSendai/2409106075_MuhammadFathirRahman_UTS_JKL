#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : netconf_modul.py
Tujuan    : Membangun pesan XML NETCONF edit-config untuk pembuatan VLAN
Pembuat   : Muhammad Fathir Rahman - NIM: 2409106075
"""

from identitas import kode_cabang

def buat_pesan_netconf():
    vlan_id = kode_cabang  # Nilai "075"
    
    # NETCONF XML Structure dengan penanda layer
    xml_rpc = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- Layer: Transport / Message Layer (RPC Request Wrapper) -->
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  
  <!-- Layer: Operations Layer (<edit-config> operation) -->
  <edit-config>
    <target>
      <running/>
    </target>
    
    <!-- Layer: Content Layer (Data Konfigurasi Spesifik / Data Model) -->
    <config>
      <vlans xmlns="http://openconfig.net/yang/vlan">
        <vlan>
          <vlan-id>{vlan_id}</vlan-id>
          <config>
            <vlan-id>{vlan_id}</vlan-id>
            <name>VLAN_CABANG_{kode_cabang}</name>
            <status>ACTIVE</status>
          </config>
        </vlan>
      </vlans>
    </config>
    
  </edit-config>
</rpc>"""
    return xml_rpc

if __name__ == "__main__":
    print(buat_pesan_netconf())
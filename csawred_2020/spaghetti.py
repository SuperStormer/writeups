from pwn import *
cpuids = [
	c[1:].split('"')[0] for c in """
"AMDisbetter!" – early engineering samples of AMD K5 processor
"AuthenticAMD" – AMD
"CentaurHauls" – IDT WinChip/Centaur (Including some VIA CPU)
"CyrixInstead" – Cyrix/early STMicroelectronics and IBM
"GenuineIntel" – Intel
"TransmetaCPU" – Transmeta
"GenuineTMx86" – Transmeta
"Geode by NSC" – National Semiconductor
"NexGenDriven" – NexGen
"RiseRiseRise" – Rise
"SiS SiS SiS " – SiS
"UMC UMC UMC " – UMC
"VIA VIA VIA " – VIA
"Vortex86 SoC" – DM&P Vortex
"  Shanghai  " – Zhaoxin
"HygonGenuine" – Hygon
"E2K MACHINE" – MCST Elbrus
"bhyve bhyve " – bhyve
" KVMKVMKVM " – KVM
"TCGTCGTCGTCG" – QEMU
"Microsoft Hv" – Microsoft Hyper-V or Windows Virtual PC
" lrpepyh vr" – Parallels (it possibly should be "prl hyperv ", but it is encoded as " lrpepyh vr" due to an endianness mismatch)
"VMwareVMware" – VMware
"XenVMMXenVMM" – Xen HVM
"ACRNACRNACRN" – Project ACRN
" QNXQVMBSQG " – QNX Hypervisor
"VirtualApple" – Apple Rosetta 2
"GenuineAO486" – ao486 CPU[5]
"GenuineIntel" – v586 core[6] (this is identical to the Intel ID string)
""".split("\n")
]
print(cpuids)
inps = [("CPU:" + c) for c in cpuids]
for inp in inps:
	print(inp)
	p = remote("rev.red.csaw.io", 5001)
	p.sendline(inp)
	r = p.recvall()
	if r != b"":
		print(r)
		break
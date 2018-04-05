### Memory Download & Exec for Kernels => 3.17 
Used in pentesting/red teaming engagements for dropping binaries without touching the disk.
This script is a simple proof of concept on how to use memfd_create syscall on x86_64 (http://man7.org/linux/man-pages/man2/memfd_create.2.html). Change the delivery method and obfuscate payloads based on your needs...

Based on https://0x00sec.org/t/super-stealthy-droppers/3715

# benchmark-dhrystone
"DHRYSTONE" Benchmark Program by  Reinhold P. Weicker

# RISC-V RV32I Bare-metal environment implementation
## Repository's purpose
- This repository is for implementing **Dhrystone 2.1** on ***Bare-metal RISC-V RV32I Processors***.
- The main contents will be written in README.md.
- The files that repository provides will be the 'ready to takeoff' state Dhrystone 2.1 for any RV32I bare-metal processor  
(should support UART TX, MMIO.)

## Target Processor
Target processor is [basic_RV32s](https://github.com/RISC-KC/basic_rv32s)' **46F5SP_MMIO_SoC**, which is based on **RV32I46F_5SP** core design.
The processor's Memory map is same as following.
- IMEM(ROM) : 0x0000_0000, 64KB (0:16383)
- DMEM(RAM) : 0x1000_0000, 32KB (0:8191)
- UART_TX : 0x1001_0000
- UART_STATUS_ADDRESS : 0x1001_0004

## Development log
(on-going)

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

## RISC-V RV32I GNU GCC Toolchain setup

1. Clone the toolchain repository. 먼저 클론을 따준다.
```bash
cd ~
git clone https://github.com/riscv-collab/riscv-gnu-toolchain.git
cd riscv-gnu-toolchain
```

2. Install dependency packages. 의존성 패키지들을 설치해준다.
```bash
sudo apt-get update
sudo apt-get install -y \
  autoconf automake autotools-dev curl python3 python3-pip python3-tomli \
  libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex \
  texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev \
  ninja-build git cmake libglib2.0-dev libslirp-dev
```
3. Configure the toolchain build. 여기서부터가 중요하다. 현재 있는 툴체인 폴더에서, configure를 진행해준다.
```bash
cd ~/riscv-gnu-toolchain
./configure --preifx=$HOME/riscv32i-elf --target=riscv32-unknown-elf --with-arch=rv32i --with-abi=ilp32
```

`riscv32i-elf` is the directory where toolchain is built. You can change this directory if needed.
Official manual does with the /opt/riscv directory.
여기서 riscv32i-elf는 툴체인이 빌드 될 디렉토리다. 원하는 폴더명이나 경로로 바꿔도 좋다.
매뉴얼에서는(공식 깃헙 페이지) /opt/riscv로 한다.

4. make
```bash
make -j$(nproc)
```
5. Confirm and register PATH. 확인 및 PATH 등록
```bash
ls $HOME/riscv32i-elf/bin | grep riscv32-unknown-elf-gcc
```

```bash
echo 'export PATH=$HOME/riscv32i-elf/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

```bash
riscv32-unknown-elf-gcc -v
```
Done.
끝.
이제 어떤 파일이든 RV32I에 맞게 컴파일할 수 있다. 

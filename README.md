# benchmark-dhrystone

"DHRYSTONE" Benchmark Program by  Reinhold P. Weicker

# RISC-V RV32I Bare-metal environment implementation

## Repository's purpose

- This repository is for implementing **Dhrystone 2.1** on ***Bare-metal RISC-V RV32I Processors***.
- The main contents will be written in README.md.
- The files that repository provides will be the 'ready to takeoff' state Dhrystone 2.1 for any RV32I bare-metal processor  
  (should support UART TX, MMIO.)
- For performance evaluation, your processor needs **Zicsr** extension with supporting `mcycle(h)`, `minstret(h)` CSR.

## Target Processor

Target processor is [basic_RV32s](https://github.com/RISC-KC/basic_rv32s)' **46F5SP_MMIO_SoC**, which is based on **RV32I46F_5SP** core design.   
(RV32I_Zicsr with 46 Instructions support, 5-Stage Pipelined In-order processor)   
<sup>RV32I except fence, fence.tso, pause = 39 instructions for RV32I, 6 instructions for Zicsr, 1 instruction from privileged architecture: mret </sup>   
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

3. Configure the toolchain build.   
   여기서부터가 중요하다. 현재 있는 툴체인 폴더에서, configure를 진행해준다.

```bash
cd ~/riscv-gnu-toolchain
./configure --prefix=$HOME/riscv32i-elf --target=riscv32-unknown-elf --with-arch=rv32i --with-abi=ilp32
```

`riscv32i-elf` is the directory where toolchain is built. You can change this directory if needed.  
Official manual does with the `/opt/riscv` directory.  

여기서 riscv32i-elf는 툴체인이 빌드 될 디렉토리다. 원하는 폴더명이나 경로로 바꿔도 좋다.  
매뉴얼에서는(공식 깃헙 페이지) `/opt/riscv`로 한다.

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

## Make Dhrystone 2.1.

Our repository provides:

- Dhrystone 2.1 Source codes (From SiFive)
  - dhry.h
  - dhry_1.c
  - dhry_2.c
- Files for compiling Dhrystone 2.1
  - crt0.s
  - linker.ld
  - Makefile
  - mini_libc.c
  - strcmp.S
  - syscalls.c
  - sys/
    - times.h
- Utility program
  - bin2mem.py

There are no modifications for the dhrystone source codes.   
Only the files for compiling is added and these are all we need to make Dhrystone 2.1.

### How to use

```bash
git clone https://github.com/T410N/dhrystone-rv32i-baremetal.git
cd dhrystone-rv32i-baremetal
make clean
make
```

And if you want to convert the output `dhrystone.bin` to `.mem`, use bin2mem.py.

```bash
./bin2mem.py dhrystone.bin dhrystone.mem
```

## Dhrystone 2.1 results

**Notes**
SiFive provided version of Dhrystone 2.1 forces benchmark to last at least 2 seconds.  
If the benchmark is done below the time limit, the benchmark will return the following message.  

> Measured time too small to obtain meaningful results. Please increase number of runs.

For 50MHz, we've benchmarked with 300,000 iterations, and also forcefully ignored the time limit and done with the 2,000 iterations too.
Result is same as following, and if you did things correctly, these are the screen that you should receive.  
<img width="611" height="1030" alt="Dhrystone_300k_RV32I" src="https://github.com/user-attachments/assets/815c951d-7a04-4a60-8514-7ccc9c1444c9" />
<img width="611" height="1030" alt="Dhrystone_2k_RV32I" src="https://github.com/user-attachments/assets/1a5f7c47-ce29-48d7-a09f-8050985737df" />

If you are receiving results like this, you should check the Tera Term's settings > Terminal > line break(word wrap... etc) and make sure it's AUTO. :
<img width="611" height="1030" alt="word_wrap_dhrystone" src="https://github.com/user-attachments/assets/32daed60-32ac-45e2-9382-7786c58cf320" />

#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 3:
        print("usage: bin2mem.py <input.bin> <output.mem> [--words N] [--pad N]")
        print("  --words N : write at most N 32-bit words")
        print("  --pad N   : write exactly N 32-bit words (pads with zeros if needed)")
        return 2
    inp = sys.argv[1]
    out = sys.argv[2]

    max_words = None
    pad_words = None
    if "--words" in sys.argv:
        i = sys.argv.index("--words")
        max_words = int(sys.argv[i+1])
    if "--pad" in sys.argv:
        i = sys.argv.index("--pad")
        pad_words = int(sys.argv[i+1])

    data = open(inp, "rb").read()
    # pad to 4 bytes
    if len(data) % 4 != 0:
        data += b"\x00" * (4 - (len(data) % 4))

    words = []
    for i in range(0, len(data), 4):
        w = int.from_bytes(data[i:i+4], byteorder="little", signed=False)
        words.append(w)

    if max_words is not None:
        words = words[:max_words]

    if pad_words is not None:
        if len(words) < pad_words:
            words += [0] * (pad_words - len(words))
        else:
            words = words[:pad_words]

    with open(out, "w", newline="\n") as f:
        for w in words:
            f.write(f"{w:08x}\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

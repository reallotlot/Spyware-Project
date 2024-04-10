
rule pe_file {
    condition:
        uint16(0) == 0x5a4d
}


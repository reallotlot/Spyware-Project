rule racism{
    strings:
        $strg1 = {}
        $strg2 = ""
    condition:
        any of them
}

rule spyware{
    strings:
        $icmp = "ICMP"
        $shutil = "shutil.move"
    condition:
        any of them
}

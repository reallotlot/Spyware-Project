rule racism{
    strings:
        $strg1 = "hate"
        $strg2 = "jews"
    condition:
        all of them
}

rule spyware{
    strings:
        $icmp = "ICMP"
        $shutil = "shutil.move"
    condition:
        any of them
}

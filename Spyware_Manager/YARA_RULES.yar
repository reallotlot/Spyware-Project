rule racism{

    strings:
        $nword = "nig" nocase

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


rule keylogger {

    strings:
        $hiding = "stealth"

    condition:
        any of them
}
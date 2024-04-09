rule detect_common_spyware {
    meta:
        description = "Detects common spyware based on characteristics"
        author = "Lotan Yahav"
        reference = "Based on known characteristics of spyware"
    strings:
        $string1 = "http://" ascii wide
        $string2 = "https://" ascii wide
        $string3 = "User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)" wide
        $string4 = "system32" wide
        $string5 = "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" wide
        $string6 = "Spyware" wide
        $string7 = "Keylogger" wide
    condition:
        any of ($string*) or all of ($string*)
}

rule eicar_test_rule {

    strings:
        $eicar_test_file = "X5O!P%@AP[4PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H"
    condition:
        any of them

}
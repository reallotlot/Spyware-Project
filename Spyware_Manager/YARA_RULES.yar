rule DOSexe {

    strings:
        $mz  = { 4D 5A } 

    condition:
        any of them
}
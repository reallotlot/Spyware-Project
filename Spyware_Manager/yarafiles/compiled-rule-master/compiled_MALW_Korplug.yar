YARA�          �       �   6         6      �  �               ?  E	      E  �
          �
         �         �      �  2                                     ��������                          	      c  ��������   �      �             ��������������������������������������������         !                     K      R                     _      d                     o      t                    k     s                    K      �                    �     �                                          �      �ں�ں��           �   ��������           �   �     �ں�ں��    
      �   ��������           �   �     �ں�ں��          �   ��������           �   �     �ں�ں��            ��������             �     �ں�ں��            ��������             �     �ں�ں��          )  ��������           %  �     �ں�ں��          ;  ��������           7  �     �ں�ں��          P  ��������           L  	     �ں�ں��   #      z  ��������           t  	  	   �ں�ں��         �  ��������           �  	  
   �ں�ں��         �  ��������           �  	     �ں�ں��   #      z  ��������           �  	     �ں�ں��         �  ��������           �  	     �ں�ں��         �  ��������           �  	     �ں�ں��   #      z  ��������             	     �ں�ں��         �  ��������             	     �ں�ں��            ��������                 ��������������������default Korplug_FAST description Rule to detect Korplug/PlugX FAST variant author Florian Roth date 2015-08-20 hash c437465db42268332543fbf6fd6a560ca010f19e0fd56562fb83fb704824b371 $x1 %s\rundll32.exe "%s", ShadowPlay $a1 ShadowPlay $s1 %s\rundll32.exe "%s", $s2 nvdisps.dll $s3 %snvdisps.dll $s4 \winhlp32.exe $s5 nvdisps_user.dat $s6 %snvdisps_user.dat Korplug maltype Korplug Backdoor https://github.com/reed1713 reference http://www.symantec.com/connect/blogs/new-sample-backdoorkorplug-signed-stolen-certificate IOC looks for events associated with the KORPLUG Backdoor linked to the recent operation greedy wonk activity. $type Microsoft-Windows-Security-Auditing $eventid 4688 $data ProgramData\RasTls\RasTls.exe $type1 $eventid1 $data1 ProgramData\RasTls\rundll32.exe $type2 $eventid2 $data2 ProgramData\RasTls\svchost.exe �       ? �@MZd/   %A � f/�          1X      8   /H   ?B   p      �      �           P     �          1H   ?B   p      �      �           P     �                  n      BB   �     �     0     h     �     �          H     �                 �                                                                                                                                                       &                                                          5              7  4  4           3*  .6      /(  9  30  /:          /B  94                                              T
                                                  S2      b      ]                  g          m  i  b.  p  q  `,          u          t  e>  t$  o&  e@          u"                                          w8      v<                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ������������������������          8   ������������������������          p   ����������������
                 �   ������������������������	          �   ������������������������            ������������������������
          P  ������������������������	          �  ����������������
   �             �  ������������������������
          �  ������������������������          0  ������������������������          h  ����������������
   @  
          �  ����������������
   h            �  ����������������
   P               ����������������
   �  
          H  ����������������
   �            �  ����������������
   �                                                      (                          (      @      H      `      h      0                
       
      
      
         h      P      X   
   (   
   0   
   8   
   @      �      �      �   
   P   
   X   
   `   
   h      �      �      �   
   x   
   �   
   �   
   �           �         
   �   
   �   
   �   
   �      H     0     8  
   �   
   �   
   �   
   �      �     h     p  
   �   
   �   
      
        �     �     �  
     
      
   (  
   0     #      2      D      M      V      _      h      q      �      �      �      �      �      �      8      @      P      H      X      �      �      �      �      �      �      �      �      �     �     �  
   @  
   H  
   P  
   X     (            
   h  
   p  
   x  
   �     `     H     P  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �          �     �  
     
     
     
         @     (     0  
   0  
   8  
   @  
   H     x     `     h  
   X  
   `  
   h  
   p     �     �     �  
   �  
   �  
   �  
   �     �      �      �      �                     !     *  
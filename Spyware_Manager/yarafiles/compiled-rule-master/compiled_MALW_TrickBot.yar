YARA�          �       �   �         �        �         �      �  z      D  �          �         �         �      �  V                                                                            �           @                          �          �      h                    �     �     �      H             ��������������������������������������������   &      -                     D      P                    &      -                     D                         &      -                     D                         &      -                     D      �                	      �ں�ں��          ~   ��������           p   	     �ں�ں��          �   ��������           �   	     �ں�ں��          �   ��������           �   	     �ں�ں��    
      �   ��������           �   	     �ں�ں��          �   ��������           �   	     �ں�ں��   	      M  ��������           ;  	     �ں�ں��   	      i  ��������           W  	     �ں�ں��         �  ��������           s  	     �ں�ں��         �  ��������           �  	  	   �ں�ں��         �  ��������           �  	  
   �ں�ں��         �  ��������           �  	     �ں�ں��   
      ]  ��������           N  	     �ں�ں��         w  ��������           h  	     �ں�ں��         �  ��������           �  	     �ں�ں��         �  ��������           �  	     �ں�ں��         %  ��������             	     �ں�ں��         @  ��������           2  	     �ں�ں��         V  ��������           H  	     �ں�ں��         i  ��������           [  	     �ں�ں��         {  ��������           m  	     �ں�ں��         �  ��������           �  	     �ں�ں��         �  ��������           �  	     �ں�ں��         �  ��������           �      ��������������������default MALW_trickbot_bankBot Trojan  author Marc Salinas @Bondey_m description Detects Trickbot Banking Trojan $str_trick_01 moduleconfig $str_trick_02 Start $str_trick_03 Control $str_trick_04 FreeBuffer $str_trick_05 Release MALW_systeminfo_trickbot_module Trojan  Detects systeminfo module from Trickbot Trojan $str_systeminf_01 <program> $str_systeminf_02 <service> $str_systeminf_03 </systeminfo> $str_systeminf_04 GetSystemInfo.pdb $str_systeminf_05 </autostart> $str_systeminf_06 </moduleconfig> MALW_dllinject_trickbot_module Trojan   Detects dllinject module from Trickbot Trojan $str_dllinj_01 user_pref( $str_dllinj_02 <ignore_mask> $str_dllinj_03 <require_header> $str_dllinj_04 </dinj> MALW_mailsercher_trickbot_module Trojan   Detects mailsearcher module from Trickbot Trojan $str_mails_01 mailsearcher $str_mails_02 handler $str_mails_03 conf $str_mails_04 ctl $str_mails_05 SetConf $str_mails_06 file $str_mails_07 needinfo $str_mails_08 mailconf J       BB          8      p      �      �                   S      BB        P     �     �     �     0                 A      BB   h     �     �                      e      BB   H     �     �     �     (     `     �     �                 �                                                                              P               &                                                                                          
       .           
      0H  /D                  =   
       X           f  D          
                           D�      C,          T                                                              d  b$  f  g      i  f  j   g&  m  n.  o
  fP  j:  p  eB  t  f2  p<  u"  q*  bL  s4  t8  o^  m\  m  sf  fJ  o`  fR  p  uZ  hT  bN  pX  sh  eb  bV  jl  vr  oj  u  bt  jv  ex  nd  `>  f(  e6  g0  rF  t@  o|  z�  j~  s�  v�      t�  g�      p�      p�  o�          m�      u�          s�                  v�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         	                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ������������������������          8   ������������������������          p   ������������������������          �   ������������������������          �   ������������������������            ������������������������          P  ������������������������          �  ������������������������          �  ������������������������          �  ������������������������          0  ������������������������          h  ������������������������          �  ������������������������          �  ������������������������            ������������������������          H  ������������������������          �  ������������������������          �  ������������������������          �  ������������������������          (  ������������������������          `  ������������������������          �  ������������������������          �  ����������������
   X                                                      (                          (      0                
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
   �                        '      0      8      @      P      H      X      @      H      `      h      H     0     8  
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
   0     �     �     �  
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
   �     V      _      h      q      z      �      h      p      �      x      �      �      �      �      �      �     �     �  
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
   H     �      �      �      �      �      �      �      �      �      �      �      �      �      x     `     h  
   X  
   `  
   h  
   p     �     �     �  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �                  
   �  
   �  
   �  
   �     X     @     H  
   �  
      
     
        �     x     �  
      
   (  
   0  
   8     �     �     �  
   H  
   P  
   X  
   `           �     �  
   p  
   x  
   �  
   �     �      �      �                           )  
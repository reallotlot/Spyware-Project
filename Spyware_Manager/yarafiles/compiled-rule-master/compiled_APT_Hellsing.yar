YARA�          �       P  �         �      �  �         �      �	  ]      �                      ,        '<      �  �I                            %         ��������                                �  ��������   �      �              
      M  ��������         X                    j  ��������   �     �                    �  ��������         �
                    �  ��������   �     @             ��������������������������������������������   '      .                     I      N                     Y      e                     �      �                    '      .                     I      N                     Y      �                    �      �                    '      .                     I      N                     Y      d                    �      �                    '      .                     I      N                     Y      |                    �      �                    '      .                     I      N                     Y      �                    �      �                    '      .                     I      N                     Y      �                    �      �                 	�                           ��������           �   	     �ں�ں��            ��������             	     �ں�ں��          &  ��������           "  	     �ں�ں��          9  ��������           5  	     �ں�ں��    
      Z  ��������           V  	     �ں�ں��          h  ��������           e  	     �ں�ں��          }  ��������           z       �ں�ں��          �  ��������           �       �ں�ں��          �  ��������           �    	   �ں�ں��          �  ��������           �    
   �ں�ں��          �  ��������           �       �ں�ں��          !  ��������                  �ں�ں��          G  ��������           ;       �ں�ں��          n  ��������           b  	     �ں�ں��          �  ��������           �  	     �ں�ں��          �  ��������           �  	�                         ��������           �   	     �ں�ں��   8      �  ��������           �  	     �ں�ں��         ,  ��������                  �ں�ں��         C  ��������           "  	     �ں�ں��   (      X  ��������           T  	     �ں�ں��   |      �  ��������           �  	     �ں�ں��            ��������             	     �ں�ں��   ,      +  ��������           '  	     �ں�ں��   |      \  ��������           X       �ں�ں��   '      �  ��������           �       �ں�ں��         
  ��������             	     �ں�ں��         -  ��������           (  K    �ں�ں��         D  ��������           ?  	�                         ��������           �   	     �ں�ں��   &      �  ��������             	     �ں�ں��   "      �  ��������           "  	      �ں�ں��         �  ��������           �  	  !   �ں�ں��         �  ��������           T  	  "   �ں�ں��   1        ��������           �    #   �ں�ں��         M  ��������             	�  $                       ��������           �   	  %   �ں�ں��   	      �  ��������             	  &   �ں�ں��         �  ��������           "  	  '   �ں�ں��         �  ��������           �  	  (   �ں�ں��         �  ��������           T  	  )   �ں�ں��         �  ��������           �  	  *   �ں�ں��         �  ��������             	  +   �ں�ں��           ��������           '  	  ,   �ں�ں��           ��������           X  	  -   �ں�ں��         -  ��������           �  	  .   �ں�ں��         =  ��������             	  /   �ں�ں��         I  ��������           (  	  0   �ں�ں��         g  ��������           ?  	�  1                       ��������           �   	  2   �ں�ں��         �  ��������             	  3   �ں�ں��         �  ��������           "  	  4   �ں�ں��   O      �  ��������           �  	  5   �ں�ں��         /  ��������           T  	  6   �ں�ں��   (      L  ��������           �  	  7   �ں�ں��         u  ��������             	�  8                       ��������           �     9   �ں�ں��         �  ��������               :   �ں�ں��         �  ��������           "  	  ;   �ں�ں��   $      �  ��������           �  	  <   �ں�ں��   ;       	  ��������           T    =   �ں�ں��         \	  ��������           �  	  >   �ں�ں��   $      b	  ��������                 ��������������������default pe apt_hellsing_implantstrings Author Costin Raiu, Kaspersky Lab Date 2015-04-07 Description detection for Hellsing implants Reference http://securelist.com/analysis/publications/69567/the-chronicles-of-the-hellsing-apt-the-empire-strikes-back $mz MZ $a1 the file uploaded failed ! $a2 ping 127.0.0.1 $b1 the file downloaded failed ! $b2 common.asp $c xweber_server.exe $d action= $debugpath1 d:\Hellsing\release\msger\ $debugpath2 d:\hellsing\sys\xrat\ $debugpath3 D:\Hellsing\release\exe\ $debugpath4 d:\hellsing\sys\xkat\ $debugpath5 e:\Hellsing\release\clare $debugpath6 e:\Hellsing\release\irene\ $debugpath7 d:\hellsing\sys\irene\ $e msger_server.dll $f ServiceMain apt_hellsing_installer detection for Hellsing xweber/msger installers $cmd cmd.exe /c ping 127.0.0.1 -n 5&cmd.exe /c del /a /f "%s" xweber_install_uac.exe system32\cmd.exe $a4 S11SWFOrVwR9UlpWRVZZWAR0U1aoBHFTUl2oU1Y= $a5 S11SWFOrVwR9dnFTUgRUVlNHWVdXBFpTVgRdUlpWRVZZWARdUqhZVlpFR1kEUVNSXahTVgRaU1YEUVNSXahTVl1SWwRZValdVFFZUqgQBF1SWlZFVllYBFRTVqg= $a6 7dqm2ODf5N/Y2N/m6+br3dnZpunl44g= $a7 vd/m7OXd2ai/5u7a59rr7Ki45drcqMPl5t/c5dqIZw== $a8 vd/m7OXd2ai/usPl5qjY2uXp69nZqO7l2qjf5u7a59rr7Kjf5tzr2u7n6euo4+Xm39zl2qju5dqo4+Xm39zl2t/m7ajr19vf2OPr39rj5eaZmqbs5OSI Njl2tyI $a9 C:\Windows\System32\sysprep\sysprep.exe $a10 %SystemRoot%\system32\cmd.exe $a11 msger_install.dll $a12  ex.dll  apt_hellsing_proxytool detection for Hellsing proxy testing tool PROXY_INFO: automatic proxy url => %s  PROXY_INFO: connection type => %d  $a3 PROXY_INFO: proxy server => %s  PROXY_INFO: bypass list => %s  InternetQueryOption failed with GetLastError() %d D:\Hellsing\release\exe\exe\ apt_hellsing_xkat detection for Hellsing xKat tool \Dbgv.sys XKAT_BIN release sys file error. driver_load error.  driver_create error. delete file:%s error. delete file:%s ok. kill pid:%d error. kill pid:%d ok. -pid-delete kill and delete pid:%d error. kill and delete pid:%d ok. apt_hellsing_msgertype2 detection for Hellsing msger type 2 implants %s\system\%d.txt _msger http://%s/lib/common.asp?action=user_login&uid=%s&lan=%s&host=%s&os=%s&proxy=%s http://%s/data/%s.1000001000 /lib/common.asp?action=user_upload&file= %02X-%02X-%02X-%02X-%02X-%02X apt_hellsing_irene detection for Hellsing msger irene installer \Drivers\usbmgr.tmp \Drivers\usbmgr.sys common_loadDriver CreateFile error!  common_loadDriver StartService error && GetLastError():%d!  irene aPLib v0.43 - the smaller the better )            ?        /#   BB   8      p           1#   BB   �      �           1         /      P  1Q   ?B   �     �     �     0     h     �     �          1-        /      H  /   %A � f        �      ?    �  /�      �  /u   ?B   �     (     `     �     �          @     x     �     �                /   %A � f       s      ?    X  /H   ?B   �     �           8     p     �          /   %A�� f       �      ?    �  /~   ?B        P     �     �     �     0	     h	     �	     �	     
     H
     �
          /   %A�� f       s      ?    �
  /H   ?B   �
     (     `     �     �               /   %A � f       s      ?    @  /H   ?B   x     �     �           X     �          /   %A � f       �                                                                    L               :              �                  �              .       .              &N  )      *>          .   6  0  1  2  /&     0B  &X      8$       
  ;
  2�  3 1�   :      .  6n   .   
  E6  F(   
  5 BT   
      L     NF  ;t  P  0 ;�  S  T  E^  ;�  ;�  1     ;
 6L     ]    .  ;4 `     )F c4  YZ  e8  f.  g  h,      j0  E> fD  m  n:  fH  p  n*     q@  bJ  f�  7T w  j mh  n~  sr  f�  e�  [ U6 f�       0           
  b0 ZJ p�  t j& /`    p�         y�  e8 cD  0  ;z s2 VX ]b          �       8  4� jP  6  � ]f  4      ]j         ]n  0          &�     vR                 &�     s\     s^     4� 8�     � o~  �  st     &�     3�         T�                 /�     *�  ,      o� s�  $   �         ,�                 ,   >     2�     :� 8�  4  &�  $                        8              m�                         h� / e� `� I� `� I� >� I�    I� /            `�          H      h� c� t�         `�                     e�                 i�     i� X i�     i� `�             w�         `                 f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Q                                                                                                                                                                                                                                                                                       W   U       N       L   P               G   B   D       @   ?   S   K   >   8   7       .           O       -   ,   *   %   1         2         9       <   :   ;   V   I                                          (           0   T          +   '                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ������������������������          8   ������������������������          p   ������������������������	          �   ����������������
   (             �   ������������������������            ������������������������          P  ������������������������          �  ������������������������          �  ������������������������          �  ������������������������          �  ������������������������          �  ����������������
   �            �  ����������������
   h            �  ����������������
   @            �  ����������������
               �  ����������������
   �            �  ����������������
   �            �  ����������������
   0            �  ����������������
               0  ����������������
   �            0  ����������������
   X            0  ����������������
   �            0  ����������������
   �            h  ������������������������          h  ������������������������          h  ������������������������          h  ������������������������          �  ����������������
   �            �  ����������������
   �            �  ����������������
   �            �  ����������������
               �  ����������������
   �            �  ����������������
                �  ����������������
   H            �  ����������������
   p              ������������������������          H  ������������������������          �  ����������������
                 �  ����������������
   P             �  ����������������
   �             (  ������������������������          `  ������������������������          �  ������������������������          �  ������������������������            ������������������������          @  ������������������������*          x  ����������������
   @  $          �  ����������������
   0  (          �  ����������������
   x               ������������������������          X  ����������������
   �            �  ������������������������          �  ����������������
   �               ����������������
                8  ����������������
   H            p  ������������������������.          �  ����������������
                �  ����������������
   �            �  ����������������
   P            �  ����������������
   (            �  ����������������
   �              ������������������������          P  ������������������������          �  ������������������������          �  ������������������������          �  ����������������
    
            0	  ������������������������          h	  ����������������
   P
            �	  ������������������������
          �	  ����������������
   �
  
          
  ������������������������          H
  ����������������
   �
            �
  ����������������
               �
  ����������������
   `	            �
  ������������������������          (  ������������������������          `  ������������������������          �  ����������������
   �            �  ������������������������            ������������������������          @  ����������������
   h            x  ������������������������          �  ����������������
   �            �  ������������������������             ������������������������8          X  ������������������������          �  ������������������������          ?                                                (                          (      @      H      `      h      0                
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
   0  
   @  
   H  
   P  
   X  
   h  
   p  
   x  
   �  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
     
     
     
      
   0  
   8  
   @  
   H     (            
   X  
   `  
   h  
   p  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �     `     H     P  
   �  
      
     
     
      
   (  
   0  
   8  
   H  
   P  
   X  
   `  
   p  
   x  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
      
     
     
      
   (     �     �     �  
   8  
   @  
   H  
   P  
   `  
   h  
   p  
   x  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
   �          �     �  
   �  
   �  
   �  
   �  
      
     
     
     
   (  
   0  
   8  
   @  
   P  
   X  
   `  
   h     @     (     0  
   x  
   �  
   �  
   �     x     `     h  
   �  
   �  
   �  
   �           &      /      I      R      j      y      �      �      �      �      �      �      �      �      �      8      @      P      H      X      �      �      �      �      �      �      �      �      �     �     �  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
      
                     
     
      
   (  
   0     X     @     H  
   @  
   H  
   P  
   X     �     x     �  
   h  
   p  
   x  
   �     �     �     �  
   �  
   �  
   �  
   �           �     �  
   �  
   �  
   �  
   �     8           (  
   �  
   �  
   �  
   �     p     X     `  
     
     
     
         �     �     �  
   0  
   8  
   @  
   H     �     �     �  
   X  
   `  
   h  
   p                  
   �  
   �  
   �  
   �     P     8     @  
   �  
   �  
   �  
   �          &     8     A     J     S     \     e     n     w     �     �     �     h      p      �      x      �                       (     @     H     `     h     �     p     x  
   �  
   �  
   �  
   �     �     �     �  
   �  
      
     
        �     �     �  
      
   (  
   0  
   8     0             
   H  
   P  
   X  
   `     h     P     X  
   p  
   x  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �  
   �  
   �  
   �  
    	  
   	  
   	  
    	  
   (	  
   8	  
   @	  
   H	  
   P	     �     �     �     �     �     �          �      �      �      �      �      �     �     �     �     �     �     �     �          �        
   `	  
   h	  
   p	  
   x	     H     0     8  
   �	  
   �	  
   �	  
   �	     �     h     p  
   �	  
   �	  
   �	  
   �	     �     �     �  
   �	  
   �	  
   �	  
   �	     �     �     �  
    
  
   
  
   
  
   
     (	     	     	  
   (
  
   0
  
   8
  
   @
     `	     H	     P	  
   P
  
   X
  
   `
  
   h
     �	     �	     �	  
   x
  
   �
  
   �
  
   �
     �	     �	     �	  
   �
  
   �
  
   �
  
   �
     
     �	     �	  
   �
  
   �
  
   �
  
   �
     @
     (
     0
  
   �
  
   �
  
      
        x
     `
     h
  
     
      
   (  
   0     �
     �
     �
  
   @  
   H  
   P  
   X     :     L     U     ^     g     p     y     �     �     �     �     �     �     �      �      �      �      �                       (     @     H     `     h     �
     �
     �
  
   h  
   p  
   x  
   �                  
   �  
   �  
   �  
   �     X     @     H  
   �  
   �  
   �  
   �     �     x     �  
   �  
   �  
   �  
   �     �     �     �  
     
     
     
               �     �  
   0  
   8  
   @  
   H     8           (  
   X  
   `  
   h  
   p     �     �     �                    "     �                           �     �     �     �     �     �     �     �     p     X     `  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �                  
   �  
      
     
        P     8     @  
      
   (  
   0  
   8     �     p     x  
   H  
   P  
   X  
   `     �     �     �  
   p  
   x  
   �  
   �     V     h     q     z     �     �     �  
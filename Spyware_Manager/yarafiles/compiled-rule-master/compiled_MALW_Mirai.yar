YARA�          �       �  F         f      �           .      
  G&      m  �+          �+         �3         �;      	  �D                                        #                                   }     �     �      �                     B     Q           �                    �                �                    �     �     @     �                    d     t     `     `                    &     6     �     @                    �     �     �                          �     �     `     8                    =     E      	     �                    �     �     �	     
                    /	     :	     �
     �
                    �	     �	     `     (             ��������������������������������������������   )      5                     e      l                     �      �                     �      �                     �      �                     �      �                     e     j                   )      �                    e      l                     �      �                     �      �                     �     �                    �     �                    �      �                     �      �                     e     j                   )      W                    e      l                     �      �                     �      �                     �     {                    �     �                    �      �                     �      �                     e     j                   )      
                    e      l                     �      �                     �      �                     �     -                    �     N                    �      �                     �      �                     e     j                   )      �                    e      l                     �      �                     �      �                     �     �                    �     
                    �      �                     �      �                     e     j                   )      z                    e      l                     �      �                     �      �                     �     �                    �     �                    �      �                     �      �                     e     j                   )      <                    e      l                     �      �                     �      �                     �     a                    �     �                    �      �                     �      �                     e     j                   )      �                    e      �                    �                          �      �                     �                         �     >                   )      �                    e      �                    �                          �      �                     �     �                    �     �                   )      K                    e      �                    �                          �      �                     �     [                    �     |                   )      �                    e      �                    �                          �      �                     �     �                    �     �                   )      @	                    e      �                    �                          �      �                     �     Q	                    �     r	                   )      �	                    e      �                    �                          �      �                     �     �	                    �     �	                	      �ں�ں��          �  ��������           �  	     �ں�ں��    @      �  ��������           �  	     �ں�ں��    @      %  ��������             	     �ں�ں��          o  ��������           f  	     �ں�ں��         �  ��������           �  	     �ں�ں��   @      �  ��������           �  	     �ں�ں��   @      %  ��������             	     �ں�ں��         o  ��������           f  	     �ں�ں��         �  ��������           �  	  	   �ں�ں��   @      �  ��������           �  	  
   �ں�ں��   @      %  ��������             	     �ں�ں��         o  ��������           f  	     �ں�ں��         �  ��������           �  	     �ں�ں��   @      �  ��������           �  	     �ں�ں��   @      %  ��������             	     �ں�ں��         o  ��������           f  	     �ں�ں��         �  ��������           �  	     �ں�ں��   @      �  ��������           �  	     �ں�ں��   @      %  ��������             	     �ں�ں��         o  ��������           f  	     �ں�ں��         �  ��������           �  	     �ں�ں��   @      �  ��������           �  	     �ں�ں��   @      %  ��������             	     �ں�ں��         o  ��������           f  	     �ں�ں��         �  ��������           �  	     �ں�ں��   @      �  ��������           �  	     �ں�ں��   @      %  ��������             	     �ں�ں��         o  ��������           f  	     �ں�ں��         m  ��������           g  	     �ں�ں��         �  ��������           {  	     �ں�ں��         �  ��������           �  	     �ں�ں��         �  ��������           �  	      �ں�ں��         �  ��������           �  	  !   �ں�ں��         m  ��������           g  	  "   �ں�ں��         �  ��������           {  	  #   �ں�ں��         �  ��������           %  	  $   �ں�ں��         -  ��������           )  	  %   �ں�ں��         �  ��������           5  	  &   �ں�ں��         �  ��������           9  	  '   �ں�ں��	         m  ��������           g  	  (   �ں�ں��	         �  ��������           {  	  )   �ں�ں��	         �  ��������           %  	  *   �ں�ں��	         -  ��������           )  	  +   �ں�ں��	         �  ��������           5  	  ,   �ں�ں��	         �  ��������           9  	  -   �ں�ں��	   	      �  ��������           �  	  .   �ں�ں��
         	  ��������           %  	  /   �ں�ں��
         #	  ��������           )  	  0   �ں�ں��
         (	  ��������           5  	  1   �ں�ں��         �	  ��������           %  	  2   �ں�ں��   	      �	  ��������           )  	  3   �ں�ں��         m  ��������           g  	  4   �ں�ں��         �  ��������           {  	  5   �ں�ں��         �  ��������           %  	  6   �ں�ں��         -  ��������           )  	  7   �ں�ں��         �  ��������           5  	  8   �ں�ں��         �  ��������           9  	  9   �ں�ں��   	      �  ��������           �      ��������������������default hash pe Mirai_Generic_Arch MALW  description Mirai Botnet TR-069 Worm - Generic Architecture author Felipe Molina / @felmoltor date 2016-12-04 version 1.0 ref1 http://www.theregister.co.uk/2016/11/28/router_flaw_exploited_in_massive_attack/ ref2 https://isc.sans.edu/forums/diary/Port+7547+SOAP+Remote+Code+Execution+Attack+Against+DSL+Modems/21759 ref3 https://krebsonsecurity.com/2016/11/new-mirai-worm-knocks-900k-germans-offline/ $miname Myname--is: $iptables1 busybox iptables -A INPUT -p tcp --destination-port 7547 -j DROP $iptables2 busybox iptables -A INPUT -p tcp --destination-port 5555 -j DROP $procnet /proc/net/tcp Mirai_MIPS_LSB MALW  Mirai Botnet TR-069 Worm - MIPS LSB MD5 bf650d39eb603d92973052ca80a4fdda SHA1 03ecd3b49aa19589599c64e4e7a51206a592b4ef sha1 ii (       03ecd3b49aa19589599c64e4e7a51206a592b4ef Mirai_MIPS_MSB MALW  Mirai Botnet TR-069 Worm - MIPS MSB 0eb51d584712485300ad8e8126773941 18bce2f0107b5fab1b0b7c453e2a6b6505200cbd (       18bce2f0107b5fab1b0b7c453e2a6b6505200cbd Mirai_ARM_LSB MALW  Mirai Botnet TR-069 Worm - ARM LSB eba670256b816e2d11f107f629d08494 8a25dee4ea7d61692b2b95bd047269543aaf0c81 (       8a25dee4ea7d61692b2b95bd047269543aaf0c81 Mirai_Renesas_SH MALW  Mirai Botnet TR-069 Worm - Renesas SH LSB 863dcf82883c885b0686dce747dcf502 bdc86295fad70480f0c6edcc37981e3cf11d838c (       bdc86295fad70480f0c6edcc37981e3cf11d838c Mirai_PPC_Cisco MALW  Mirai Botnet TR-069 Worm - PowerPC or Cisco 4500 dbd92b08cbff8455ff76c453ff704dc6 6933d555a008a07b859a55cddb704441915adf68 (       6933d555a008a07b859a55cddb704441915adf68 Mirai_SPARC_MSB MALW  Mirai Botnet TR-069 Worm - SPARC MSB 05891dbabc42a36f33c30535f0931555 3d770480b6410cba39e19b3a2ff3bec774cabe47 (       3d770480b6410cba39e19b3a2ff3bec774cabe47 Mirai_1 MALW  Mirai Variant 1 Joan Soriano / @joanbtl 2017-04-16 655c3cf460489a7d032c37cd5b84a3a8 4dd3803956bc31c8c7c504734bddec47a1b57d58 $dir1 /dev/watchdog $dir2 /dev/misc/watchdog $pass1 PMMV $pass2 FGDCWNV $pass3 OMVJGP Mirai_2 MALW  Mirai Variant 2 0e5bda9d39b03ce79ab8d421b90c0067 96f42a9fad2923281d21eca7ecdd3161d2b61655 $s1 $s2 ZOJFKRA $s3 $s4 Mirai_3 MALW  Mirai Variant 3 bb22b1c921ad8fa358d985ff1e51a5b8 432ef83c7692e304c621924bc961d95c4aea0c00 $ssl ssl3_ctrl Mirai_4 MALW  Mirai Variant 4 f832ef7a4fcd252463adddfa14db43fb 4455d237aadaf28aafce57097144beac92e55110 210765 qllw ;;;;;; Mirai_Dwnl MALW  Mirai Downloader 85784b54dee0b7c16c57e3a3a01db7e6 6f6c625ef730beefbc23c7f362af329426607dee GET /mirai/ dvrHelper Mirai_5 MALW  Mirai Variant 5 7e17c34cddcaeb6755c457b99a8dfe32 b63271672d6a044704836d542d92b98e2316ad24 )      )      L              /      8   /      p   /      �           {         �   /        /      P  /      �  //            	  ? %          �       {         �  /      �  /      0  /      h  //            	  ? %        �  �       {         �  /      �  /        /      H  //            	  ? %        w  �       {         �  /      �  /      �  /      (  //            	  ? %        3  �       {         `  /      �  /      �  /        //            	  ? %        �  �       {         @  /      x  /      �  /      �  //            	  ? %        �  �       ^            /      �  /      �  /         /      X         m         8  /      p  /      �  /      �  /        /      P         }   	      �  /      �  /      �  /      0	  /      h	  /      �	  /      �	  	       <   
      
  /      H
  /      �
  
       ,         �
  /      �
         |         (  /      `  /      �  /      �  /        /      @  /      x         �                                                                                                                                                                            8      .     0         3          2       8  .4          <      <     62  1D              4F      G          <8              5P  H(  P  Q              P$  N&  N*  <X  EH  8^  [
      K@          8~          N>  ;�  e  IV  Gd  Dj      WB      Kh              m  e0  r  m"  t  j6  Wn      w      n.      m<  q,  fL  eT  s:  jJ      `b                      sN                      tR  f�                      xZ  pz  st                  wv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      3   1   0       /       :   7       9   8       6           2   5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ������������������������          8   ������������������������8          p   ������������������������%          �   ������������������������          �   ����������������
                   ����������������
   (   8          P  ����������������
   P   %          �  ����������������
   x             �  ����������������
   �             �  ����������������
   �   8          0  ����������������
   �   %          h  ����������������
               �  ����������������
   @            �  ����������������
   h  8            ����������������
   �  %          H  ����������������
   �            �  ����������������
   �            �  ����������������
     8          �  ����������������
   0  %          (  ����������������
   X            `  ����������������
   �            �  ����������������
   �  8          �  ����������������
   �  %            ����������������
   �            @  ����������������
                x  ����������������
   H  8          �  ����������������
   p  %          �  ����������������
   �               ������������������������          X  ����������������
   `            �  ������������������������          �  ������������������������             ������������������������          8  ����������������
   �            p  ����������������
   (            �  ����������������
   �            �  ������������������������            ����������������
   �            P  ����������������
                �  ����������������
   P            �  ����������������
               �  ����������������
   x            0	  ����������������
   �            h	  ����������������
   �            �	  ����������������
   �            �	  ������������������������          
  ������������������������          H
  ������������������������          �
  ������������������������          �
  ������������������������          �
  ������������������������          (  ����������������
   @            `  ����������������
   �            �  ����������������
   h            �  ����������������
   �              ����������������
   �            @  ����������������
   �            x  ����������������
               :                       
                               (                          (      @      H      `      h      �      �      �      �      �      �      0                
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
   �            +      ;      K      8      @      P      H      X      �      �                       (     @     H     `     h     �     �     �     �     �     �     �     �          �         
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
   0     h      w      �      �      �      �      �      �      h      p      �      x      �                       (     @     H     `     h     �     �     �     �     �     �     �     �                �     �     �  
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
   �     �      �                "     +     7     A     �      �      �      �      �            (     @     H     `     h     �     �     �     �     �     �     �     �                      (     �     �     �  
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
   p     ^     m     }     �     �     �     �     �     �      �      �      �      �      @     H     `     h     �     �     �     �     �     �     �     �                      (     @     H     �     �     �  
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
        �     �     �               !     -     7     �                           `     h     �     �     �     �     �     �     �     �                      (     @     H     `     h     �     x     �  
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
   �     8           (  
   �  
   �  
   �  
   �     T     c     s     �     �     �     �     �     (     0     @     8     H     �     �     �     �     �     �     �     �                      (     @     H     `     h     �     �     p     X     `  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
         �     �     �  
     
     
      
   (                  
   8  
   @  
   H  
   P     �     �     �     �               #     -     X     `     p     h     x     �     �     �     �     �     �                      (     @     H     P     8     @  
   `  
   h  
   p  
   x     �     p     x  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �     0             
      
     
     
        J     Y     i     y     �     �     �     �     �     �     `     h     �     �     �     �     �     �     �     �      	     	     h     P     X  
   (  
   0  
   8  
   @     �     �     �  
   P  
   X  
   `  
   h     �     �     �  
   x  
   �  
   �  
   �          �        
   �  
   �  
   �  
   �     H     0     8  
   �  
   �  
   �  
   �     �     h     p  
   �  
   �  
      
        �     �     �     �     �     �     �     �     �     �     �      	     (	     @	     H	     `	     h	     �	     �	     �	     �	     �	     �	     �     �     �  
     
      
   (  
   0     �     �     �  
   @  
   H  
   P  
   X     (	     	     	  
   h  
   p  
   x  
   �     `	     H	     P	  
   �  
   �  
   �  
   �     �	     �	     �	  
   �  
   �  
   �  
   �     �	     �	     �	  
   �  
   �  
   �  
   �     
     �	     �	  
     
     
     
              $     4     D     T     d     t     �     �           �          �	     �	      
     
      
     (
     @
     H
     `
     h
     �
     �
     @
     (
     0
  
   0  
   8  
   @  
   H     x
     `
     h
  
   X  
   `  
   h  
   p     �
     �
     �
  
   �  
   �  
   �  
   �     �     �     �                0     (     8     �
     �
     �
     �
     �
     �
                      (     @     H     �
     �
     �
  
   �  
   �  
   �  
   �                  
   �  
   �  
   �  
   �     �     �     H     P     `     X     h     `     h     �     �     �     �     �     �     �     �                X     @     H  
   �  
      
     
        �     x     �  
      
   (  
   0  
   8     �     �     �  
   H  
   P  
   X  
   `           �     �  
   p  
   x  
   �  
   �     8           (  
   �  
   �  
   �  
   �     p     X     `  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
    	     �     	          )     9     I     Y  
YARA�          �       �   6         6      x  �         �      �  j      �  �          �         �         �      �  �                                                                            1     A     �      �             ��������������������������������������������         !                     H      O                     �      �                     �      �                          F                    H      O                     �      �                     �      �                 	      �ں�ں��          �   ��������           �   	     �ں�ں��            ��������              	     �ں�ں��            ��������           
  	     �ں�ں��          .  ��������           %  	     �ں�ں��          K  ��������           >  	     �ں�ں��          a  ��������           T  	     �ں�ں��          �  ��������           r  	     �ں�ں��          �  ��������           �  	     �ں�ں��          �  ��������           �  	  	   �ں�ں��          �  ��������           �  	  
   �ں�ں��          �  ��������           �  	     �ں�ں��            ��������             	     �ں�ں��          %  ��������             	     �ں�ں��         f  ��������           ^  	     �ں�ں��         {  ��������           n  	     �ں�ں��         �  ��������           �  	     �ں�ں��         �  ��������           �  	     �ں�ں��         �  ��������           �  	     �ں�ں��         �  ��������           �  	     �ں�ں��   
      �  ��������           �  	     �ں�ں��           ��������              	     �ں�ں��         +  ��������             	     �ں�ں��         T  ��������           I  	     �ں�ں��         x  ��������           l  	     �ں�ں��         �  ��������           �      ��������������������default shimrat RAT  description Detects ShimRat and the ShimRat loader author Yonathan Klijnsma (yonathan.klijnsma@fox-it.com) date 20/11/2015 ref https://blog.fox-it.com/2016/06/15/mofang-a-politically-motivated-information-stealing-adversary/ $dll .dll $dat .dat $headersig QWERTYUIOPLKJHG $datasig MNBVCXZLKJHGFDS $datamarker1 Data$$00 $datamarker2 Data$$01%c%sData $cmdlineformat ping localhost -n 9 /c %s > nul $demoproject_keyword1 Demo $demoproject_keyword2 Win32App $comspec COMSPEC $shim_func1 ShimMain $shim_func2 NotifyShims $shim_func3 GetHookAPIs shimratreporter RAT  Detects ShimRatReporter $IpInfo IP-INFO $NetworkInfo Network-INFO $OsInfo OS-INFO $ProcessInfo Process-INFO $BrowserInfo Browser-INFO $QueryUserInfo QueryUser-INFO $UsersInfo Users-INFO $SoftwareInfo Software-INFO $AddressFormat %02X-%02X-%02X-%02X-%02X-%02X $proxy_str (from environment) = %s $netuserfun NetUserEnum $networkparams GetNetworkParams �              /      8   /      p   /      �   1       �   /        1@      P  /      �  /      �  /      �  1P          /      8   /      0  /      h  /      �          �      BB   �          H     �     �     �     (     `     �     �          @                 �                                                                                                                                           %          &*  )          
      .  /&           ,  ..     .6  %H                              D  1F           "      D  E  1`  .h  H  %�                  N   O  P  Q  R(     T  2�  4�      T2  PB  .�          .     OT  .�  Jb  b"  3�     Jp  f  . g$  &H j  f0  Xn  C�  f8  N�  p  q  f:  i>  t
  f@  s,  jL  eZ  s4  oD  1P p<  F�  J 3B O�  .N        sN  sV  lr  O    jx  tX  sd     f�  nz  b�  V2 u�  ut  uv  T@ o|  I.     WR     m�  p�  O    SV                       j: hF     F      n>         pD                                     uX                                                 m\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
   	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ������������������������          8   ������������������������          p   ������������������������          �   ������������������������          �   ������������������������            ������������������������	          P  ������������������������          �  ������������������������          �  ������������������������          �  ������������������������          0  ������������������������          h  ������������������������          �  ������������������������          �  ������������������������            ������������������������          H  ������������������������          �  ������������������������
          �  ������������������������          �  ����������������
   �  
          (  ������������������������          `  ������������������������	          �  ������������������������          �  ������������������������            ������������������������          @  ������������������������                                                    (                          (      @      H      `      h      0                
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
   �     �     �     �  
   �  
   �  
   �  
   �     �     �     �  
   �  
   �  
   �  
   �     
            )      9      I      X      i      x      �      �      �      �      �      �      �      8      @      P      H      X      �      �      �      �      �      �      �      �           �     �  
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
   �     8           (  
   �  
   �  
   �  
   �     p     X     `  
   �  
   �  
   �  
   �                    #     ,     5     >     G     P     Y     b     k  
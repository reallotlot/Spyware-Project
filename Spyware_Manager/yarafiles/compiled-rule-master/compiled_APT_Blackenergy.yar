YARA�          �       �  V         v
      �           6      �  !      �  �#          �#         �+         �3      x  _9                                     ��������                                H  ��������   �                          �  ��������   @     �                    b  ��������         �              
      �  ��������   �                           ��������   �     @                    �  ��������                              s  ��������   �     �             ��������������������������������������������         %                     C      J                     W      a                     v      {                     �      �                          ^                    C      J                     W      �                    v      �                    �      �                         �                    C      J                     W      �                    v      �                    #  ��������2                 �      )                         �                    C      J                     W      �                    v      �                    �      )                         �                    C      J                     W      �                    v      �                    #  ��������P                    ��������                 +     1                    r     x                    �     �                                                   �                    C      J                     W      �                    v      �                    #  ��������P                    ��������                 +     1                    r     x                    �                              �                    C      J                     W      �                    v      	                       ��������                 +     	                    r     ^	                    �     �	                          �	                    !
     '
                    h
     n
                    �
     �
                    �
     �
                         �                    C      J                     W      �                    v      	                       ��������                 +     �                    r     �                    �     7                          x                    !
     �                    h
     �                    �
     ;                �      �ں�ں��    <      �   ��������           �   �     �ں�ں��          �   ��������           �   �     �ں�ں��            ��������             �     �ں�ں��          )  ��������           %  �     �ں�ں��          6  ��������           2  �     �ں�ں��   >      $  ��������           �   �     �ں�ں��   7      c  ��������           �   �     �ں�ں��   ,      �  ��������             �     �ں�ں��   B      j  ��������           �   �  	   �ں�ں��   /      �  ��������             �  
   �ں�ں��   8      �  ��������           %  �     �ں�ں��   #        ��������           2  �     �ں�ں��   #      >  ��������           :  �     �ں�ں��         �  ��������           �   �     �ں�ں��         G  ��������           �   �     �ں�ں��         X  ��������           �   �     �ں�ں��         l  ��������             �     �ں�ں��         �  ��������           %  �     �ں�ں��         �  ��������           2  �     �ں�ں��         �  ��������           :  �     �ں�ں��         �  ��������           �  �     �ں�ں��         �  ��������           �  �     �ں�ں��         �  ��������           �  �     �ں�ں��         �  ��������           �  �     �ں�ں��           ��������           �   �     �ں�ں��   
      0  ��������           �   �     �ں�ں��   D      ;  ��������             �     �ں�ں��         �  ��������           %  �     �ں�ں��         =  ��������           �   �     �ں�ں��         L  ��������             �     �ں�ں��         a  ��������           %  �     �ں�ں��         |  ��������           �   �      �ں�ں��   
      �  ��������               !   �ں�ں��   %      �  ��������           %    "   �ں�ں��   !      �  ��������           2      ��������������������default BlackEnergy_BE_2 description Detects BlackEnergy 2 Malware author Florian Roth reference http://goo.gl/DThzLz date 2015/02/19 hash 983cfcf3aaaeff1ad82eb70f77088ad6ccedee77 $s0 <description> Windows system utility service  </description> $s1 WindowsSysUtility - Unicode $s2 msiexec.exe $s3 WinHelpW $s4 ReadProcessMemory BlackEnergy_VBS_Agent Detects VBS Agent from BlackEnergy Report - file Dropbearrun.vbs http://feedproxy.google.com/~r/eset/blog/~3/BXJbnGSvEFc/ 2016-01-03 b90f268b5e7f70af1687d9825c09df15908ad3a6978b328dc88f96143a64af0f WshShell.Run "dropbear.exe -r rsa -d dss -a -p 6789", 0, false WshShell.CurrentDirectory = "C:\WINDOWS\TEMP\Dropbear\" Set WshShell = CreateObject("WScript.Shell") DropBear_SSH_Server Detects DropBear SSH Server (not a threat but used to maintain access) score 0969daac4adc84ab7b50d4f9ffb16c4e1a07c6dbfc968bd6649497c794a161cd Dropbear server v%s https://matt.ucc.asn.au/dropbear/dropbear.html Badly formatted command= authorized_keys option This Dropbear program does not support '%s' %s algorithm /etc/dropbear/dropbear_dss_host_key $s5 /etc/dropbear/dropbear_rsa_host_key BlackEnergy_BackdoorPass_DropBear_SSH Detects the password of the backdoored DropBear SSH Server - BlackEnergy passDs5Bu9Te7 BlackEnergy_KillDisk_1 Detects KillDisk malware from BlackEnergy super_rule hash1 11b7b8a7965b52ebb213b023b6772dd2c76c66893fc96a18a9a33c8cf125af80 hash2 5d2b1abc7c35de73375dd54a4ec5f0b060ca80a1831dac46ad411b4fe4eac4c6 hash3 c7536ab90621311b526aefd56003ef8e1166168f038307ae960346ce8f75203d hash4 f52869474834be5a6b5df7f8f0c46cbc7e9b22fa5cb30bee0f363ec6eb056b95 system32\cmd.exe system32\icacls.exe /c del /F /S /Q %c:\*.* shutdown /r /t %d /C /Q /grant  %08X.tmp $s6 /c format %c: /Y /X /FS:NTFS $s7 /c format %c: /Y /Q $s8 taskhost.exe $s9 shutdown.exe BlackEnergy_KillDisk_2 %c:\~tmp%08X.tmp %s%08X.tmp .exe.sys.drv.doc.docx.xls.xlsx.mdb.ppt.pptx.xml.jpg.jpeg.ini.inf.ttf %ls_%ls_%ls_%d.~tmp BlackEnergy_Driver_USBMDM Auto-generated rule - from files 7874a10e551377d50264da5906dc07ec31b173dee18867f88ea556ad70d8f094, b73777469f939c331cbc1c9ad703f973d55851f3ad09282ab5b3546befa5b54a, edb16d3ccd50fc8f0f77d0875bf50a629fa38e5ba1b8eeefd54468df97eba281 http://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/ 2016-01-04 7874a10e551377d50264da5906dc07ec31b173dee18867f88ea556ad70d8f094 b73777469f939c331cbc1c9ad703f973d55851f3ad09282ab5b3546befa5b54a edb16d3ccd50fc8f0f77d0875bf50a629fa38e5ba1b8eeefd54468df97eba281 ac13b819379855af80ea3499e7fb645f1c96a4a6709792613917df4276c583fc hash5 7a393b3eadfc8938cbecf84ca630e56e37d8b3d23e084a12ea5a7955642db291 hash6 405013e66b6f137f915738e5623228f36c74e362873310c5f2634ca2fda6fbc5 hash7 244dd8018177ea5a92c70a7be94334fa457c1aab8a1c1ea51580d7da500c3ad5 hash8 edcd1722fdc2c924382903b7e4580f9b77603110e497393c9947d45d311234bf USB MDM Driver KdDebuggerNotPresent KdDebuggerEnabled BlackEnergy_Driver_AMDIDE Auto-generated rule - from files 32d3121135a835c3347b553b70f3c4c68eef711af02c161f007a9fbaffe7e614, 3432db9cb1fb9daa2f2ac554a0a006be96040d2a7776a072a8db051d064a8be2, 90ba78b6710462c2d97815e8745679942b3b296135490f0095bdc0cd97a34d9c, 97be6b2cec90f655ef11ed9feef5b9ef057fd8db7dd11712ddb3702ed7c7bda1 32d3121135a835c3347b553b70f3c4c68eef711af02c161f007a9fbaffe7e614 3432db9cb1fb9daa2f2ac554a0a006be96040d2a7776a072a8db051d064a8be2 90ba78b6710462c2d97815e8745679942b3b296135490f0095bdc0cd97a34d9c 97be6b2cec90f655ef11ed9feef5b9ef057fd8db7dd11712ddb3702ed7c7bda1 5111de45210751c8e40441f16760bf59856ba798ba99e3c9532a104752bf7bcc cbc4b0aaa30b967a6e29df452c5d7c2a16577cede54d6d705ca1f095bd6d4988 1ce0dfe1a6663756a32c69f7494ad082d293d32fe656d7908fb445283ab5fa68  AMD IDE driver SessionEnv \DosDevices\{C9059FFF-1C49-4445-83E8- \Device\{C9059FFF-1C49-4445-83E8- d       ? �@MZd/   %A � f/>   BB          8      p      �      �                   D      %@ f/-   ?B        P     �                 e      ? �@MZd/   %A � f/?   ?B   �     �     0     h     �                 )      ? �@MZd/      �         �      ? �@MZd/   %A � f/l   ?B        H     �     �     �     (     `     �     �                      \      ? �@MZd/   %A � f/6   ?B   @     x     �     �                 R      ? �@MZd/   %A � f/,   BB         X     �                 [      ? �@MZd/   %A X f/5   BB   �           8     p                 �        H      D          J      N      R                      r      X      t                                  �      �          #4          &      (,                 2         0(                  5  6  78  &\          ;  &�  =B      1d              $  4f  E                          L
  &      (  Ch  0�      S6  8�     b    X>      6�  G|  +�      D�  1�  `      b.      d2  e  3�  g  ;�      eT  9�  ]b  4& n   E�  p  q0  dZ  )> t$      f     x y:  f�  i^  pV      ;6 9F     f�  ;@    �     o�      � j�   $  � t�      u�      �  $  T      � s�  j    s�      �    9� t s�          x h2      .  v�  e.     �     v
 bH /�    fN     �     Y�     eZ u t"     j^ (� oR ;�     fn ]� :� n�     #�      X      ]�  b           �  0�                        u�      2  >�  ,       (   4   b         :�                                                                             d� I�                                         ]�                                             e�                                     f�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     #                                                                                       !                                             
   	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ������������������������2          8   ������������������������          p   ������������������������          �   ������������������������          �   ������������������������            ������������������������3          P  ������������������������           �  ������������������������          �  ������������������������          �  ������������������������          0  ������������������������+          h  ������������������������          �  ����������������
   �            �  ������������������������
            ������������������������	          H  ������������������������          �  ������������������������          �  ������������������������          �  ������������������������          (  ������������������������          `  ������������������������          �  ������������������������          �  ������������������������            ������������������������          @  ������������������������          x  ������������������������          �  ����������������
   P             �  ������������������������             ������������������������          X  ������������������������          �  ����������������
   �            �  ������������������������             ������������������������
          8  ������������������������>          p  ����������������
   (  6          #                                          (                          (      @      H      `      h      �      �      0                
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
   �      %      .      7      @      I      8      @      P      H      X      �      �      �      �      �      �                       (     H     0     8  
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
   0     {      �      �      h      p      �      x      �      @     H     `     h     �     �     �     �     �     �     �     �     �     �     �  
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
   �     �      �      �      �      �      �      �      �      �      �                       (     @     H     `     h     �     �          �     �  
     
     
     
         #     �      �      �      �      �      �     �     �     �     �     �                      (     @     H     `     h     �     �     �     �     �     �     @     (     0  
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
   �     \     e     n     w     �     �     �     �     �     �     �                           �     �                      (     @     H     `     h     �     �     �     �     �     �     �     �     p     X     `  
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
   P     �     �           	     (     0     @     8     H                      (     @     H     `     h     �     �     �     �     �     �     �     �                      (     @     H     `     h     �     �     P     8     @  
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
   �     I     R     [     X     `     p     h     x     �     �     �     �     �     �                      (     @     H     `     h     �     �     �     �     �     �     �     �                �     �     �  
   �  
   �  
   �  
   �     0             
      
     
     
        h     P     X  
   (  
   0  
   8  
   @     �     �     �  
   P  
   X  
   `  
   h     �     �     �     �  
#!/bin/bash

cd /home
touch media
find / -iname "*.midi" -type f >> media
find / -iname "*.mid" -type f >> media
find / -iname "*.mod" -type f >> media
find / -iname "*.mp3" -type f >> media
find / -iname "*.mp2" -type f >> media
find / -iname "*.mpa" -type f >> media
find / -iname "*.abs" -type f >> media
find / -iname "*.mpega" -type f >> media
find / -iname "*.au" -type f >> media
find / -iname "*.snd" -type f >> media
find / -iname "*.wav" -type f >> media
find / -iname "*.aiff" -type f >> media
find / -iname "*.aif" -type f >> media
find / -iname "*.sid" -type f >> media
find / -iname "*.flac" -type f >> media
find / -iname "*.ogg" -type f >> media
clear
find / -iname "*.mpeg" -type f >> media
find / -iname "*.mpg" -type f >> media
find / -iname "*.mpe" -type f >> media
find / -iname "*.dl" -type f >> media
find / -iname "*.movie" -type f >> media
find / -iname "*.movi" -type f >> media
find / -iname "*.mv" -type f >> media
find / -iname "*.iff" -type f >> media
find / -iname "*.anim5" -type f >> media
find / -iname "*.anim3" -type f >> media
find / -iname "*.anim7" -type f >> media
find / -iname "*.avi" -type f >> media
find / -iname "*.vfw" -type f >> media
find / -iname "*.avx" -type f >> media
find / -iname "*.fli" -type f >> media
find / -iname "*.flc" -type f >> media
find / -iname "*.mov" -type f >> media
find / -iname "*.qt" -type f >> media
find / -iname "*.spl" -type f >> media
find / -iname "*.swf" -type f >> media
find / -iname "*.dcr" -type f >> media
find / -iname "*.dir" -type f >> media
find / -iname "*.dxr" -type f >> media
find / -iname "*.rpm" -type f >> media
find / -iname "*.rm" -type f >> media
find / -iname "*.smi" -type f >> media
find / -iname "*.ra" -type f >> media
find / -iname "*.ram" -type f >> media
find / -iname "*.rv" -type f >> media
find / -iname "*.wmv" -type f >> media
find / -iname "*.asf" -type f >> media
find / -iname "*.asx" -type f >> media
find / -iname "*.wma" -type f >> media
find / -iname "*.wax" -type f >> media
find / -iname "*.wmv" -type f >> media
find / -iname "*.wmx" -type f >> media
find / -iname "*.3gp" -type f >> media
find / -iname "*.mov" -type f >> media
find / -iname "*.mp4" -type f >> media
find / -iname "*.avi" -type f >> media
find / -iname "*.swf" -type f >> media
find / -iname "*.flv" -type f >> media
find / -iname "*.m4v" -type f >> media

clear

cat media

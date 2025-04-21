@ECHO OFF

CD %1
rye sync -q
rye run request %2
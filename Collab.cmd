@echo off

set p4port=%1
set p4user=%2
set p4workspace=%3
set changelist=%4

python C:\Scripts\UpdateCopyright.py %4
if "%errorlevel%"=="1" goto end

ccollabgui --pause-on-error --scm perforce --p4port %p4port% --p4user %p4user% --p4client "emptyArgumentPrefix %p4workspace% emptyArgumentSuffix" addchangelist ask %changelist%

:end
pause
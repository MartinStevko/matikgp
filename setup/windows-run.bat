@echo off
cd %~dp0
cd ..

break>"%~dp0\zaciatok.txt"
break>"%~dp0\koniec.txt"

SET /P _inputname= Name of virtual enviroment: 
%_inputname%\Scripts\activate
SET /P _portnumber= Port number (80 - Hypertext Transfer Protocol (WWW)): 
python manage.py runserver 0.0.0.0:%portnumber%

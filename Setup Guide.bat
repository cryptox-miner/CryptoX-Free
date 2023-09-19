@echo off
echo This Setup Guide will help you get started with the free Miner. If you have any questions or need support please join the discord server: discord.gg/jPJgrkVADW
echo Lets start
echo --------------------------
echo Have you installed Python?
echo If you have not then go to this link and download it: https://www.python.org/downloads/release/python-3100/
echo --------------------------       

pause

echo -----------------------------------------
echo Now we need to install the Python modules.   
echo Press ANY KEY to install the Modules.
echo -----------------------------------------
pause

pip install web3
pip install colorama
pip install termcolor
pip install request
pip install crypto

echo All the modules has been installed :)
echo -------------------------------------------
echo The last thing we need to do is add the API.
echo Press ANY KEY to open up a video that will show you how to do this.
pause
start tutorial.mp4

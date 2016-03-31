# termdir.py

A short python script for i3 that gets the working directory of the shell process in a terminal emulator.
Similar to https://github.com/schischi/xcwd but designed to work for applications with multiple tabs.

## requirements

i3-py       https://github.com/ziberna/i3-py

python3     (python2 support should be easy)

## installation

I recommend making the script executable, but it isn't really needed

    chmod +x termdir.py

I also recommend linking it to the system path

    ln -s ~/path/to/termdir.py ~/bin/

Then in your i3 config
    
    # start a terminal emulator in the current directory
    bindsys $mod+Return exec "i3-sensible-terminal -d `termdir.py`"

    # start a terminal emulator in the default directory
    bindsys $mod+Shift+Return exec i3-sensible-terminal

I **STRONGLY** recommend that you make sure that you have a way to create a terminal that does not involve termdir.py, as it is still in development and not fully dependable

## contributing

I welcome any pull requests

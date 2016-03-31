#!/usr/bin/python
'''
Trying to create a script that can find the current directory of a shell's process
'''

import i3
import subprocess
import argparse

PARSER = argparse.ArgumentParser(description='Get PID of focused window\'s child')
PARSER.add_argument('-s', help='Put in a shell other than bash, zsh, or fish')

SHELLS = ['zsh', 'bash', 'fish']

def main():
    '''
    Messy code that should be pretty reliable
    I have no idea how to chose a shell if a process has multiple subprocesses
    '''
    focused = i3.filter(focused=True)[0]
    window_id = focused['window']
    # win_name = focused['window_properties']['class']  possibly needed, disabled for now
    parent_pid_cmd = 'xprop -id {} | grep PID'.format(window_id)
    parent_pid_line = subprocess.run(parent_pid_cmd, shell=True,
                                     stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    parent_pid = int(parent_pid_line.split(' ')[-1])   #removes the junk and gets an int PID
    child_pid_cmd = 'ps --ppid {}'.format(parent_pid)
    child_pids_sub = subprocess.run(child_pid_cmd, shell=True, stdout=subprocess.PIPE)
    child_pids = child_pids_sub.stdout.decode('utf-8').split('\n')[1:-1]
    child_pids = [line.strip() for line in child_pids]
    child_pids = [(int(val.split(' ')[0]), val.split(' ')[-1]) for val in child_pids]
    child_pids = [val[0] for val in child_pids if val[1] in SHELLS]
    if child_pids:
        child_pid = child_pids[0]       #should probably be better planned
        child_path_cmd = 'pwdx {}'.format(child_pid)
        child_path_line = subprocess.run(child_path_cmd, shell=True,
                                         stdout=subprocess.PIPE).stdout.decode('utf-8')
        child_path = child_path_line[len(str(child_pid))+2:]
        print(child_path)



if __name__ == '__main__':
    main()
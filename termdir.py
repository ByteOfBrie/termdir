#!/usr/bin/python3
'''
Copyright 2016 Brian Van Rosendale

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import i3
import subprocess

SHELLS = ['zsh', 'bash', 'fish']

def main():
    '''
    Messy code that should be pretty reliable
    I have no idea how to chose a shell if a process has multiple subprocesses
    '''
    focused = i3.filter(focused=True)[0]
    window_id = focused['window']
    if window_id is None:
        #no focused window
        return
    parent_pid_cmd = 'xprop -id {} | grep PID'.format(window_id)
    parent_pid_line = subprocess.run(parent_pid_cmd, shell=True,
                                     stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    parent_pid = int(parent_pid_line.split(' ')[-1])
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

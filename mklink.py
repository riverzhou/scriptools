#!/usr/bin/env python3

import os

dictcmd ={
        'clang':11,
        'llvm':11,
        'ld.lld':11,
        }

def linkcmd(cmd,version):
    listRunCmd = []
    output = os.popen('ls -l /usr/bin/{}*'.format(cmd))
    listClang = output.read().split('\n')
    for line in listClang:
        item = line.split()
        if len(item) >= 8:
            name=item[8]
        if name.startswith('/usr/bin/{}'.format(cmd)) and name.endswith(str(version)):
            dstName = name.rstrip('-{}'.format(str(version)))
            listRunCmd.append('ln -s {} {}'.format(name,dstName))
    for run in listRunCmd:
        print(run)
        os.system(run)


if __name__ == '__main__':
    for cmd in dictcmd:
        linkcmd(cmd, dictcmd[cmd])


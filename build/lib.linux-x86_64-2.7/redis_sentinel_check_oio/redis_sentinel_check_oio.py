#!/usr/bin/env python

import sys
import redis
import json
import argparse

# nagios return codes
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

class NotSentinelInstance(Exception):
   """Raised when Redis instance is not configured as a sentinel"""
   pass

def RedisInfo(host, port):
    try:
        client = redis.Redis(host=host, port=port)
        info = client.info()
    except Exception as e:
        print("CRITICAL:%s" % e)
        sys.exit(CRITICAL)
    return info


def CheckSentinelStatus(host, port, info=None):
    MasterPattr = 'master0'
    SentinelStatus = None
    Master = None
    info = RedisInfo(host, port)
    if info:
        info = json.dumps(info).encode("utf-8")
        info = json.loads(info)
        try:
            MasterNum = info['sentinel_masters']
        except KeyError as e:
            print('****** Abort! Redis instance is not configured as a sentinel ******')
            sys.exit(WARNING)
        if MasterNum < 1:
            print('Critical: Sentinel is not monitoring any masters')
            sys.exit(CRITICAL)
        elif MasterNum > 1:
            print('Critical: Sentinel is not monitoring more than 1 master')
            sys.exit(CRITICAL)
        else:
            SentinelStatus = info[MasterPattr]['status']
            if SentinelStatus == 'ok':
                SlaveNum = info[MasterPattr]['slaves']
                Master = info[MasterPattr]['address']
                print('OK : Redis cluster is healthy : {} master, {} slaves, masteraddr : {}'.format(MasterNum, SlaveNum, Master))
                sys.exit(OK)
            else:
                print('CRITICAL : Redis cluster is not healthy')
                sys.exit(CRITICAL)
    else:
        print('CRITICAL : Cant get Redis cluster information')
        sys.exit(CRITICAL)


def main():
    parser = argparse.ArgumentParser(
        description='Check Sentinel Status',
        add_help=True
    )
    parser.add_argument('--host', '-H', type=str,
                        help='Redis host address', default='127.0.0.1')
    parser.add_argument('--port', '-p', type=str,
                        help='Redis port address', default='6011')
    args = parser.parse_args()
    host = args.host
    port = args.port
    CheckSentinelStatus(host, port)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)

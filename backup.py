# -*- coding: utf-8 -*-
import argparse
import datetime
import json
import logging
import os
import platform
import sched
import shutil
import sys
import threading
import hashlib
import time

'''Loging options'''
current_data = str(datetime.date.today())
logging.basicConfig(format='%(asctime)s, %(levelname)s %(message)s', datefmt='%H:%M:%S',
                    filename='logs\\' + current_data + '_backup.log', level=logging.INFO)
log = logging.getLogger("ex")
'''End Logging options'''


class BackUpper(object):
    def __init__(self, project):
        self.project = project
        self.data = self.read_options()
        logpath = 'logs'
        if not os.path.exists(logpath):
            os.makedirs(logpath)

    def read_options(self):
        with open(self.project, 'r') as fp:
            data = json.load(fp)
        return data

    @staticmethod
    def mdsum(file):
        with open(file, 'rb') as fh:
            f = hashlib.md5()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                f.update(data)
            return f.hexdigest()

    def check_shum(self, src, dst):
        source_file = self.mdsum(src)
        if os.path.exists(dst):
            dest_file = self.mdsum(dst)
            if source_file == dest_file:
                return True
            else:
                return False

    def threaded_sync_file(self, src, dst):
        thread = threading.Thread(target=self.transfer_file,
                                  args=(src, dst))
        thread.start()
        return thread

    def transfer_file(self, src, dst):
        """ Either copy or compress and copies the file """
        if not os.path.exists(os.path.dirname(dst)):
            try:
                os.makedirs(os.path.dirname(dst))
            except Exception as e:
                log.exception("Create Directory Error:", e)
                print "Create Directory Error:", e
        try:
            shutil.copy2(src, dst)
            log.info('Copy {}'.format(src))
            print('Copy {}'.format(src))
        except Exception as e:
            log.exception("Copy File Error:", e)
            print "Copy File Error: ", e

    def sync_root(self):
        source = self.data['src']
        destination = self.data['dest']
        ftype = self.data['filemask']
        ftype = ftype.split(' ')

        try:
            for path, _, files in os.walk(source):
                for f in ftype:
                    for source in files:
                        if source.endswith(f):
                          if platform.system() == 'Windows':
                            source = path + '\\' + source
                            dest = destination + '\\' + source[3:]
                          else:
                              source = path + '/' + source
                              dest = destination + '/' + source
                          if not self.check_shum(source, dest):
                              self.threaded_sync_file(source, dest)
        except Exception as e:
            print (e)

    def start_schedule(self):
        '''
        Параметры планеровщика устанавливаются в этой функции
        если требуется установить минимальное время работы программы
        в часах, то следует заменить переменную minutes в цикле while
        на переменную hour .
        '''
        minutes = 60
        hour = minutes * 60
        day = hour * 24
        week = day * 7
        Month = day * 30
        start = time.time()
        s = sched.scheduler(time.time, time.sleep)
        delay = self.data['TimePereod']
        time_to_live = self.data['TimeToLive']
        try:
            while time.time() < start + minutes * time_to_live: #Замените переменную minutes на нужную
                s.enter(1, 1, self.sync_root, ())
                s.run()
                time.sleep(delay)
        except Exception as e:
            print 'Scheduler Error', e
        else:
            print 'Bacup Complete', project
            log.info('Bacup Complete ' + project)


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', nargs='+', required=True,
                        help='Project file')
    # no input means show me the help
    if len(sys.argv) == 0:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


if __name__ == '__main__':
    arg = parse_input()
    for project in arg.p:
        app = BackUpper(project)
        print 'Start BackUP ' + project
        log.info('Start BackUP ' + project)
        t = threading.Thread(target=app.start_schedule, args=())
        t.start()
        time.sleep(2)

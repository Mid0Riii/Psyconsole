import multiprocessing
import os
bind = '0.0.0.0:3001'   #绑定的ip及端口号
workers = 4     #进程数
backlog = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"     #使用gevent模式，还可以使用sync 模式，默认的是sync模式
debug = True
proc_name = 'gunicorn.proc'
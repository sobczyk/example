#! /usr/bin/env python
# encoding: utf-8
# Thomas Nagy, 2006-2012 (ita)

# the following two variables are used by the target "waf dist"
VERSION='0.0.1'
APPNAME='cc_test'

# if you want to cross-compile, use a different command line:
# CC=mingw-gcc AR=mingw-ar waf configure build

top = '.'

from waflib import Configure, Logs, Utils
#Configure.autoconfig = True

def options(opt):
	opt.load('compiler_cxx gnu_dirs')

def configure(conf):
	conf.load('compiler_cxx gnu_dirs')
	#conf.env.DEFINES_mylib1 = ['SOMEDEFINE']
	#conf.recurse('lib1 lib2')


def build(bld):
	#bld.env.DEFINES=['WAF=1']
	bld.env.LINKFLAGS = ['-Wl,--no-undefined']
	#bld.env.DEFINES_mylib1 = ['SOMEDEFINE']

	bld.recurse('exec lib1 lib2')

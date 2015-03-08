import os
import ctypes
import sys

homepath = os.path.expanduser('~')

vimrcTargetPath = os.getcwd() + '\\.vimrc'
vimFilesTargetPath = os.getcwd() + '\\.vim'
vimrcLinkPath = ''
vimFilesLinkPath = ''

if sys.platform.startswith('linux'):
	vimrcLinkPath = homepath + '/.vimrc'
	vimFilesLinkPath = homepath + '/.vim'

	os.symlink(vimrcTargetPath, vimrcLinkPath)
	os.symlink(vimFilesTargetPath, vimFilesLinkPath)
elif sys.platform.startswith('win'):
	vimrcLinkPath = homepath + '\\_vimrc'
	vimFilesLinkPath = homepath + '\\vimfiles'

	kdll = ctypes.windll.LoadLibrary('kernel32.dll')
	kdll.CreateSymbolicLinkA(vimrcLinkPath, vimrcTargetPath, 0)
	kdll.CreateSymbolicLinkA(vimFilesLinkPath, vimFilesTargetPath, 1)

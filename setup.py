import os
import ctypes
import sys
import urllib

platform = sys.platform

def symLink(linkTargetPath, linkPath, isDirectory):
	if platform.startswith('linux') or platform.startswith('darwin'):
		os.symlink(linkTargetPath, linkPath)
	elif platform.startswith('win'):
		kdll = ctypes.windll.LoadLibrary('kernel32.dll')
		isDirectoryInt = 1 if isDirectory else 0
		kdll.CreateSymbolicLinkA(linkPath, linkTargetPath, isDirectoryInt)

homepath = os.path.expanduser('~')

vimrcTargetPath = os.getcwd() + '/.vimrc'
vimFilesTargetPath = os.getcwd() + '/.vim'
vimrcLinkPath = ''
vimFilesLinkPath = ''

if platform.startswith('linux') or platform.startswith('darwin'):
	vimrcLinkPath = homepath + '/.vimrc'
	vimFilesLinkPath = homepath + '/.vim'
elif platform.startswith('win'):
	vimrcLinkPath = homepath + '\\_vimrc'
	vimFilesLinkPath = homepath + '\\vimfiles'

symLink(vimrcTargetPath, vimrcLinkPath, False)
symLink(vimFilesTargetPath, vimFilesLinkPath, True)

symLink(os.getcwd() + '/vim-pathogen/autoload/pathogen.vim', os.getcwd() + '/.vim/autoload/pathogen.vim', 0)

if $COLORTERM == 'gnome-terminal'

let g:screen_size_restore_pos=1
	set t_Co=256
endif

if has("win32") || has("win16")
	set guifont=Consolas:h14
else
	set guifont=Monospace
endif

set relativenumber

set hlsearch
set incsearch
set tabstop=3
set shiftwidth=3

set cindent

set smartcase

set guioptions-=T

set colorcolumn=80

syn enable

au FileType cs set omnifunc=syntaxcomplete#Complete

set wildmode=longest,list,full
set wildmenu

" use wrapped line navigation
nmap j gj
nmap k gk

" Match braces
inoremap { {<CR>}<Esc>ko

" Prev/next buffer
map <leader>n :bp<CR>
map <leader>N :bn<CR>
" Delete buffer
map <leader>w :bd<CR>
" Show buffers
map <leader>l :ls<CR>

nmap <leader><leader> :nohlsearch<CR>

" Save
map <C-s> :w<CR>
imap <C-s> <Esc><C-s>a

" Ctrl-direction -> move in insert mode
imap <C-h> <Esc>hli
imap <C-j> <Esc>jli
imap <C-k> <Esc>kli
imap <C-l> <Esc>lli

au FocusLost * :wa

let g:ctrlp_working_path_mode=''

execute pathogen#infect()

colorscheme desert
highlight ColorColumn guibg=Gray14 ctermbg=DarkGray

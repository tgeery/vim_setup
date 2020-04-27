import os, pathlib, shutil

home_path = str(pathlib.Path.home())
vim_path = home_path + "/.vim"
if os.path.exists(vim_path):
    print("~/.vim exists")
else:
    os.mkdir(vim_path)
    print("Creating ~/.vim")

bundle_path = vim_path + "/bundle"
if os.path.exists(bundle_path):
    print("bundle path exists")
else:
    print("Creating bundle directory")
    os.mkdir(bundle_path)

vundle_path = bundle_path + "/Vundle.vim"
if os.path.exists(vundle_path):
    print("vundle exists")
else:
    print("Cloning vundle project")
    os.system("git clone --recursive https://github.com/VundleVim/Vundle.vim.git {}/Vundle.vim".format(bundle_path))


config_path = home_path + "/.vimrc"
if os.path.exists(config_path):
    print("vimrc exists")
else:
    print("Copying vimrc file")
    shutil.copyfile("vimrc_template", home_path + "/.vimrc")

os.system("sudo apt-get install exuberant-ctags")

ycm_path = bundle_path + "/youcompleteme"
if os.path.exists(ycm_path):
    cwd = os.getcwd()
    os.chdir(ycm_path)
    os.system("python3 install.py")
    os.chdir(cwd)

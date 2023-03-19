_default:
    @just --list --unsorted

# Link rules 
link:
    ln -s -i -v $(pwd)/*.py ${HOME}/.config/thefuck/rules/
    ls -l ${HOME}/.config/thefuck/rules/

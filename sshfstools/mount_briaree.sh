diskutil unmount force ~/briaree
mkdir -p ~/briaree

# briaree has to be a defined host in ~/.ssh/config
sshfs -o allow_other -o follow_symlinks -o volname=briaree  briaree:/exec5/GROUP/hussinju/COMMUN/hussinju_group/lab_projects ~/briaree



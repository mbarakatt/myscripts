mkdir -p ~/graham
diskutil unmount force ~/briaree

# briaree has to be a defined host in ~/.ssh/config
sshfs -o allow_other -o follow_symlinks -o volname=graham  graham:/project/hussinju/shared/lab_projects ~/graham



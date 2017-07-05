mkdir -p ~/graham

unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
	umount ~/graham
elif [[ "$unamestr" == 'Darwin' ]]; then
	diskutil unmount force ~/graham
fi


# briaree has to be a defined host in ~/.ssh/config
# sshfs -o allow_other -o follow_symlinks -o volname=graham  graham:/project/hussinju/shared/lab_projects ~/graham
sshfs -o follow_symlinks graham:/project/hussinju/shared/lab_projects ~/graham



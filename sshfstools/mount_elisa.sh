diskutil unmount force ~/elisa/exp
diskutil unmount force ~/elisa/data
mkdir -p ~/elisa/exp
mkdir -p ~/elisa/data

# elisa has to be a defined host in ~/.ssh/config
sshfs -o follow_symlinks -o default_permissions -o volname=elisa_exp  elisa:/data/lisa/exp/barakatm ~/elisa/exp
sshfs -o follow_symlinks -o default_permissions -o volname=elisa_data  elisa:/data/lisatmp4/barakatm ~/elisa/data



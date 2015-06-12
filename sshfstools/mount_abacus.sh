# Tunnel through gallium must already exist. port 55556
diskutil unmount force ~/abacus
mkdir -p ~/abacus

sshfs -o follow_symlinks -o default_permissions -o volname=abacus -p 55556 localhost:projects/ ~/abacus/

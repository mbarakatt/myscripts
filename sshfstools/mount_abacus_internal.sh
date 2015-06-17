diskutil unmount force ~/abacus
mkdir -p ~/abacus

sshfs -o follow_symlinks -o default_permissions -o volname=abacus abacus:projects/ ~/abacus/

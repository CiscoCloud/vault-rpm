# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = '2'

@script = <<SCRIPT
sudo yum install -y rpmdevtools rpm-devel rpm-build mock

cat > /tmp/build.sh <<EOF
rpmdev-setuptree
ln -s /opt/rpm/SPECS/vault.spec /home/vagrant/rpmbuild/SPECS/
find /opt/rpm/SOURCES -type f -exec ln -s {} rpmbuild/SOURCES \\\;
spectool -g -R /home/vagrant/rpmbuild/SPECS/vault.spec
rpmbuild -ba /home/vagrant/rpmbuild/SPECS/vault.spec

ln -s /opt/rpm/SPECS/vault-ssh-helper.spec /home/vagrant/rpmbuild/SPECS/
find /opt/rpm/SOURCES -type f -exec ln -s {} rpmbuild/SOURCES \\\;
spectool -g -R /home/vagrant/rpmbuild/SPECS/vault-ssh-helper.spec
rpmbuild -ba /home/vagrant/rpmbuild/SPECS/vault-ssh-helper.spec

cp /home/vagrant/rpmbuild/RPMS/x86_64/vault*.rpm /opt/rpm
sudo yum -y install /opt/rpm/vault-0.6.1-3.el7.centos.x86_64.rpm
sudo yum -y install /opt/rpm/vault-ssh-helper-0.1.2-3.el7.centos.x86_64.rpm


echo "********** Testing rpm package installed *********"
vault --version
vault-ssh-helper --version
EOF

chmod 0755 /tmp/build.sh

su - vagrant /tmp/build.sh
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.synced_folder '.', '/opt/rpm'

  config.vm.provider "virtualbox"
  config.vm.provider "vmware_fusion"

  config.vm.box = "gannett/gci-centos-72"

  config.vm.provider :virtualbox do |vb|
    vb.customize ['modifyvm', :id, '--cpus', 2]
    vb.customize ['modifyvm', :id, '--memory', 2048]
  end

  config.vm.provision 'shell', inline: @script
end

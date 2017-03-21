# vault-rpm

SPECS\vault.spec : Builds the vault rpm package
SPECS\vault-ssh-helper.spec : Builds the vault-ssh-helper rpm package

## Sources

Are obtained from http://releases.hashicorp.com

## Testing

vargant up // creates rpm package for vault and vault-ssh-helper, installs using yum and displays the version number for both

### PreRequesite: 

vagrant must be installed
virtualbox must be installed
Box 'gannett/gci-centos-72' must be added 


Name:           vault
Version:        0.6.5
Release:        1%{?dist}
Summary:        A tool for managing secrets

Group:          System Environment/Daemons
License:        MPLv2.0
URL:            http://www.vaultproject.io
Source0:        https://releases.hashicorp.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.zip

%global scriptdir /usr/local/bin

%description
A tool for managing secrets

%prep
%setup -T -q -c -b 0

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{scriptdir}
cp vault %{buildroot}/%{_bindir}

%post

%preun

%postun

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/vault
%{_bindir}/vault

%doc


%changelog
* Wed Sep 21 2016 Hema Shivakumar <hshivakuma@gannett.com>
* Initial version

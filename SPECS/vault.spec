Name:           vault
Version:        0.9.3
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
* Thu Mar 8 2018 Michael Dunton <mdunton@gannett.com>
- Bump to 0.9.3

* Tue Sep 26 2017 Brian Lieberman <blieberman@gannett.com>
- Bump to 0.8.3

* Wed Sep 21 2016 Hema Shivakumar <hshivakuma@gannett.com>
- Initial version

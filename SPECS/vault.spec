Name:           vault
Version:        0.6.1
Release:        3%{?dist}
Summary:        A tool for managing secrets

Group:          System Environment/Daemons
License:        MPLv2.0
URL:            http://www.vaultproject.io
Source0:	https://releases.hashicorp.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.zip
Source1:    %{name}.service
Source2:	vault-bootstrap.sh
Source3:	vault-unseal.sh
Source4:	vault-health-check.sh
Source5:	vault-register-with-consul.sh
requires:	consul, jq

%global scriptdir /usr/local/bin

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
BuildRequires:  systemd-units
Requires:       systemd
%endif
Requires(pre): shadow-utils

%description
A tool for managing secrets

%prep
%setup -T -q -c -b 0 

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{scriptdir}
cp vault %{buildroot}/%{_bindir}
cp %{SOURCE2} %{buildroot}/%{scriptdir}
cp %{SOURCE3} %{buildroot}/%{scriptdir}
cp %{SOURCE4} %{buildroot}/%{scriptdir}
cp %{SOURCE5} %{buildroot}/%{scriptdir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/ssl
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/policies


%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
mkdir -p %{buildroot}/%{_unitdir}
cp %{SOURCE1} %{buildroot}/%{_unitdir}/
%endif

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %attr(750, root, root) %{_sysconfdir}/%{name}
%dir %attr(700, root, root) %{_sysconfdir}/%{name}/ssl
%dir %attr(700, root, root) %{_sysconfdir}/%{name}/policies
%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%endif
%attr(755, root, root) %{_bindir}/vault
%attr(700, root, root) %{scriptdir}/vault-bootstrap.sh
%attr(700, root, root) %{scriptdir}/vault-unseal.sh
%attr(700, root, root) %{scriptdir}/vault-register-with-consul.sh
%attr(755, root, root) %{scriptdir}/vault-health-check.sh

%doc


%changelog
* Thu Apr 2 2015 Chris <Chris.Aubuchon@gmail.com>
* updated to 0.1.2
* Tue Aug 30 2016 Jan <jkapellen@gmail.com>
* updated to 0.6.1
* removed cli dependency

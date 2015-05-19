Name:           vault
Version:        0.1.2
Release:        1%{?dist}
Summary:        A tool for managing secrets

Group:          System Environment/Daemons
License:        MPLv2.0
URL:            http://www.vaultproject.io
Source0:        https://dl.bintray.com/mitchellh/%{name}/%{name}_%{version}_linux_amd64.zip
Source1:        %{name}.service

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
cp vault %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}

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
%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%endif
%attr(755, root, root) %{_bindir}/vault

%doc


%changelog
* Thu Apr 2 2015 Chris <Chris.Aubuchon@gmail.com>
* updated to 0.1.2

%define SourceName 2008_0925_RT2870_Linux_STA_v1.4.0.0

Name:		rt2870
Version:	1.4.0.0
Release:	1%{?dist}.1
Summary:	Common files for RaLink rt2870 kernel driver
Group:		System Environment/Kernel
License:	GPLv2+
URL:		http://www.ralinktech.com/ralink/Home/Support/Linux.html
Source0:	http://www.ralinktech.com.tw/data/drivers/%{SourceName}.tar.bz2
Source1:	http://www.ralinktech.com.tw/data/drivers/ReleaseNote-RT2870.txt
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Provides:	%{name}-kmod-common = %{version}
Requires:	%{name}-kmod >= %{version}

%description
This package contains the linux kernel module files for the Ralink rt2870
driver for WiFi, a linux device driver for 802.11a/b/g universal NIC cards -
either PCI, PCIe or MiniPCI - that use Ralink rt2870 chipsets.

%prep
%setup -q -n %{SourceName}
iconv -f JOHAB -t UTF8 %{SOURCE1} -o ./ReleaseNotes
sed -i 's/\r//' ./ReleaseNotes
iconv -f JOHAB -t UTF8 README_STA -o README_STA
sed -i 's/\r//' README_STA

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT2870STA/
install  -p -m 0644 RT2870STA.dat $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT2870STA/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ReleaseNotes README_STA iwpriv_usage.txt
%dir %{_sysconfdir}/Wireless/RT2870STA
%config(noreplace) %{_sysconfdir}/Wireless/RT2870STA/RT2870STA.dat

%changelog
* Tue Oct 07 2008 Orcan Ogetbil  <orcanbahri[AT]yahoo[DOT]com> - 1.4.0.0-1.1
- Install RT2870STA.dat at the "right" place

* Sat Oct 04 2008 Orcan Ogetbil  <orcanbahri[AT]yahoo[DOT]com> - 1.4.0.0-1
- Rebuild for 1.4.0.0
- Added iwpriv_usage.txt into package

* Sat Oct 04 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.3.1.0-4
- Various small adjustments

* Sat Sep 27 2008 Orcan Ogetbil <orcanbahri[AT]yahoo[DOT]com> - 1.3.1.0-3
- Re-wrote the description, removed supported hardware info.
- Fixed the defattr.
- Added the /etc/Wireless/RT2870STA.dat file that comes with the source to the rpm.
- Rename SourceDir to SourceName

* Thu Sep 22 2008 Orcan Ogetbil <orcanbahri[AT]yahoo[DOT]com> - 1.3.1.0-2
- Some cleanup in the SPEC file to match standards
- Fix rpmlint's encoding complaints with doc files
- License is GPLv2+

* Thu Sep 20 2008 Orcan Ogetbil <orcanbahri[AT]yahoo[DOT]com> - 1.3.1.0-1
- Initial build.

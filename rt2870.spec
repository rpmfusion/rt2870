%define SourceName 2009_0424_RT2870_Linux_STA_V2.1.1.0

Name:		rt2870
Version:	2.1.1.0
Release:	1%{?dist}
Summary:	Common files for RaLink rt2870 kernel driver
Group:		System Environment/Kernel
License:	GPLv2+
URL:		http://www.ralinktech.com/ralink/Home/Support/Linux.html
Source0:	http://www.ralinktech.com.tw/data/drivers/%{SourceName}.tgz
Source1:	http://www.ralinktech.com.tw/data/drivers/ReleaseNote-RT2870.txt
Source2:	suspend.sh
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Provides:	%{name}-kmod-common = %{version}
Requires:	%{name}-kmod >= %{version}

%description
This package contains the linux kernel module files for the Ralink rt2870
driver for WiFi, a linux device driver for USB 802.11a/b/g universal NIC cards
that use Ralink rt2870 chipsets.

%prep
%setup -q -n %{SourceName}

# Fix bunch of encoding and permission issues
sed 's|\r||' %{SOURCE1} > ReleaseNotes
touch -r  %{SOURCE1} ReleaseNotes

sed 's|\r||' sta_ate_iwpriv_usage.txt > tmpfile
iconv -f JOHAB -t UTF8 tmpfile -o tmpfile2
touch -r sta_ate_iwpriv_usage.txt tmpfile2
mv -f tmpfile2 sta_ate_iwpriv_usage.txt

iconv -f JOHAB -t UTF8 README_STA > tmpfile
touch -r README_STA tmpfile
mv -f tmpfile README_STA

chmod -x *.txt

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT2870STA/
install -pm 0644 RT2870STA*.dat $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT2870STA/
cp -a %{SOURCE2} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ReleaseNotes README_STA *.txt suspend.sh
%dir %{_sysconfdir}/Wireless
%dir %{_sysconfdir}/Wireless/RT2870STA
%config(noreplace) %{_sysconfdir}/Wireless/RT2870STA/RT2870STA*.dat


%changelog
* Sat Apr 24 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.1.1.0-1
- version update (2.1.1.0)

* Thu Mar 26 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.1.0.0-1
- Rebuild for 2.1.0.0
- Move suspend.sh to %%doc
- Fix description: rt2870 is USB only

* Tue Mar 10 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.0.0-3
- Add suspend script (RPMFusion BZ#199)

* Tue Oct 07 2008 Orcan Ogetbil  <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.0.0-2
- Re-own %%{_sysconfdir}/Wireless/

* Tue Oct 07 2008 Orcan Ogetbil  <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.0.0-1.1
- Install RT2870STA.dat at the "right" place

* Sat Oct 04 2008 Orcan Ogetbil  <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.0.0-1
- Rebuild for 1.4.0.0
- Added iwpriv_usage.txt into package

* Sat Oct 04 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.3.1.0-4
- Various small adjustments

* Sat Sep 27 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.1.0-3
- Re-wrote the description, removed supported hardware info.
- Fixed the defattr.
- Added the /etc/Wireless/RT2870STA.dat file that comes with the source to the rpm.
- Rename SourceDir to SourceName

* Thu Sep 22 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.1.0-2
- Some cleanup in the SPEC file to match standards
- Fix rpmlint's encoding complaints with doc files
- License is GPLv2+

* Thu Sep 20 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.1.0-1
- Initial build.

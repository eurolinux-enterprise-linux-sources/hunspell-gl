Name: hunspell-gl
Summary: Galician hunspell dictionaries
%define upstreamid 20080515
Version: 0.%{upstreamid}
Release: 7%{?dist}
Source: http://openoffice.mancomun.org/libreeengalego/Corrector/gl_ES-pack.zip
Group: Applications/Text
URL: http://wiki.mancomun.org/index.php/Corrector_ortogr%C3%A1fico_para_OpenOffice.org#Descrici.C3.B3n
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2
BuildArch: noarch

Requires: hunspell

%description
Galician hunspell dictionaries.

%prep
%setup -q -c -n hunspell-gl

%build
unzip gl_ES.zip
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_gl_ES.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 16 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080515-1
- latest dictionaries

* Wed Apr 16 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080410-1
- latest dictionaries

* Fri Nov 09 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071107-1
- latest dictionaries

* Tue Aug 21 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070802-1
- latest dictionaries
- clarify license

* Sun May 05 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070504-1
- latest dictionaries

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20061002-1
- initial version

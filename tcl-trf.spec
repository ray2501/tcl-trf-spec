%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tcl-trf
Summary:       Tcl extension providing "transformer" commands
Version:       2.1.4
Release:       1
License:       Tcl and MIT and BSD
Group:         Development/Libraries/Tcl
Source:        trf2.1.4.tar.gz
URL:           http://tcltrf.sourceforge.net
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.4
BuildRequires: zlib-devel
BuildRequires: libbz2-devel
BuildRequires: openssl-devel
Requires:      tcl >= 8.4
Requires:      zlib
Requires:      libbz2-1
Requires:      openssl
BuildRoot:     %{buildroot}

%description
Trf is an extension library to the script language tcl. It provides 
transformer procedures which change the flow of bytes through a channel 
in arbitrary ways. The underlying functionality in the core is that of 
stacked channels which allows code outside of the core to intercept all 
actions (read/write) on a channel.

Among the applications of the above provided here are compression, 
charset recording, error correction, and hash generation.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries/Tcl
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q -n trf%{version} 

%build
rm -rf $RPM_BUILD_ROOT

./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
	--mandir=%{directory}/share/man \
        --with-tcl=%{directory}/%{_lib} \
        --with-zlib-lib-dir=%{directory}/%{_lib} \
        --with-ssl-lib-dir=%{directory}/%{_lib} \
        --with-bz2-lib-dir=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{directory}/%{_lib}/tcl/Trf%{version} install

mv %{buildroot}%{directory}/%{_lib}/tcl/Trf%{version}/libTrfstub2.1.4.a %{buildroot}%{directory}/%{_lib}/tcl/libTrfstub2.1.4.a

%clean
rm -rf %buildroot

%files
%doc doc/license.terms README ChangeLog
%defattr(-,root,root)
%{directory}/%{_lib}/tcl/Trf%{version}
%{directory}/%{_lib}/tcl/Trf%{version}/pkgIndex.tcl
%{directory}/%{_lib}/tcl/Trf%{version}/libTrf2.1.4.so

%files devel
%{directory}/%{_lib}/tcl/libTrfstub2.1.4.a
%{_includedir}/transform.h
%{_includedir}/trfDecls.h

%changelog
* Sat Apr 29 2017 Danilo Chang <ray2501@gmail.com> 2.1.4
- Remove folder patches
- Remove folder zlib.vc
- Remove file painless-guide-to-crc.txt
- Remove file msvcrt.dll
- Update md2 configure
- Remove folder haval and haval.1996, use haval1.1 to replace
- Replace ripemd folder to a free version
- Initial 2.1.4 version, cleanup source code package

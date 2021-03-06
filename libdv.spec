# Note that this is NOT a relocatable package

Summary:   libdv - DV software codec
Name:      libdv
Version:   1.0.0
Release:   1
CopyRight: GPL
Group:     Libraries/Multimedia
Source:    http://download.sourceforge.net/libdv/libdv-1.0.0.tar.gz
URL:       http://libdv.sourceforge.net/
BuildRoot: %{_tmppath}/libdv-1.0.0-root

Packager: Charles 'Buck' Krasic <krasic@acm.org>

%description 

The Quasar DV codec (libdv) is a software codec for DV video.  DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface.  libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M.  See http://libdv.sourceforge.net/ for more.

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README README.encoder AUTHORS NEWS INSTALL TODO COPYRIGHT 
%{_mandir}/man1/playdv.1.gz
%{_mandir}/man1/encodedv.1.gz
%{_mandir}/man1/dubdv.1.gz
%{_mandir}/man1/dvconnect.1.gz
%{_bindir}/playdv
%{_bindir}/encodedv
%{_bindir}/dvconnect
%{_bindir}/dubdv
%{_libdir}/libdv.so*


%package devel
Summary: Libraries, includes and more from libdv
Group: Development/Libraries

%description devel
The Quasar DV codec (libdv) is a software codec for DV video.  DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface.  libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M.  See http://libdv.sourceforge.net/ for more.

This is the libraries, include files and other resources you can use
to incorporate libdv into applications.

%files devel
%defattr(-, root, root)
%doc ChangeLog COPYING README README.encoder AUTHORS NEWS INSTALL TODO COPYRIGHT
%{_includedir}/libdv
%{_libdir}/libdv.a
%{_libdir}/libdv.la
%{_libdir}/pkgconfig/*

%changelog

%prep
%setup -n libdv-1.0.0

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  ./bootstrap
fi

./configure --prefix=${_prefix} --without-debug --mandir=%{_mandir} 
make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

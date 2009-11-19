Summary:	CUE Sheet Parser Library
Name:		libcue
Version:	1.3.0
Release:	1
License:	GPL v2 and BSD-like
Group:		Libraries
Source0:	http://dl.sourceforge.net/libcue/%{name}-%{version}.tar.bz2
# Source0-md5:	afd94427ff1e59f093a1b8b29aea2ecf
URL:		http://libcue.sourceforge.net
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libcue is intended to parse a so called cue sheet from a char string or a file
pointer. For handling of the parsed data a convenient API is available.

This project is meant as a fork of cuetools by Svend Sorensen which saw it last
release in 02/2006. 


%package devel
Summary:	Header files for libcue libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcue libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek libcue.

%package static
Summary:	Static libcue libraries
Summary(pl.UTF-8):	Statyczne biblioteki libcue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcue libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libcue.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS COPYING
%attr(755,root,root) %{_libdir}/libcue.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcue.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcue.so
%{_libdir}/libcue.la
%{_includedir}/libcue-1.3
%{_pkgconfigdir}/libcue.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcue.a

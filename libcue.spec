Summary:	CUE Sheet Parser Library
Summary(pl.UTF-8):	Biblioteka analizująca Cue Sheet
Name:		libcue
Version:	1.4.0
Release:	1
License:	GPL v2, parts BSD-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libcue/%{name}-%{version}.tar.bz2
# Source0-md5:	5f5045f00e6ac92d9a057fe5b0982c69
URL:		http://libcue.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libcue is intended to parse a so called cue sheet (CD tracks layout)
from a char string or a file pointer. For handling of the parsed data
a convenient API is available.

This project is meant as a fork of cuetools by Svend Sorensen which
saw it last release in 02/2006. 

%description -l pl.UTF-8
Biblioteka libcue służy do analizy tzw. "cue sheet" (układu ścieżek
CD) z łańcucha znaków lub pliku. Dostępne jest wygodne API do obsługi
przeanalizowanych danych.

Ten projekt jest odgałęzieniem cuetools Svenda Sorensena, wydanych
po raz ostatni w lutym 2006.

%package devel
Summary:	Header files for libcue library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcue library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcue.

%package static
Summary:	Static libcue library
Summary(pl.UTF-8):	Statyczna biblioteka libcue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcue library.

%description static -l pl.UTF-8
Statyczna biblioteka libcue.

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
%doc AUTHORS COPYING ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libcue.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcue.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcue.so
%{_libdir}/libcue.la
%{_includedir}/libcue-1.4
%{_pkgconfigdir}/libcue.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcue.a

Summary:	CUE Sheet Parser Library
Summary(pl.UTF-8):	Biblioteka analizująca Cue Sheet
Name:		libcue
Version:	2.3.0
Release:	1
License:	GPL v2, parts BSD-like
Group:		Libraries
#Source0Download: https://github.com/lipnitsk/libcue/releases
Source0:	https://github.com/lipnitsk/libcue/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a3daa638ba0bf8581c750e6ea6e82a52
URL:		https://github.com/lipnitsk/libcue
BuildRequires:	bison
BuildRequires:	cmake >= 2.8
BuildRequires:	flex
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
Obsoletes:	libcue-static < 2.1

%description devel
Header files for libcue library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcue.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.md
%attr(755,root,root) %{_libdir}/libcue.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcue.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcue.so
%{_includedir}/libcue.h
%{_includedir}/libcue
%{_pkgconfigdir}/libcue.pc

#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	A C++ interface for sockets
Summary(pl):	Interfejs C++ do gniazd
Name:		socket++
Version:	1.12.12
Release:	1
License:	Freely Distributable
Vendor:		Gnanasekaran Swaminathan
Group:		Libraries
Source0:	http://www.linuxhacker.at/linux/downloads/src/%{name}-%{version}.tar.gz
# Source0-md5:	b96e06129504ae2b4005a5834264c5a4
Patch0:		%{name}-%{version}-p1.patch
Patch1:		%{name}-info.patch
URL:		http://www.linuxhacker.at/socketxx/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Socket++ library defines a family of C++ classes that can be used more
effectively than directly calling the underlying low-level system
functions. One distinct advantage of the socket++ is that it has the
same interface as that of the iostream so that the users can perform
type-safe input output.

This is a modified version of the original socket++ 1.11 Library.

%description -l pl
Socket++ jest bibliotek± definiuj±c± rodzinê klas C++, która mo¿e w
sposób bardziej efektywny obs³ugiwaæ gniazda ni¿ bezpo¶rednie
odwo³ania do le¿±cego ni¿ej podsystemu gniazd. Jedn± z wiêkszych zalet
socket++ jest to, ¿e u¿ywa on tego samego interfejsu co klasa
iostream, tak wiêc mo¿na wykonywaæ na niej operacje wej¶cia/wyj¶cia z
kontrol± typów.

To jest zmodyfikowana wersja oryginalnej biblioteki socket++ 1.11.

%package devel
Summary:	socket++ development files
Summary(pl):	Pliki dla deweloperów programów korzystaj±cych z socket++
Group:		Development/Libraries
Requires:	%{name} = :%{version}-%{release}

%description devel
socket++ development files.

%description devel -l pl
Pliki dla deweloperów programów korzystaj±cych z socket++.

%package static
Summary:	socket++ static library
Summary(pl):	Biblioteka statyczna socket++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
socket++ static library.

%description static -l pl
Biblioteka statyczna socket++ .

%package doc-info
Summary:	socket++ info documentation
Summary(pl):	dokumentacja info socket++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description doc-info
socket++ info documentation

%description doc-info -l pl
Dokumentacja info socket++

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--enable-static=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post doc-info
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun doc-info
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README* THANKS
%{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%files doc-info
%defattr(644,root,root,755)
%{_infodir}/*.info*

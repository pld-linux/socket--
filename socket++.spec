Name:		socket++
Summary:	A C++ interface for sockets.
Version:	1.12.10
Release:	1
License:	Freely Distributable
Group:		Development/Libraries
Source0:	http://www.hstraub.at/linux/downloads/src/%{name}-%{version}.tar.gz
# Source0-md5:	1636c25b9192bf92c3b0dcb69c907f2a
Vendor:		Gnanasekaran Swaminathan
URL:		http://members.aon.at/hstraub/linux/socket++/
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Socket++ library defines a family of C++ classes that can be used more
effectively than directly calling the underlying low-level system
functions. One distinct advantage of the socket++ is that it has the
same interface as that of the iostream so that the users can perform
type-safe input output.

This is a modified version of the original socket++ 1.11 Library

%description -l pl
Socket++ jest biblotek± definuj±c± rodzinê klas C++ która mo¿e w
sposób bardziej efektywny obs³ugiwaæ gniazda ni¿ bezpo¶rednie
odwo³ania do le¿±cego ni¿ej podsystemu gniazd. Jedn± z wiêkszych zalet
socket++ jest to ¿e u¿wa on tego samego interfejsu co klasa iostream,
tak wiêc mo¿na wykonywaæ na niej [type-safe(?)] wej¶cie/wyj¶cie.

To jest zmodyfikowana wersja oryginalnej bibloteki socket++ 1.11 

%package devel
Summary:	socket++ development files
Summary(pl):	Pliki dla deweloperów programów korzystaj±cych z socket++ 
Group:		Development/Libraries
Requires:	%{name} = :%{version}-%{release}

%description devel
socket++ development files.

%description devel -l pl
Pliki dla deweloperów programów korzystaj±cych z socket++ .

%package static
Summary:	socket++ static library
Summary(pl):	Biblioteki statyczna socket++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
socket++ static library.

%description static -l pl
Biblioteka statyczna socket++ .

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

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
#/sbin/install-info %{_infodir}/socket++.info.gz %{_infodir}/dir

%preun
if [ "$1" = 0 ]; then
  /sbin/install-info --delete %{_infodir}/socket++.info.gz %{_infodir}/dir
fi

%postun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_libdir}/lib*.so.*.*.*
%{_infodir}/*
%doc COPYING README* ChangeLog AUTHORS THANKS NEWS

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

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

%prep
%setup -q
%build
#%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
[ "$RPM_BUILD_ROOT" != "" ] && rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
[ "$RPM_BUILD_ROOT" != "" ] && rm -rf $RPM_BUILD_ROOT

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
%{_includedir}/socket++/*
%{_libdir}/*
%{_infodir}/*
%doc COPYING README* ChangeLog AUTHORS THANKS NEWS

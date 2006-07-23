Summary:	The f2c Fortran to C conversion library
Summary(pl):	Biblioteka f2c do t³umaczenia z Fortranu na C
Name:		libf2c
Version:	20051005
Release:	1
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.netlib.org/f2c/libf2c.zip
# Source0-md5:	b9ee5e6e0a2aabd2e9f3df718ecdfbec
Patch0:		%{name}-LP64.patch
Patch1:		%{name}-opt.patch
URL:		ftp://ftp.netlib.org/f2c/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The f2c Fortran to C conversion library.

%description -l pl
Biblioteka f2c do t³umaczenia z Fortranu na C.

%package devel
Summary:	Header file for f2c library
Summary(pl):	Plik nag³ówkowy biblioteki f2c
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for f2c library.

%description devel -l pl
Plik nag³ówkowy biblioteki f2c.

%package static
Summary:	Static f2c library
Summary(pl):	Statyczna biblioteka f2c
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static f2c library.

%description static -l pl
Statyczna biblioteka f2c.

%prep
%setup -q -n libf2c
%patch0 -p1
%patch1 -p1

%build
%{__make} -f makefile.u \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%{__cc} -shared -o libf2c.so.0.23 *.o -Wl,-soname=libf2c.so.0 -lm
rm -f libf2c.a *.o

%{__make} -f makefile.u \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install libf2c.so.0.23 $RPM_BUILD_ROOT%{_libdir}
ln -sf libf2c.so.0.23 $RPM_BUILD_ROOT%{_libdir}/libf2c.so
install libf2c.a $RPM_BUILD_ROOT%{_libdir}
install f2c.h $RPM_BUILD_ROOT%{_includedir}
 
%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Notice README
%attr(755,root,root) %{_libdir}/libf2c.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libf2c.so
%{_includedir}/f2c.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libf2c.a

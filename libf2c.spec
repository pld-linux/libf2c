Summary:	Fortran to C conversion support library
Summary(pl.UTF-8):	Biblioteka wspierająca tłumaczenie z Fortranu na C
Name:		libf2c
Version:	20051005
Release:	2
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.netlib.org/f2c/libf2c.zip
# Source0-md5:	b9ee5e6e0a2aabd2e9f3df718ecdfbec
Patch0:		%{name}-LP64.patch
Patch1:		%{name}-opt.patch
URL:		ftp://ftp.netlib.org/f2c/
BuildRequires:	unzip
Conflicts:	f2c < 20031027-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library of support routines used by f2c Fortran to C converter.

%description -l pl.UTF-8
Biblioteka funkcji wspierających wykorzystywana przez konwerter
z Fortranu do C f2c.

%package devel
Summary:	Header file for f2c library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki f2c
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for f2c library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki f2c.

%package static
Summary:	Static f2c library
Summary(pl.UTF-8):	Statyczna biblioteka f2c
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static f2c library.

%description static -l pl.UTF-8
Statyczna biblioteka f2c.

%prep
%setup -q -n libf2c
%patch0 -p1
%patch1 -p1

%build
%{__make} -f makefile.u \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

ar crs libf2cmain.a main.o getarg_.o iargc_.o
%{__rm} main.o getarg_.o iargc_.o
%{__cc} -shared -o libf2c.so.0.23 *.o -Wl,-soname=libf2c.so.0 -lm
%{__rm} libf2c.a *.o

%{__make} -f makefile.u \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install libf2c.so.0.23 $RPM_BUILD_ROOT%{_libdir}
ln -sf libf2c.so.0.23 $RPM_BUILD_ROOT%{_libdir}/libf2c.so.0
ln -sf libf2c.so.0.23 $RPM_BUILD_ROOT%{_libdir}/libf2c.so
install libf2c.a libf2cmain.a $RPM_BUILD_ROOT%{_libdir}
install f2c.h $RPM_BUILD_ROOT%{_includedir}
 
%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Notice README
%attr(755,root,root) %{_libdir}/libf2c.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libf2c.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libf2c.so
%{_libdir}/libf2cmain.a
%{_includedir}/f2c.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libf2c.a

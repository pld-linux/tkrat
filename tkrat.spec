Summary:	A Tcl/Tk Mail User Agent
Summary(pl.UTF-8):   Program pocztowy z interfejsem Tcl/Tk
Name:		tkrat
Version:	2.0.3
Release:	1
License:	BSD
Group:		X11/Applications/Networking
Source0:	http://www.tkrat.org/downloads/stable/%{name}-%{version}.tar.gz
# Source0-md5:	484f46b21af62705cb8948c821c8bfdb
Patch0:		%{name}-ac.patch
URL:		http://www.tkrat.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
TkRat is a modern Mail User Agent tkat speaks MIME. It has an inteface
built in Tcl/Tk and kernel written in C. Also features POP, IMAP and
pgp support.

%description -l pl.UTF-8
TkRat jest nowoczesnym programem pocztowym znającym MIME. Jego
interfejs jest zbudowany w Tcl/Tk, a jądro napisane in C. TkRat może
być klientem POP oraz IMAP, wykorzystuje też pgp/GnuPg.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure2_13 \
	--with-install-prefix=$RPM_BUILD_ROOT

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BLURB CONFIGURATION COPYRIGHT README
%doc doc/{changes,interface,userproc.example,userprocs}
%attr(755,root,root) %{_bindir}/tkrat
%{_libdir}/tkrat2.0
%{_datadir}/tkrat2.0
%{_mandir}/*/*

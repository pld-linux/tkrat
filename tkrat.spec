Summary:	A Tcl/Tk Mail User Agent.
Summary(pl):	Program pocztowy z interfejsem Tcl/Tk.
Name:		tkrat
Version:	2.0.2
Release:	1
Source0:	http://www.tkrat.org/downloads/stable/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac.patch
Copyright:	BSD
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Requires:	tk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define %{_prefix}		/usr/X11R6

%description 
TkRat is a modern Mail User Agent tkat speaks MIME. It has an inteface
built in Tcl/Tk and kernel written in C. Also features POP, IMAP and
pgp support.

%description 
TkRat jest nwoczesnym programem pocztowym znaj�cym MIME. Jego
interfejs jest zbudowany w Tcl/Tk, a j�dro napisane in C. TkRat
mo�e by� klientem POP oraz IMAP, wykorzystuje te� pgp/GnuPg.


%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
%configure2_13 \
	--with-install-prefix=$RPM_BUILD_ROOT

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

gzip -9nf BLURB CONFIGURATION COPYRIGHT README
gzip -9nf doc/{changes,interface,userproc.example,userprocs}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc doc/*.gz
%attr(755,root,root) %{_bindir}/tkrat
%{_libdir}/tkrat2.0
%{_datadir}/tkrat2.0
%{_mandir}/*/*
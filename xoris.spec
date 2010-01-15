Summary:	xoris grabs the RGB color value of any pixel on the screen and dumps the color's name
Name:		xoris
Version:	0.1e
Release:	0.1
License:	MIT
Group:		Applications
Source0:	http://dl.sourceforge.net/xoris/%{name}-%{version}.tar.gz
# Source0-md5:	f1e8abbb5e57f66f52335a37f5405207
URL:		http://sourceforge.net/projects/xoris/
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xoris grabs the RGB color value of any pixel on the screen and dumps
the color's name to stdout.

%prep
%setup -q

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*

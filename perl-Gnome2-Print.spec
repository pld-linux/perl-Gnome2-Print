#
# Conditional build:
%bcond_with tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2-Print
Summary:	Perl interface to the GNOME Print libraries
Summary(pl):	Interfejs perlowy do bibliotek GNOME Print
Name:		perl-Gnome2-Print
Version:	0.94
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	03f8830f963da7985f4ab0796cdcfa89
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeprintui-devel >= 2.2
BuildRequires:	perl-Glib >= 1.020
BuildRequires:	perl-Gnome2
BuildRequires:	perl-Gtk2 >= 1.021
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.020
Requires:	perl-Gtk2 >= 1.021
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gnome2::Print Perl module allows a Perl developer to use the GNOME
Printing libraries with Gtk2-perl.

%description -l pl
Modu³ Perla Gnome2::Print umo¿liwia programistom perlowym korzystanie
z bibliotek GNOME Print wraz z Gtk2-perl.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Gnome2/Print.pm
%dir %{perl_vendorarch}/Gnome2/Print
%{perl_vendorarch}/Gnome2/Print/Font
%{perl_vendorarch}/Gnome2/Print/Install
%dir %{perl_vendorarch}/auto/Gnome2/Print
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Print/*.so
%{perl_vendorarch}/auto/Gnome2/Print/*.bs
%{_mandir}/man3/*

#
# Conditional build:
%bcond_with tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2-Print
Summary:	Perl interface to the Gnome Print libraries
Summary(pl):	Interfejs perlowy do bibliotek Gnome Print
Name:		perl-%{pnam}
Version:	0.91
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	6ad6f04f1db66291e89c081093689292
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
The Gnome2 Perl module allows a perl developer to use the Gnome
Printing libraries with Gtk2-perl.

%description -l pl
Modu³ Perla Gnome2 umo¿liwia programistom perlowym korzystanie z
bibliotek Gnome Print wraz z Gtk2-perl.

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
%dir %{perl_vendorarch}/auto/Gnome2/Print
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Print/*.so
%{perl_vendorarch}/auto/Gnome2/Print/*.bs
%{perl_vendorarch}/Gnome2/Print
%{_mandir}/man3/*

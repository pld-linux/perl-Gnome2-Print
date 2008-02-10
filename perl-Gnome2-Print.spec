#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Gnome2-Print
Summary:	Perl interface to the GNOME Print libraries
Summary(pl.UTF-8):	Interfejs perlowy do bibliotek GNOME Print
Name:		perl-Gnome2-Print
Version:	1.000
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	66578c2ffaebbe035a0735e65ad71c3f
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	perl-ExtUtils-Depends >= 0.1
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.120
BuildRequires:	perl-Gtk2 >= 1.120
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	libgnomeprintui >= 2.2.0
Requires:	perl-Glib >= 1.120
Requires:	perl-Gtk2 >= 1.120
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gnome2::Print Perl module allows a Perl developer to use the GNOME
Printing libraries with Gtk2-perl.

%description -l pl.UTF-8
Moduł Perla Gnome2::Print umożliwia programistom perlowym korzystanie
z bibliotek GNOME Print wraz z Gtk2-perl.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Print/{,*/}*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{perl_vendorarch}/Gnome2/Print.pm
%dir %{perl_vendorarch}/Gnome2/Print
%{perl_vendorarch}/Gnome2/Print/Config
%{perl_vendorarch}/Gnome2/Print/Font
%{perl_vendorarch}/Gnome2/Print/Install
%dir %{perl_vendorarch}/auto/Gnome2/Print
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Print/*.so
%{perl_vendorarch}/auto/Gnome2/Print/*.bs
%{_mandir}/man3/*

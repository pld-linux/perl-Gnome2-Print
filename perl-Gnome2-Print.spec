#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pnam	Gnome2-Print
Summary:	Perl interface to the GNOME Print libraries
Summary(pl.UTF-8):	Interfejs perlowy do bibliotek GNOME Print
Name:		perl-Gnome2-Print
Version:	1.001
Release:	5
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	67ae821c4b7cb9046513a3944cd37e9b
Patch0:		perl-5.36.patch
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	perl-ExtUtils-Depends >= 0.1
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib-devel >= 1.120
BuildRequires:	perl-Gtk2-devel >= 1.120
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	libgnomeprintui >= 2.2.0
Requires:	perl-Glib >= 1.120
Requires:	perl-Gtk2 >= 1.120
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gnome2::Print Perl module allows a Perl developer to use the GNOME
Printing libraries with Gtk2-perl.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Moduł Perla Gnome2::Print umożliwia programistom perlowym korzystanie
z bibliotek GNOME Print wraz z Gtk2-perl.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl Gnome2-Print bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gnome2-Print dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	libgnomeprintui-devel >= 2.2.0
Requires:	perl-Cairo-devel
Requires:	perl-Glib-devel >= 1.120
Requires:	perl-Gtk2-devel >= 1.120

%description devel
Development files for Perl Gnome2-Print bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gnome2-Print dla Perla.

%prep
%setup -q -n %{pnam}-%{version}
%patch -P0 -p1

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Print/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{perl_vendorarch}/Gnome2/Print.pm
%dir %{perl_vendorarch}/Gnome2/Print
%{perl_vendorarch}/Gnome2/Print/Config
%{perl_vendorarch}/Gnome2/Print/Font
%dir %{perl_vendorarch}/auto/Gnome2/Print
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Print/Print.so
%{_mandir}/man3/Gnome2::Print*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome2/Print/Install

%define upstream_name    Padre-Plugin-Ecliptic
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Padre plugin that provides Eclipse-like useful features
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(ExtUtils::Install)
BuildRequires:	perl(File::Which)
BuildRequires:	perl(Locale::Msgfmt)
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Once you enable this Plugin under Padre, you'll get a brand new menu with
the following options:

Open Resource (Shortcut: Ctrl + Shift + R)
    This opens a nice dialog that allows you to find any file that exists
    in the current document or working directory. You can use ? to replace
    a single character or * to replace an entire string. The matched files
    list are sorted alphabetically and you can select one or more files to
    be opened in Padre when you press the OK button.

    You can simply ignore CVS, .svn and .git folders using a simple
    checkbox (enhancement over Eclipse).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.230.0-2mdv2011.0
+ Revision: 656951
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 623001
- new version

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2011.0
+ Revision: 480733
- update to 0.19

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 420889
- update to 0.18

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 418120
- update to 0.17

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-2mdv2010.0
+ Revision: 408650
- force rebuild
- update to 0.16

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 399771
- import perl-Padre-Plugin-Ecliptic


* Sat Jul 25 2009 cpan2dist 0.15-1mdv
- initial mdv release, generated with cpan2dist

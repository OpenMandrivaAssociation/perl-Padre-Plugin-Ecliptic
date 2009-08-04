%define upstream_name    Padre-Plugin-Ecliptic
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Padre plugin that provides Eclipse-like useful features
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::XSAccessor)
BuildRequires: perl(ExtUtils::Install)
BuildRequires: perl(File::Which)
BuildRequires: perl(Locale::Msgfmt)
BuildRequires: perl(Padre)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*

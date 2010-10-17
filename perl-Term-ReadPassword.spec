%define upstream_name    Term-ReadPassword
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Asking the user for a password
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module lets you ask the user for a password in the traditional way,
from the keyboard, without echoing.

This is not intended for use over the web; user authentication over the web
is another matter entirely. Also, this module should generally be used in
conjunction with Perl's *crypt()* function, sold separately.

The *read_password* function prompts for input, reads a line of text from
the keyboard, then returns that line to the caller. The line of text
doesn't include the newline character, so there's no need to use *chomp*.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

# Commenting-out because it's interactive.
# %check
# %make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*



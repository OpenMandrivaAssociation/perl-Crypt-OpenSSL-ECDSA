%define upstream_name    Crypt-OpenSSL-ECDSA
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Perl extension for OpenSSL ECDSA (Elliptic Curve Digital Signature Algorithm)
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Crypt::OpenSSL::Bignum)
BuildRequires: perl(Crypt::OpenSSL::EC)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-devel
BuildRequires: pkgconfig(libssl)



%description
This module provides an interface to the ECDSA (Elliptic Curve Digital
Signature Algorithm) functions in OpenSSL

Tested against OpenSSL 1.0.2

Export
    None by default.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*


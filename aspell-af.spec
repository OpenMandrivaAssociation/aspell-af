%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-0
%define languageenglazy Afrikaans
%define languagecode af
%define lc_ctype af_ZA

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50_0
Release:	1
Group:		System/Internationalization
License:	LGPL
Provides:	spell-%{languagecode}
Url:		https://aspell.net/
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
# old ispell is replaced with aspell
Obsoletes:	ispell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{name}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%files
%doc README.%{languagecode} Copyright doc/*
%{_libdir}/aspell-*/*


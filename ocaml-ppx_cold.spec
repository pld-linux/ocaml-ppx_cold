#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Expand @cold into @inline/@specialise/@local never
Summary(pl.UTF-8):	Rozwijanie @cold do @inline/@specialise/@local never
Name:		ocaml-ppx_cold
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_cold/tags
Source0:	https://github.com/janestreet/ppx_cold/archive/v%{version}/ppx_cold-%{version}.tar.gz
# Source0-md5:	c19f765e076c13c3c22a256557fa26a5
URL:		https://github.com/janestreet/ppx_cold
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
ppx_cold translates @cold attributes to @inline/@local/@specialise
never.

This package contains files needed to run bytecode executables using
ppx_cold library.

%description -l pl.UTF-8
ppx_cold tłumaczy atrybuty @cold na @inline/@local/@specialise never.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_cold.

%package devel
Summary:	Expand @cold into @inline/@specialise/@local never - development part
Summary(pl.UTF-8):	Rozwijanie @cold do @inline/@specialise/@local never - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_cold library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_cold.

%prep
%setup -q -n ppx_cold-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_cold/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_cold

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_cold
%attr(755,root,root) %{_libdir}/ocaml/ppx_cold/ppx.exe
%{_libdir}/ocaml/ppx_cold/META
%{_libdir}/ocaml/ppx_cold/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_cold/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_cold/*.cmi
%{_libdir}/ocaml/ppx_cold/*.cmt
%{_libdir}/ocaml/ppx_cold/*.cmti
%{_libdir}/ocaml/ppx_cold/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_cold/ppx_cold.a
%{_libdir}/ocaml/ppx_cold/*.cmx
%{_libdir}/ocaml/ppx_cold/*.cmxa
%endif
%{_libdir}/ocaml/ppx_cold/dune-package
%{_libdir}/ocaml/ppx_cold/opam

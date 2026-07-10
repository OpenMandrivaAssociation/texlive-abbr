%global tl_name abbr
%global tl_revision 77161

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Simple macros supporting abbreviations for Plain and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/abbr
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abbr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abbr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides some simple macros to support abbreviations in
Plain TeX or LaTeX. It allows writing (e.g.) \<TEX> instead of \TeX,
hence frees users from having to escape space after parameterless
macros.


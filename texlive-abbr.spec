Name:		texlive-abbr
Version:	15878
Release:	2
Summary:	Simple macros supporting abreviations for Plain and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/abbr
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abbr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abbr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Abbr is a set of some simple macros to support abbreviations in
Plain or LaTeX. It allows writing e.g. \<TEX> instead of \TeX,
hence frees users from having to escape space after
parameterless macros.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/abbr/abbr.tex
%doc %{_texmfdistdir}/doc/generic/abbr/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

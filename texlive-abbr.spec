# revision 15878
# category Package
# catalog-ctan /macros/generic/abbr
# catalog-date 2007-05-25 16:15:27 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-abbr
Version:	20070525
Release:	1
Summary:	Simple macros supporting abreviations for Plain and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/abbr
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abbr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abbr.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Abbr is a set of some simple macros to support abbreviations in
Plain or LaTeX. It allows writing e.g. \<TEX> instead of \TeX,
hence frees users from having to escape space after
parameterless macros.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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

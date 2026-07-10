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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides some simple macros to support abbreviations in
Plain TeX or LaTeX. It allows writing (e.g.) \<TEX> instead of \TeX,
hence frees users from having to escape space after parameterless
macros.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/abbr
%dir %{_datadir}/texmf-dist/tex/generic/abbr
%doc %{_datadir}/texmf-dist/doc/generic/abbr/README
%{_datadir}/texmf-dist/tex/generic/abbr/abbr.tex

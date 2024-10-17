Name:		texlive-shtthesis
Version:	62441
Release:	2
Summary:	An unofficial LaTeX thesis template for ShanghaiTech University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/shtthesis
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shtthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shtthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package, forked from ucasthesis, is an unofficial LaTeX
thesis template for ShanghaiTech University and satisfies all
format requirements of the school. The user just needs to set
\documentclass{shtthesis} and to set up mandatory information
via \shtsetup, then his or her thesis document will be typeset
properly.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/shtthesis
%doc %{_texmfdistdir}/doc/latex/shtthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

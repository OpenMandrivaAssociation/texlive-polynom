Name:		texlive-polynom
Version:	44832
Release:	2
Summary:	Macros for manipulating polynomials
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/polynom
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The polynom package implements macros for manipulating
polynomials, for example it can typeset long polynomial
divisions. The main test case and application is the polynomial
ring in one variable with rational coefficients.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/polynom/polynom.sty
%doc %{_texmfdistdir}/doc/latex/polynom/README
%doc %{_texmfdistdir}/doc/latex/polynom/polydemo.pdf
%doc %{_texmfdistdir}/doc/latex/polynom/polydemo.tex
%doc %{_texmfdistdir}/doc/latex/polynom/polynom.pdf
#- source
%doc %{_texmfdistdir}/source/latex/polynom/polynom.dtx
%doc %{_texmfdistdir}/source/latex/polynom/polynom.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

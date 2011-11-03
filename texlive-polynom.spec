Name:		texlive-polynom
Version:	0.17
Release:	1
Summary:	Macros for manipulating polynomials
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/polynom
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The polynom package implements macros for manipulating
polynomials, for example it can typeset long polynomial
divisions. The main test case and application is the polynomial
ring in one variable with rational coefficients.

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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

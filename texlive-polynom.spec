# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/polynom
# catalog-date 2007-01-13 23:45:25 +0100
# catalog-license lppl
# catalog-version 0.17
Name:		texlive-polynom
Version:	0.17
Release:	3
Summary:	Macros for manipulating polynomials
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/polynom
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.17-2
+ Revision: 755020
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.17-1
+ Revision: 719285
- texlive-polynom
- texlive-polynom
- texlive-polynom
- texlive-polynom


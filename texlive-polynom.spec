%global tl_name polynom
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.19
Release:	%{tl_revision}.1
Summary:	Macros for manipulating polynomials
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/polynom
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polynom.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The polynom package implements macros for manipulating polynomials, for
example it can typeset long polynomial divisions. The main test case and
application is the polynomial ring in one variable with rational
coefficients.


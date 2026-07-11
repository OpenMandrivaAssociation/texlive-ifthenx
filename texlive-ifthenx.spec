%global tl_name ifthenx
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1a
Release:	%{tl_revision}.1
Summary:	Extra tests for \ifthenelse
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ifthenx
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifthenx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifthenx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends the ifthen package, providing extra predicates for
the package's \ifthenelse command. The package is complementary to
xifthen, in that they provide different facilities; the two may be
loaded in the same document, as long as xifthen is loaded first.


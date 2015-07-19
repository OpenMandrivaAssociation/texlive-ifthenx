# revision 25819
# category Package
# catalog-ctan /macros/latex/contrib/ifthenx
# catalog-date 2012-04-01 23:59:58 +0200
# catalog-license lppl
# catalog-version 0.1a
Name:		texlive-ifthenx
Version:	0.1a
Release:	9
Summary:	Extra tests for \ifthenelse
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifthenx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifthenx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifthenx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends the ifthen package, providing extra
predicates for the package's \ifthenelse command. The package
is complementary to xifthen, in that they provide different
facilities; the two may be loaded in the same document, as long
as xifthen is loaded first.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ifthenx/ifthenx.sty
%doc %{_texmfdistdir}/doc/latex/ifthenx/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1a-1
+ Revision: 790625
- Import texlive-ifthenx
- Import texlive-ifthenx


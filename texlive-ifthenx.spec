Name:		texlive-ifthenx
Version:	25819
Release:	2
Summary:	Extra tests for \ifthenelse
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ifthenx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifthenx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifthenx.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

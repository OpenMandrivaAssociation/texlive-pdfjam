Name:		texlive-pdfjam
Version:	67088
Release:	1
Summary:	Shell scripts interfacing to pdfpages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/pdfjam
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfjam.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfjam.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-pdfjam.bin = %{EVRD}
%rename pdfjam

%description
This is a collection of shell scripts which provide an
interface to the pdfpages LaTeX package. They do such jobs as
selecting pages, concatenating files, doing n-up formatting,
and so on.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/pdf180
%{_bindir}/pdf270
%{_bindir}/pdf90
%{_bindir}/pdfbook
%{_bindir}/pdfflip
%{_bindir}/pdfjam
%{_bindir}/pdfjam-pocketmod
%{_bindir}/pdfjam-slides3up
%{_bindir}/pdfjam-slides6up
%{_bindir}/pdfjoin
%{_bindir}/pdfnup
%{_bindir}/pdfpun
%{_texmfdistdir}/scripts/pdfjam
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/support/pdfjam

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdf180 pdf180
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdf270 pdf270
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdf90 pdf90
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdfbook pdfbook
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdfflip pdfflip
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdfjam pdfjam
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdfjam-pocketmod pdfjam-pocketmod
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdfjam-slides3up pdfjam-slides3up
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdfjam-slides6up pdfjam-slides6up
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdfjoin pdfjoin
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdfnup pdfnup
ln -sf %{_texmfdistdir}/scripts/pdfjam/pdfpun pdfpun
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1

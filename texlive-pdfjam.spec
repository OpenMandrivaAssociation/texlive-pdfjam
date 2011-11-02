Name:		texlive-pdfjam
Version:	2.02
Release:	1
Summary:	Shell scripts interfacing to pdfpages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/pdfjam
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfjam.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfjam.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-pdfjam.bin = %{EVRD}
Provides:	pdfjam = %{version}
Obsoletes:	pdfjam <= 1.21
Conflicts:	pdfjam <= 1.21
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a collection of shell scripts which provide an
interface to the pdfpages LaTeX package. They do such jobs as
selecting pages, concatenating files, doing n-up formatting,
and so on.

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
%{_texmfdistdir}/scripts/pdfjam/pdf180
%{_texmfdistdir}/scripts/pdfjam/pdf270
%{_texmfdistdir}/scripts/pdfjam/pdf90
%{_texmfdistdir}/scripts/pdfjam/pdfbook
%{_texmfdistdir}/scripts/pdfjam/pdfflip
%{_texmfdistdir}/scripts/pdfjam/pdfjam
%{_texmfdistdir}/scripts/pdfjam/pdfjam-pocketmod
%{_texmfdistdir}/scripts/pdfjam/pdfjam-slides3up
%{_texmfdistdir}/scripts/pdfjam/pdfjam-slides6up
%{_texmfdistdir}/scripts/pdfjam/pdfjoin
%{_texmfdistdir}/scripts/pdfjam/pdfnup
%{_texmfdistdir}/scripts/pdfjam/pdfpun
%doc %{_texmfdistdir}/doc/support/pdfjam/COPYING
%doc %{_texmfdistdir}/doc/support/pdfjam/PDFjam-README.html
%doc %{_texmfdistdir}/doc/support/pdfjam/VERSION
%doc %{_texmfdistdir}/doc/support/pdfjam/pdfdroplets.png
%doc %{_texmfdistdir}/doc/support/pdfjam/pdfjam.conf
%doc %{_texmfdistdir}/doc/support/pdfjam/tests.zip
%doc %{_mandir}/man1/pdf180.1*
%doc %{_texmfdir}/doc/man/man1/pdf180.man1.pdf
%doc %{_mandir}/man1/pdf270.1*
%doc %{_texmfdir}/doc/man/man1/pdf270.man1.pdf
%doc %{_mandir}/man1/pdf90.1*
%doc %{_texmfdir}/doc/man/man1/pdf90.man1.pdf
%doc %{_mandir}/man1/pdfbook.1*
%doc %{_texmfdir}/doc/man/man1/pdfbook.man1.pdf
%doc %{_mandir}/man1/pdfflip.1*
%doc %{_texmfdir}/doc/man/man1/pdfflip.man1.pdf
%doc %{_mandir}/man1/pdfjam-pocketmod.1*
%doc %{_texmfdir}/doc/man/man1/pdfjam-pocketmod.man1.pdf
%doc %{_mandir}/man1/pdfjam-slides3up.1*
%doc %{_texmfdir}/doc/man/man1/pdfjam-slides3up.man1.pdf
%doc %{_mandir}/man1/pdfjam-slides6up.1*
%doc %{_texmfdir}/doc/man/man1/pdfjam-slides6up.man1.pdf
%doc %{_mandir}/man1/pdfjam.1*
%doc %{_texmfdir}/doc/man/man1/pdfjam.man1.pdf
%doc %{_mandir}/man1/pdfjoin.1*
%doc %{_texmfdir}/doc/man/man1/pdfjoin.man1.pdf
%doc %{_mandir}/man1/pdfnup.1*
%doc %{_texmfdir}/doc/man/man1/pdfnup.man1.pdf
%doc %{_mandir}/man1/pdfpun.1*
%doc %{_texmfdir}/doc/man/man1/pdfpun.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

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
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1

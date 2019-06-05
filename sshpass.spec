#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sshpass
Version  : 1.06
Release  : 2
URL      : http://http.debian.net/debian/pool/main/s/sshpass/sshpass_1.06.orig.tar.gz
Source0  : http://http.debian.net/debian/pool/main/s/sshpass/sshpass_1.06.orig.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: sshpass-bin
Requires: sshpass-license
Requires: sshpass-man

%description


%package bin
Summary: bin components for the sshpass package.
Group: Binaries
Requires: sshpass-license
Requires: sshpass-man

%description bin
bin components for the sshpass package.


%package license
Summary: license components for the sshpass package.
Group: Default

%description license
license components for the sshpass package.


%package man
Summary: man components for the sshpass package.
Group: Default

%description man
man components for the sshpass package.


%prep
%setup -q -n sshpass-1.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536894435
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536894435
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/sshpass
cp COPYING %{buildroot}/usr/share/doc/sshpass/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sshpass

%files license
%defattr(-,root,root,-)
/usr/share/doc/sshpass/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/sshpass.1

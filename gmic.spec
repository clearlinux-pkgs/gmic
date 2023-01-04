#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gmic
Version  : 2.8.4
Release  : 34
URL      : https://gmic.eu/files/source/gmic_2.8.4.tar.gz
Source0  : https://gmic.eu/files/source/gmic_2.8.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CECILL-1.0 CECILL-1.1 CECILL-2.0 GPL-3.0
Requires: gmic-bin = %{version}-%{release}
Requires: gmic-filemap = %{version}-%{release}
Requires: gmic-lib = %{version}-%{release}
Requires: gmic-license = %{version}-%{release}
Requires: gmic-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : gimp-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : openexr-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(opencv)
BuildRequires : qttools-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

%package bin
Summary: bin components for the gmic package.
Group: Binaries
Requires: gmic-license = %{version}-%{release}
Requires: gmic-filemap = %{version}-%{release}

%description bin
bin components for the gmic package.


%package dev
Summary: dev components for the gmic package.
Group: Development
Requires: gmic-lib = %{version}-%{release}
Requires: gmic-bin = %{version}-%{release}
Provides: gmic-devel = %{version}-%{release}
Requires: gmic = %{version}-%{release}

%description dev
dev components for the gmic package.


%package filemap
Summary: filemap components for the gmic package.
Group: Default

%description filemap
filemap components for the gmic package.


%package lib
Summary: lib components for the gmic package.
Group: Libraries
Requires: gmic-license = %{version}-%{release}
Requires: gmic-filemap = %{version}-%{release}

%description lib
lib components for the gmic package.


%package license
Summary: license components for the gmic package.
Group: Default

%description license
license components for the gmic package.


%package man
Summary: man components for the gmic package.
Group: Default

%description man
man components for the gmic package.


%package staticdev
Summary: staticdev components for the gmic package.
Group: Default
Requires: gmic-dev = %{version}-%{release}

%description staticdev
staticdev components for the gmic package.


%prep
%setup -q -n gmic-2.8.4
cd %{_builddir}/gmic-2.8.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672869197
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake .. -DENABLE_TIFF=OFF
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DENABLE_TIFF=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1672869197
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gmic
cp %{_builddir}/gmic-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gmic/e48dd1d9bcb69a8b411bdcffcb04012d4b02e9e4 || :
cp %{_builddir}/gmic-%{version}/gmic-qt/COPYING %{buildroot}/usr/share/package-licenses/gmic/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/gmic-%{version}/gmic-qt/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/gmic/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/gmic-%{version}/zart/Licence_CeCILL_V2-en.html %{buildroot}/usr/share/package-licenses/gmic/5e489eefae18f5cc77435302ef0d9d04fac672f1 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gmic
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/gmic.h
/usr/lib64/cmake/gmic/GmicConfig.cmake
/usr/lib64/cmake/gmic/GmicTargets-relwithdebinfo.cmake
/usr/lib64/cmake/gmic/GmicTargets.cmake
/usr/lib64/glibc-hwcaps/x86-64-v3/libgmic.so
/usr/lib64/libgmic.so

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-gmic

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libgmic.so.1
/usr/lib64/libgmic.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gmic/5e489eefae18f5cc77435302ef0d9d04fac672f1
/usr/share/package-licenses/gmic/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/gmic/e48dd1d9bcb69a8b411bdcffcb04012d4b02e9e4
/usr/share/package-licenses/gmic/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gmic.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libgmic.a

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
Name     : gmic
Version  : 3.5.0
Release  : 45
URL      : https://gmic.eu/files/source/gmic_3.5.0.tar.gz
Source0  : https://gmic.eu/files/source/gmic_3.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CECILL-1.0 CECILL-1.1 GPL-3.0
Requires: gmic-bin = %{version}-%{release}
Requires: gmic-data = %{version}-%{release}
Requires: gmic-lib = %{version}-%{release}
Requires: gmic-license = %{version}-%{release}
Requires: gmic-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : extra-cmake-modules
BuildRequires : gimp-dev
BuildRequires : glibc-dev
BuildRequires : gmic-dev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev
BuildRequires : libXScrnSaver-dev
BuildRequires : libXau-dev
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXdamage-dev
BuildRequires : libXdmcp-dev
BuildRequires : libXext-dev
BuildRequires : libXfixes-dev
BuildRequires : libXft-dev
BuildRequires : libXi-dev
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : opencv-dev
BuildRequires : openexr-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(opencv)
BuildRequires : pkgconfig(opencv4)
BuildRequires : qt6base-dev
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
Requires: gmic-data = %{version}-%{release}
Requires: gmic-license = %{version}-%{release}

%description bin
bin components for the gmic package.


%package data
Summary: data components for the gmic package.
Group: Data

%description data
data components for the gmic package.


%package dev
Summary: dev components for the gmic package.
Group: Development
Requires: gmic-lib = %{version}-%{release}
Requires: gmic-bin = %{version}-%{release}
Requires: gmic-data = %{version}-%{release}
Provides: gmic-devel = %{version}-%{release}
Requires: gmic = %{version}-%{release}

%description dev
dev components for the gmic package.


%package lib
Summary: lib components for the gmic package.
Group: Libraries
Requires: gmic-data = %{version}-%{release}
Requires: gmic-license = %{version}-%{release}

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


%prep
%setup -q -n gmic-3.5.0
cd %{_builddir}/gmic-3.5.0
pushd ..
cp -a gmic-3.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735660886
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DENABLE_TIFF=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DENABLE_TIFF=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735660886
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gmic
cp %{_builddir}/gmic-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gmic/e48dd1d9bcb69a8b411bdcffcb04012d4b02e9e4 || :
cp %{_builddir}/gmic-%{version}/gmic-qt/COPYING %{buildroot}/usr/share/package-licenses/gmic/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/gmic-%{version}/gmic-qt/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/gmic/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gmic
/usr/bin/gmic

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/gmic

%files dev
%defattr(-,root,root,-)
/usr/include/CImg.h
/usr/include/gmic.h
/usr/lib64/cmake/gmic/GmicConfig.cmake
/usr/lib64/cmake/gmic/GmicTargets-relwithdebinfo.cmake
/usr/lib64/cmake/gmic/GmicTargets.cmake
/usr/lib64/libgmic.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgmic.so.1
/usr/lib64/libgmic.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gmic/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/gmic/e48dd1d9bcb69a8b411bdcffcb04012d4b02e9e4
/usr/share/package-licenses/gmic/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gmic.1

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gmic
Version  : 2.0.0
Release  : 2
URL      : http://gmic.eu/files/source/gmic_2.0.0.tar.gz
Source0  : http://gmic.eu/files/source/gmic_2.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CECILL-1.1
Requires: gmic-bin
Requires: gmic-lib
Requires: gmic-doc
BuildRequires : cmake
BuildRequires : gimp-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(opencv)

%description
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

%package bin
Summary: bin components for the gmic package.
Group: Binaries

%description bin
bin components for the gmic package.


%package dev
Summary: dev components for the gmic package.
Group: Development
Requires: gmic-lib
Requires: gmic-bin
Provides: gmic-devel

%description dev
dev components for the gmic package.


%package doc
Summary: doc components for the gmic package.
Group: Documentation

%description doc
doc components for the gmic package.


%package lib
Summary: lib components for the gmic package.
Group: Libraries

%description lib
lib components for the gmic package.


%prep
%setup -q -n gmic-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1497113598
mkdir clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DENABLE_TIFF=OFF
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1497113598
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib/gimp/2.0/plug-ins/gmic_film_cluts.gmz
/usr/lib/gimp/2.0/plug-ins/gmic_gimp_gtk

%files bin
%defattr(-,root,root,-)
/usr/bin/gmic

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libgmic.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgmic.so.1

Name:           sparsehash
Version:        2.0.2
Release:        5
License:        BSD-3-Clause
Summary:        Extremely memory-efficient hash_map implementation
Url:            http://code.google.com/p/sparsehash
Group:          Development/C++
Source0:        http://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# We're shipping only headers -- it's all inline
BuildArch:	noarch

%description
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

%package devel
Summary:        Extremely memory-efficient C++ hash_map implementation
Group:          Development/C++

%description devel
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

%prep
%setup -q
%configure

%build
%make

%check
%make check

%install
%makeinstall_std
rm %{buildroot}%{_docdir}/%{name}-%{version}/INSTALL
rm %{buildroot}%{_docdir}/%{name}-%{version}/README_windows.txt

%files devel
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}-%{version}/
%{_includedir}/google/
%{_includedir}/sparsehash/
%{_libdir}/pkgconfig/*.pc

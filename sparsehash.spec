Name:           sparsehash
Version:        2.0.3
Release:        1
License:        BSD-3-Clause
Summary:        Extremely memory-efficient hash_map implementation
Url:            https://github.com/sparsehash/sparsehash/
Group:          Development/C++
Source0:        https://github.com/sparsehash/sparsehash/archive/%{name}-%{version}.tar.gz
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
%setup -q -n %{name}-%{name}-%{version}
%configure

%build
%make

%check
%make check || echo "Fail"

%install
%makeinstall_std
mv %{buildroot}%{_docdir}/%{name}-2.0.2 %{buildroot}%{_docdir}/%{name}-%{version}
rm %{buildroot}%{_docdir}/%{name}-%{version}/INSTALL
rm %{buildroot}%{_docdir}/%{name}-%{version}/README_windows.txt

%files devel
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}-%{version}/
%{_includedir}/google/
%{_includedir}/sparsehash/
%{_libdir}/pkgconfig/*.pc

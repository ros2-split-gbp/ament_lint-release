%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-ament-cmake-copyright
Version:        0.10.7
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ament_cmake_copyright package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-ament-cmake-test
Requires:       ros-galactic-ament-copyright
Requires:       ros-galactic-ros-workspace
BuildRequires:  ros-galactic-ament-cmake-core
BuildRequires:  ros-galactic-ament-cmake-test
BuildRequires:  ros-galactic-ament-copyright
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-galactic-ament-cmake-lint-cmake
%endif

%description
The CMake API for ament_copyright to check every source file contains copyright
reference.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Thu Apr 28 2022 Audrow Nash <audrow@openrobotics.org> - 0.10.7-1
- Autogenerated by Bloom

* Fri May 07 2021 Audrow Nash <audrow@openrobotics.org> - 0.10.6-1
- Autogenerated by Bloom

* Tue Apr 20 2021 Audrow Nash <audrow@openrobotics.org> - 0.10.5-2
- Autogenerated by Bloom

* Wed Apr 14 2021 Audrow Nash <audrow@openrobotics.org> - 0.10.5-1
- Autogenerated by Bloom

* Thu Mar 18 2021 Claire Wang <clairewang@openrobotics.org> - 0.10.4-1
- Autogenerated by Bloom

* Mon Mar 08 2021 Claire Wang <clairewang@openrobotics.org> - 0.10.3-3
- Autogenerated by Bloom


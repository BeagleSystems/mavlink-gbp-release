Name:           ros-kinetic-mavlink
Version:        2016.12.12
Release:        0%{?dist}
Summary:        ROS mavlink package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://qgroundcontrol.org/mavlink/
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel
Requires:       ros-kinetic-catkin
BuildRequires:  cmake
BuildRequires:  python-devel
BuildRequires:  python-future
BuildRequires:  python-lxml
BuildRequires:  python-setuptools

%description
MAVLink message marshaling library. This package provides C-headers and C++11
library for both 1.0 and 2.0 versions of protocol. For pymavlink use separate
install via rosdep (python-pymavlink).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Dec 12 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.12.12-0
- Autogenerated by Bloom

* Fri Nov 11 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.11.11-0
- Autogenerated by Bloom

* Mon Nov 07 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.11.7-0
- Autogenerated by Bloom

* Sat Nov 05 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.11.5-0
- Autogenerated by Bloom

* Sun Oct 09 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.10.10-0
- Autogenerated by Bloom

* Wed Oct 05 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.10.5-0
- Autogenerated by Bloom

* Sun Oct 02 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.10.2-0
- Autogenerated by Bloom

* Fri Sep 09 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.9.9-0
- Autogenerated by Bloom

* Thu Aug 25 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.8.25-0
- Autogenerated by Bloom

* Mon Aug 08 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.8.8-0
- Autogenerated by Bloom

* Tue Aug 02 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.8.2-1
- Autogenerated by Bloom

* Tue Aug 02 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.8.2-0
- Autogenerated by Bloom

* Thu Jul 07 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.7.7-0
- Autogenerated by Bloom

* Fri Jun 24 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.6.24-0
- Autogenerated by Bloom

* Wed Jun 22 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.6.22-1
- Autogenerated by Bloom

* Wed Jun 22 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.6.22-0
- Autogenerated by Bloom

* Sat Jun 11 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.6.12-0
- Autogenerated by Bloom

* Fri Jun 10 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.6.10-0
- Autogenerated by Bloom

* Wed Jun 08 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.6.8-1
- Autogenerated by Bloom

* Wed Jun 08 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.6.8-0
- Autogenerated by Bloom

* Tue Jun 07 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.6.7-0
- Autogenerated by Bloom

* Fri May 20 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.5.20-0
- Autogenerated by Bloom

* Mon May 16 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.5.16-0
- Autogenerated by Bloom

* Sun May 15 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.5.15-1
- Autogenerated by Bloom

* Sun May 15 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.5.15-0
- Autogenerated by Bloom

* Mon Apr 04 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.4.4-0
- Autogenerated by Bloom


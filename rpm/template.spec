Name:           ros-jade-industrial-msgs
Version:        0.5.1
Release:        0%{?dist}
Summary:        ROS industrial_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/industrial_msg
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-genmsg
Requires:       ros-jade-message-runtime
Requires:       ros-jade-std-msgs
Requires:       ros-jade-trajectory-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-genmsg
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-trajectory-msgs

%description
The industrial message package containes industrial specific messages
definitions. This package is part of the ROS-Industrial program.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Jan 15 2017 Shaun Edwards <sedwards@swri.org> - 0.5.1-0
- Autogenerated by Bloom

* Mon Feb 22 2016 Shaun Edwards <sedwards@swri.org> - 0.5.0-0
- Autogenerated by Bloom

* Sun Feb 21 2016 Shaun Edwards <sedwards@swri.org> - 0.4.3-0
- Autogenerated by Bloom

